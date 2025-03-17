from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime
import redis
import yaml
from generate_docs import DocumentGenerator
import json
import os

app = FastAPI()

# Настраиваем CORS для работы с веб-интерфейсом
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключаемся к Redis
REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')
redis_client = redis.Redis(host=REDIS_HOST, port=6379, db=0, decode_responses=True)

class DocumentRequest(BaseModel):
    template_name: str
    context: dict

def get_daily_requests_key():
    """Получаем ключ для текущего дня"""
    today = datetime.now().strftime('%Y-%m-%d')
    return f"document_requests:{today}"

def increment_daily_requests():
    """Увеличиваем счетчик запросов за день"""
    key = get_daily_requests_key()
    try:
        current = redis_client.get(key)
        
        if current is None:
            # Если это первый запрос за день, устанавливаем счетчик
            redis_client.setex(key, 86400, 1)  # TTL: 24 часа
            return 1
        
        current = int(current)
        if current >= 50:
            raise HTTPException(status_code=429, detail="Превышен лимит запросов на сегодня (50)")
        
        redis_client.incr(key)
        return current + 1
    except redis.ConnectionError:
        # Если Redis недоступен, пропускаем проверку
        return 1

@app.post("/generate")
async def generate_document(request: DocumentRequest):
    # Проверяем лимит запросов
    requests_count = increment_daily_requests()
    
    try:
        generator = DocumentGenerator()
        document = generator.generate_document(
            request.template_name,
            request.context
        )
        
        return {
            "status": "success",
            "document": document,
            "requests_remaining": 50 - requests_count
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/templates")
async def list_templates():
    """Получаем список доступных шаблонов"""
    try:
        with open('config.yml', 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
        return {"templates": [doc['template'] for doc in config['documents']]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/requests/remaining")
async def get_remaining_requests():
    """Получаем количество оставшихся запросов на сегодня"""
    try:
        key = get_daily_requests_key()
        current = redis_client.get(key)
        used = int(current) if current else 0
        return {"remaining": 50 - used}
    except redis.ConnectionError:
        # Если Redis недоступен, возвращаем максимальное количество
        return {"remaining": 50}

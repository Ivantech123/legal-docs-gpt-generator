import os
import yaml
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

class DocumentGenerator:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        self.env = Environment(loader=FileSystemLoader('templates'))
        
    def enhance_with_gpt(self, text, context):
        """Улучшает текст документа с помощью GPT"""
        response = self.client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {"role": "system", "content": "Вы - опытный юрист. Помогите улучшить юридический документ."},
                {"role": "user", "content": f"Контекст документа: {context}\n\nТекст документа:\n{text}"}
            ]
        )
        return response.choices[0].message.content

    def generate_document(self, template_name, context):
        """Генерирует документ из шаблона"""
        template = self.env.get_template(template_name)
        document = template.render(**context)
        enhanced_document = self.enhance_with_gpt(document, str(context))
        return enhanced_document

    def save_document(self, content, output_path):
        """Сохраняет документ"""
        Path(output_path).write_text(content, encoding='utf-8')

def main():
    generator = DocumentGenerator()
    
    # Загружаем конфигурацию документов
    with open('config.yml', 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    
    # Генерируем каждый документ
    for doc in config['documents']:
        content = generator.generate_document(
            doc['template'],
            doc['context']
        )
        generator.save_document(content, f"docs/{doc['output']}")

if __name__ == '__main__':
    main()

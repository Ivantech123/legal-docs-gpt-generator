# 🤖 Legal Docs GPT Generator

[![GitHub Actions](https://github.com/Ivantech123/legal-docs-gpt-generator/actions/workflows/generate-docs.yml/badge.svg)](https://github.com/Ivantech123/legal-docs-gpt-generator/actions)
[![Website](https://img.shields.io/website?url=https%3A%2F%2Fivantech123.github.io%2Flegal-docs-gpt-generator%2F)](https://ivantech123.github.io/legal-docs-gpt-generator/)
[![GitHub license](https://img.shields.io/github/license/Ivantech123/legal-docs-gpt-generator)](https://github.com/Ivantech123/legal-docs-gpt-generator/blob/main/LICENSE)

Умный генератор юридических документов с использованием GPT и GitHub Actions. Автоматизирует создание и улучшение юридических документов.

🌐 [Открыть веб-сайт](https://ivantech123.github.io/legal-docs-gpt-generator/)

## ✨ Возможности

- 📝 **Автоматическая генерация** - создание документов из шаблонов
- 🤖 **GPT улучшения** - автоматическое улучшение текста с помощью ИИ
- 🔄 **GitHub Actions** - автоматическая генерация при изменении шаблонов
- 📋 **Готовые шаблоны** - базовые шаблоны юридических документов
- 🔒 **Безопасность** - защита конфиденциальных данных

## 🚀 Быстрый старт

1. Клонируйте репозиторий:
```bash
git clone https://github.com/Ivantech123/legal-docs-gpt-generator.git
cd legal-docs-gpt-generator
```

2. Установите зависимости:
```bash
pip install -r requirements.txt
```

3. Создайте файл `.env` с вашими API ключами:
```env
OPENAI_API_KEY=your_api_key_here
```

4. Добавьте свой шаблон в `templates/` и настройте его в `config.yml`

5. Запустите генерацию:
```bash
python generate_docs.py
```

## 📂 Структура проекта

```
.
├── .github/workflows/  # GitHub Actions
│   ├── generate-docs.yml
│   └── static.yml
├── templates/         # Шаблоны документов
│   └── contract.md
├── docs/             # Сгенерированные документы и веб-сайт
├── generate_docs.py  # Скрипт генерации
└── config.yml       # Конфигурация
```

## 🛠️ Как это работает

1. **Создание шаблона**
   - Добавьте шаблон в формате Markdown в папку `templates/`
   - Используйте Jinja2 синтаксис для переменных

2. **Настройка данных**
   - Укажите параметры документа в `config.yml`
   - Настройте метаданные и переменные

3. **Генерация и улучшение**
   - GitHub Actions автоматически запускает генерацию
   - GPT анализирует и улучшает текст
   - Результат сохраняется в `docs/`

4. **Публикация**
   - Документы автоматически публикуются на GitHub Pages
   - Доступны через веб-интерфейс

## 🔧 Настройка

1. Добавьте `OPENAI_API_KEY` в секреты репозитория:
   - Settings → Secrets → Actions → New repository secret
   - Имя: `OPENAI_API_KEY`
   - Значение: ваш ключ OpenAI API

2. Включите GitHub Pages:
   - Settings → Pages
   - Source: GitHub Actions

## 📚 Примеры документов

- [Договор подряда](https://ivantech123.github.io/legal-docs-gpt-generator/examples.html)
- [Все примеры](https://ivantech123.github.io/legal-docs-gpt-generator/examples.html)

## 📝 Лицензия

MIT License - используйте свободно для любых целей

## 🤝 Участие в проекте

Мы приветствуем ваш вклад в проект! Вы можете:
1. Создавать Issue с предложениями
2. Добавлять новые шаблоны документов
3. Улучшать код и документацию

## 📞 Контакты

- 🌐 Сайт: [legal-docs-gpt-generator](https://ivantech123.github.io/legal-docs-gpt-generator/)
- 📂 GitHub: [Репозиторий проекта](https://github.com/Ivantech123/legal-docs-gpt-generator)

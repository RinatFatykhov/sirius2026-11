# Как начать работу

## 1. Установить зависимости

Linux:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Windows:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

## Добавить `.env`

Создать файл с названием `.env` и внести в него следующие данные:

```bash
API_URL=...
API_KEY=...
MODEL=...
```

# Запуск

Запустить ноутбук:

```bash
uv run marimo edit
```

Запустить скрипт:

```bash
uv run examples/01_call_llm.py
```

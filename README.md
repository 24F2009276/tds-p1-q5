# Data Analyst Telegram Bot

A Telegram bot that acts as a data analysis agent using an LLM. The bot receives data analysis questions through Telegram, performs any required computation or retrieval, and replies with a single JSON object in the required format.

## Features

- Accepts data analysis questions via Telegram
- Uses an OpenAI-compatible LLM API
- Supports Python-based analysis when needed
- Returns responses as JSON only
- Logs every interaction to a public JSONL log

## Repository Structure

```
.
├── bot.py              # Main application
├── requirements.txt    # Python dependencies
├── .gitignore
└── README.md
```

## Environment Variables

Create a `.env` file or configure the following environment variables:

```text
BOT_TOKEN=<telegram bot token>
AIPIPE_TOKEN=<AIPIPE API token>
MODEL=gpt-4o-mini
MODEL_BASE_URL=https://aipipe.org/openai/v1
BASE_URL=<your deployed application URL>
```

## Installation

```bash
pip install -r requirements.txt
```

## Running Locally

```bash
python bot.py
```

The application starts a FastAPI server and continuously polls Telegram for incoming messages.

## Deployment

The bot is deployed on Render and exposes:

- `/health` – health check endpoint
- `/run.jsonl` – public JSONL execution log

## Response Format

The bot replies with exactly one JSON object:

```json
{
  "answer": "...",
  "log_url": "https://<deployment-url>/run.jsonl"
}
```

where the structure of `answer` matches the format requested in the user's message.

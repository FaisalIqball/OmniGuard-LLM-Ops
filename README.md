# OmniGuard-LLM-Ops 🛡️

OmniGuard is an advanced safety and reliability layer for Large Language Models. It provides real-time guardrails to prevent PII leaks, detect hallucinations, and ensure enterprise-grade security for AI deployments.

## 🌟 Features

- **PII Anonymization**: Automatically detects and masks sensitive information (Names, Emails, SSNs, API Keys) before they reach the LLM.
- **Hallucination Detection**: Uses NLI (Natural Language Inference) and G-Eval metrics to score the factual consistency of LLM responses.
- **Toxicity & Bias Filtering**: Multi-layer filtering to prevent harmful, biased, or inappropriate content generation.
- **Red-Teaming Engine**: Integrated module for automated adversarial testing (Prompt Injection, Jailbreaking).
- **FastAPI Wrapper**: Drop-in middleware for any LLM-based API.

## 🏗️ System Overview

OmniGuard acts as a proxy between your application and the LLM provider (OpenAI, Anthropic, Local).

```text
User Request --> [ PII Masking ] --> [ LLM API ] --> [ Hallucination Check ] --> User Response
                       ^                                       |
                       |---------- Guardrail Logging ----------|
```

## 🚀 Deployment

### Using Docker

```bash
docker-compose up -d
```

### Manual Setup

```bash
pip install -r requirements.txt
python -m api.main
```

## 📊 Evaluation Metrics

OmniGuard provides a dashboard to monitor:
- **Safety Health**: Percentage of blocked requests.
- **Factual Accuracy**: Average hallucination scores.
- **Latency Impact**: Overhead introduced by the guardrails.

## 📜 License
MIT

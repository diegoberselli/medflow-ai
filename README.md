# 🏥 Automação Médica com N8N e IA

> Sistema completo de automação médica integrando N8N, IA, banco de dados e APIs externas

## 🚀 Quick Start

### 1. **Setup Ambiente**
```bash
# Clonar e configurar
git clone <repo>
cd medical-automation

# Ambiente Python
python -m venv venv
venv\Scripts\activate
python setup.py
```

### 2. **Executar Sistema**
```bash
# Terminal 1 - API
cd api
python main.py
# ✅ API: http://localhost:8000

# Terminal 2 - N8N
npm install n8n -g
n8n start
# ✅ N8N: http://localhost:5678
```

### 3. **Importar Workflow**
- Abrir http://localhost:5678
- Importar: `n8n/complete-medical-workflow.json`
- Ativar workflow

## 🏗️ Arquitetura

```
Paciente → N8N Webhook → API Flask → SQLite
    ↓           ↓           ↓         ↓
  Texto      Workflow    Endpoints  Dados
  Áudio      Automation  REST API   Médicos
             IA Process             Pacientes
                ↓                   Consultas
           Gmail + TTS
```

## 🗄️ Banco de Dados

| Tabela | Campos |
|--------|--------|
| **patients** | id, name, email, phone |
| **doctors** | id, name, specialty, price |
| **appointments** | id, patient_id, doctor_id, datetime, status |
| **schedule** | id, doctor_id, datetime, available |

## 🔌 API Endpoints

| Método | Endpoint | Descrição |
|--------|----------|----------|
| GET | `/doctors` | Listar médicos |
| GET | `/doctors/{id}/schedule` | Horários disponíveis |
| POST | `/appointments` | Agendar consulta |
| DELETE | `/appointments/{id}` | Cancelar consulta |
| GET | `/payment-info` | Formas de pagamento |
| POST | `/chat` | Chat com IA |
| POST | `/process-audio` | Processamento áudio |

## 🧪 Testes Rápidos

```bash
# API Status
curl http://localhost:8000/

# Chat IA
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Quais horários disponíveis?"}'

# N8N Webhook
curl -X POST http://localhost:5678/webhook/medical-chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Quero agendar", "type": "text"}'
```

## ⚙️ Configuração Opcional

### Gmail (Emails Automáticos)
```python
# api/email_service.py
sender_email = "seu-email@gmail.com"
sender_password = "sua-senha-app"  # Gmail App Password
```

### OpenAI (TTS/STT)
```python
# api/tts_service.py
openai.api_key = "sk-sua-api-key"
```

## 📁 Estrutura do Projeto

```
medical-automation/
├── api/                 # API Flask
│   ├── main.py         # Endpoints principais
│   ├── database.py     # Modelos SQLAlchemy
│   ├── email_service.py # Envio de emails
│   ├── tts_service.py  # Áudio ↔ Texto
│   └── ai_service.py   # Processamento IA
├── n8n/                # Workflows N8N
├── docs/               # Documentação
│   ├── DOCUMENTACAO_COMPLETA.md
│   ├── GUIA_DEMONSTRACAO.md
│   └── Medical-API.postman_collection.json
└── README.md
```

## 🎯 Funcionalidades

### ✅ Implementado
- **API REST** completa com SQLite
- **N8N Workflow** com processamento inteligente
- **Chat multimodal** (texto + áudio)
- **Emails automáticos** (agendamento/cancelamento)
- **IA conversacional** com OpenAI
- **Documentação** completa

### 🔄 Fluxos Principais
1. **Consultar horários** → N8N → API → Resposta
2. **Agendar consulta** → N8N → API → Email confirmação
3. **Cancelar consulta** → N8N → API → Email cancelamento
4. **Consultar pagamento** → N8N → API → Informações

## 📊 Dados de Teste
- **3 Pacientes**: João, Maria, Pedro
- **3 Médicos**: Dr. Carlos (Cardiologia), Dra. Ana (Dermatologia), Dr. Paulo (Clínico)
- **126 Horários**: 7 dias × 6 horários/dia × 3 médicos

## 🛠️ Ferramentas de Teste
- **Postman Collection**: `docs/Medical-API.postman_collection.json`
- **Checklist**: `docs/demo-checklist.md`
- **Documentação**: `docs/DOCUMENTACAO_COMPLETA.md`


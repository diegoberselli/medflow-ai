# 🎬 Guia de Demonstração - Automação Médica

## 🎯 Roteiro de Apresentação (10 minutos)

### 1. **Introdução (1 min)**
"Implementei uma automação médica completa integrando N8N, IA, banco de dados e APIs externas."

**Mostrar arquitetura:**
- API Flask + SQLite
- N8N Workflow
- Integrações Gmail + OpenAI

### 2. **Demonstração da API (2 min)**

**Terminal 1 - Status da API:**
```bash
curl http://localhost:8000/
```

**Mostrar médicos cadastrados:**
```bash
curl http://localhost:8000/doctors
```

**Demonstrar chat com IA:**
```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Quais horários disponíveis?"}'
```

### 3. **N8N Workflow (3 min)**

**Abrir N8N:** http://localhost:5678

**Mostrar workflow visual:**
- Webhook de entrada
- Processamento de texto/áudio
- Identificação de intenção
- Chamadas para API
- Resposta automática

**Testar webhook:**
```bash
curl -X POST http://localhost:5678/webhook/medical-chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Quero agendar uma consulta", "type": "text"}'
```

### 4. **Banco de Dados (1 min)**

**Mostrar estrutura:**
```bash
# No diretório api/
sqlite3 medical.db ".tables"
sqlite3 medical.db "SELECT * FROM doctors;"
sqlite3 medical.db "SELECT * FROM patients;"
```

### 5. **Funcionalidades Avançadas (2 min)**

**Agendamento com email:**
```bash
curl -X POST http://localhost:8000/appointments \
  -H "Content-Type: application/json" \
  -d '{
    "patient_id": 1,
    "doctor_id": 1,
    "datetime": "2024-01-15T10:00:00"
  }'
```

**Mostrar:** Email enviado automaticamente

**Processamento de áudio (se configurado):**
```bash
curl -X POST http://localhost:8000/process-audio \
  -H "Content-Type: application/json" \
  -d '{"audio_base64": "exemplo_base64"}'
```

### 6. **Conclusão (1 min)**

**Resumir implementação:**
- ✅ API REST completa
- ✅ N8N integrado
- ✅ Multimodal (texto/áudio)
- ✅ Emails automáticos
- ✅ IA conversacional

## 🎥 Script de Demonstração

### Cenário 1: Consultar Horários
```
"Vou simular um paciente consultando horários disponíveis..."

[Executar comando curl]
[Mostrar resposta da API]
[Mostrar execução no N8N]
```

### Cenário 2: Agendar Consulta
```
"Agora vou agendar uma consulta e mostrar o email automático..."

[Executar agendamento]
[Mostrar banco atualizado]
[Mostrar email enviado]
```

### Cenário 3: Workflow Completo
```
"Este é o fluxo completo no N8N, processando diferentes tipos de mensagem..."

[Mostrar workflow visual]
[Executar diferentes intenções]
[Mostrar respostas condicionais]
```

## 📋 Checklist de Demonstração

### Antes da Apresentação
- [ ] API rodando (http://localhost:8000)
- [ ] N8N ativo (http://localhost:5678)
- [ ] Workflow importado e ativo
- [ ] Banco populado com dados
- [ ] Postman collection pronta
- [ ] Terminais organizados

### Durante a Apresentação
- [ ] Mostrar código da API
- [ ] Demonstrar endpoints principais
- [ ] Executar workflow N8N
- [ ] Mostrar banco de dados
- [ ] Testar cenários diferentes
- [ ] Explicar integrações

### Pontos de Destaque
- [ ] Arquitetura modular
- [ ] Processamento multimodal
- [ ] Integração N8N + API
- [ ] Emails automáticos
- [ ] IA conversacional
- [ ] Documentação completa

## 🎯 Perguntas Frequentes

**P: Como funciona a integração N8N + API?**
R: O N8N recebe webhooks, processa com IA, chama endpoints da API e retorna respostas estruturadas.

**P: O sistema suporta áudio?**
R: Sim, com OpenAI Whisper (STT) e TTS para conversão áudio↔texto.

**P: Como são enviados os emails?**
R: Automaticamente via Gmail SMTP quando consultas são agendadas/canceladas.

**P: O banco é escalável?**
R: SQLite para demo, mas estrutura suporta PostgreSQL/MySQL.

**P: Há testes implementados?**
R: Collection Postman completa + checklist de validação.

## 🚀 Comandos Rápidos para Demo

```bash
# Verificar API
curl http://localhost:8000/

# Testar chat
curl -X POST http://localhost:8000/chat -H "Content-Type: application/json" -d '{"message": "horários"}'

# Testar N8N
curl -X POST http://localhost:5678/webhook/medical-chat -H "Content-Type: application/json" -d '{"message": "Quero agendar", "type": "text"}'

# Ver médicos
curl http://localhost:8000/doctors

# Ver horários
curl http://localhost:8000/doctors/1/schedule

# Agendar consulta
curl -X POST http://localhost:8000/appointments -H "Content-Type: application/json" -d '{"patient_id":1,"doctor_id":1,"datetime":"2024-01-15T10:00:00"}'
```

## 📊 Métricas de Sucesso

- **Tempo de resposta API**: < 100ms
- **Execução workflow N8N**: < 2s
- **Taxa de sucesso**: 100%
- **Cobertura de requisitos**: 100%
- **Funcionalidades extras**: 5+

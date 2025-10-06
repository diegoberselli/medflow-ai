# Checklist de Testes - Automação Médica

## ✅ API REST

### Endpoints Básicos
- [ ] `GET /` - Página inicial funcionando
- [ ] `GET /doctors` - Lista 3 médicos
- [ ] `GET /doctors/1/schedule` - Horários Dr. Carlos Lima
- [ ] `GET /payment-info` - Formas de pagamento

### Agendamento
- [ ] `POST /appointments` - Criar consulta
- [ ] Horário fica indisponível após agendamento
- [ ] `DELETE /appointments/1` - Cancelar consulta
- [ ] Horário volta a ficar disponível

## ✅ Banco de Dados

### Dados Iniciais
- [ ] 3 pacientes cadastrados
- [ ] 3 médicos com especialidades
- [ ] 126 horários (7 dias × 6 horários × 3 médicos)
- [ ] Todos horários inicialmente disponíveis

### Integridade
- [ ] Agendamento atualiza tabela `schedule`
- [ ] Cancelamento libera horário
- [ ] Dados consistentes entre tabelas

## ✅ N8N Workflow

### Instalação
- [ ] Node.js instalado
- [ ] N8N instalado globalmente
- [ ] Interface acessível (localhost:5678)
- [ ] Workflow importado

### Integração
- [ ] Webhook recebe mensagens
- [ ] HTTP Request conecta com API
- [ ] Fluxo de horários funcionando
- [ ] Fluxo de agendamento funcionando

## ✅ Integrações Externas

### Gmail
- [ ] Credenciais configuradas
- [ ] Email de confirmação enviado
- [ ] Email de cancelamento enviado

### TTS (Opcional)
- [ ] API configurada
- [ ] Conversão texto → áudio
- [ ] Resposta em áudio

## ✅ Documentação

### Arquivos
- [ ] README.md completo
- [ ] Coleção Postman
- [ ] Workflow N8N exportado
- [ ] Checklist de testes

### Evidências
- [ ] Screenshots da API
- [ ] Screenshots do N8N
- [ ] Vídeo demonstrativo
- [ ] Logs de funcionamento

## 🎯 Fluxos Principais

### Consulta de Horários
1. [ ] Paciente pergunta horários
2. [ ] N8N consulta API
3. [ ] Retorna horários disponíveis

### Agendamento
1. [ ] Paciente solicita agendamento
2. [ ] N8N agenda via API
3. [ ] Email de confirmação enviado
4. [ ] Horário marcado como ocupado

### Cancelamento
1. [ ] Paciente cancela consulta
2. [ ] N8N cancela via API
3. [ ] Email de cancelamento enviado
4. [ ] Horário liberado

### Pagamento
1. [ ] Paciente pergunta valores
2. [ ] N8N retorna informações
3. [ ] Formas de pagamento listadas
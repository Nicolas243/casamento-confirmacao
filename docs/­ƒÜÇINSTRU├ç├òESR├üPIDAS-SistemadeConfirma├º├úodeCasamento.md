# 🚀 INSTRUÇÕES RÁPIDAS - Sistema de Confirmação de Casamento

## ⚡ CONFIGURAÇÃO ESSENCIAL (OBRIGATÓRIA)

### 1. CONFIGURE O WHATSAPP
Abra o arquivo `config.py` e substitua:
```python
WHATSAPP_GROUP_URL = "https://chat.whatsapp.com/XXXXXXXXXXXXXXX"
```
Pelo link real do seu grupo do WhatsApp.

**Como obter o link:**
1. WhatsApp → Grupo do casamento → ⋮ (três pontos) → Convidar via link → Copiar

### 2. EXECUTE O SISTEMA
```bash
cd confirmacao_casamento
source venv/bin/activate
python src/main.py
```

### 3. ACESSE AS PÁGINAS
- **Convidados**: http://localhost:5000
- **Administração**: http://localhost:5000/admin.html

## 🎯 COMO FUNCIONA

### Para CONVIDADOS:
- **SIM** → Vai direto para o WhatsApp
- **NÃO** → Preenche formulário com nome e familiares

### Para VOCÊ (administrador):
- Acesse `/admin.html` para ver todas as confirmações
- Exporte CSV para planilha
- Monitore em tempo real

## ⚠️ IMPORTANTE

1. **TESTE PRIMEIRO**: Teste com alguns amigos antes de enviar para todos
2. **BACKUP**: Faça backup do arquivo `src/database/app.db` regularmente
3. **LINK WHATSAPP**: Certifique-se de que o link está funcionando

## 🆘 PROBLEMAS COMUNS

- **Erro de módulo**: `source venv/bin/activate` e `pip install -r requirements.txt`
- **Porta ocupada**: Mate processos com `sudo lsof -t -i tcp:5000 | xargs kill -9`
- **WhatsApp não abre**: Verifique o link no `config.py`

## 📱 PARA DEPLOY ONLINE

Quando quiser colocar online para os convidados acessarem, me avise que eu faço o deploy gratuito para você!

---
**✅ PRONTO! Seu sistema está funcionando!**


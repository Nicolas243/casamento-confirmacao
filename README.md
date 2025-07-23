# Sistema de Confirmação de Presença para Casamento

Sistema web completo para confirmação de presença em casamentos, desenvolvido especialmente para **Nicolas e Julia**.

## 🚀 Como Usar

### 1. Clone o repositório
```bash
git clone https://github.com/SEU_USUARIO/casamento-confirmacao.git
cd casamento-confirmacao
```

### 2. Instale as dependências
```bash
pip install -r requirements.txt
```

### 3. Configure o WhatsApp
Edite o arquivo `config.py` e substitua:
```python
WHATSAPP_GROUP_URL = "https://chat.whatsapp.com/XXXXXXXXXXXXXXX"
```
Pelo link real do seu grupo do WhatsApp.

### 4. Execute o sistema
```bash
python src/main.py
```

### 5. Acesse as páginas
- **Convidados**: http://localhost:5000
- **Administração**: http://localhost:5000/admin.html

## 📱 Como Funciona

### Para CONVIDADOS:
- **SIM** → Vai direto para o WhatsApp
- **NÃO** → Preenche formulário com nome e familiares

### Para VOCÊ (administrador):
- Acesse `/admin.html` para ver todas as confirmações
- Exporte CSV para planilha
- Monitore em tempo real

## 🌐 Deploy

Para colocar online, você pode usar:
- Heroku
- Railway
- Render
- PythonAnywhere

## 📞 Suporte

Para dúvidas ou problemas, consulte a documentação completa nos arquivos markdown incluídos.


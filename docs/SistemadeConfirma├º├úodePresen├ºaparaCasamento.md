# Sistema de Confirmação de Presença para Casamento

## 📋 Descrição

Sistema web completo para confirmação de presença em casamentos, desenvolvido especialmente para **Nicolas e Julia**. O sistema permite que os convidados confirmem sua presença de forma simples e elegante, com redirecionamento automático para WhatsApp para quem confirma presença e coleta de dados para quem não pode comparecer.

## ✨ Funcionalidades

### 🎯 Página Principal
- **Design elegante e responsivo** com tema romântico
- **Versículo bíblico** (Mateus 5:37) como inspiração
- **Dois botões principais**: SIM e NÃO
- **Redirecionamento automático** para grupo do WhatsApp (botão SIM)
- **Modal de coleta de dados** para quem não vai comparecer (botão NÃO)

### 📊 Painel Administrativo
- **Estatísticas em tempo real** das confirmações
- **Lista completa** de todas as respostas
- **Filtros** por tipo de confirmação (SIM/NÃO)
- **Exportação em CSV** para análise externa
- **Atualização automática** a cada 30 segundos

### 🔧 Funcionalidades Técnicas
- **API REST** completa para gerenciamento de dados
- **Banco de dados SQLite** para armazenamento
- **Validação de dados** e prevenção de duplicatas
- **Design responsivo** para desktop e mobile
- **CORS habilitado** para integração

## 🚀 Como Usar

### 1. Personalização Inicial

**IMPORTANTE**: Antes de usar, você DEVE personalizar o link do WhatsApp:

1. Abra o arquivo `config.py`
2. Substitua a linha:
   ```python
   WHATSAPP_GROUP_URL = "https://chat.whatsapp.com/XXXXXXXXXXXXXXX"
   ```
   Pelo link real do seu grupo do WhatsApp

**Como obter o link do WhatsApp:**
1. Abra o grupo do WhatsApp do casamento
2. Toque nos três pontos (menu)
3. Selecione "Convidar via link"
4. Copie o link e cole no arquivo `config.py`

### 2. Executando o Sistema

```bash
# 1. Entre na pasta do projeto
cd confirmacao_casamento

# 2. Ative o ambiente virtual
source venv/bin/activate

# 3. Execute o servidor
python src/main.py
```

O sistema estará disponível em: `http://localhost:5000`

### 3. Acessando as Páginas

- **Página Principal**: `http://localhost:5000`
- **Painel Admin**: `http://localhost:5000/admin.html`

## 📱 Como os Convidados Usam

### Para quem VAI ao casamento:
1. Acessa a página
2. Clica no botão **"SIM"**
3. É redirecionado automaticamente para o grupo do WhatsApp

### Para quem NÃO VAI ao casamento:
1. Acessa a página
2. Clica no botão **"NÃO"**
3. Preenche o formulário com:
   - Nome completo
   - Lista de familiares que também não irão (opcional)
4. Clica em "Confirmar"
5. Recebe mensagem de confirmação

## 🎨 Personalização Avançada

### Alterando Nomes dos Noivos
No arquivo `config.py`, modifique:
```python
NOME_NOIVOS = "Seus Nomes Aqui"
```

### Alterando o Versículo
No arquivo `config.py`, modifique:
```python
VERSICULO_BIBLICO = "Seu versículo preferido aqui"
```

### Alterando Cores e Design
Edite o arquivo `src/static/index.html` na seção `<style>` para personalizar:
- Cores do gradiente
- Fontes
- Tamanhos
- Animações

## 🌐 Deploy para Produção

### Opção 1: Deploy Automático (Recomendado)
```bash
# Execute este comando na pasta do projeto
# (será implementado automaticamente)
```

### Opção 2: Hospedagem Manual
1. **Heroku, Railway, ou similar**:
   - Faça upload dos arquivos
   - Configure as variáveis de ambiente
   - Execute `python src/main.py`

2. **VPS próprio**:
   - Instale Python 3.11+
   - Transfira os arquivos
   - Configure nginx/apache como proxy reverso
   - Use gunicorn para produção

## 📊 Gerenciamento de Dados

### Visualizando Confirmações
1. Acesse `http://localhost:5000/admin.html`
2. Veja as estatísticas em tempo real
3. Use os filtros para organizar os dados
4. Clique em "Exportar CSV" para baixar planilha

### Estrutura dos Dados
Cada confirmação contém:
- **Nome**: Nome completo do convidado
- **Status**: SIM (vai) ou NÃO (não vai)
- **Familiares**: Lista de familiares que não vão (apenas para NÃO)
- **Data/Hora**: Timestamp da confirmação
- **IP**: Endereço IP (para evitar duplicatas)

## 🔒 Segurança

### Proteções Implementadas
- **Validação de dados** no frontend e backend
- **Prevenção de duplicatas** por nome
- **Sanitização de inputs** para evitar ataques
- **CORS configurado** adequadamente

### Para Produção
1. Altere a `SECRET_KEY` no arquivo `config.py`
2. Use HTTPS sempre que possível
3. Configure backup do banco de dados
4. Monitore logs de acesso

## 🛠️ Estrutura do Projeto

```
confirmacao_casamento/
├── src/
│   ├── models/
│   │   ├── user.py          # Modelo de usuário (padrão)
│   │   └── confirmacao.py   # Modelo de confirmação
│   ├── routes/
│   │   ├── user.py          # Rotas de usuário (padrão)
│   │   └── confirmacao.py   # Rotas de confirmação
│   ├── static/
│   │   ├── index.html       # Página principal
│   │   └── admin.html       # Painel administrativo
│   ├── database/
│   │   └── app.db          # Banco de dados SQLite
│   └── main.py             # Arquivo principal do Flask
├── venv/                   # Ambiente virtual Python
├── config.py              # Configurações personalizáveis
├── requirements.txt       # Dependências Python
└── README.md             # Esta documentação
```

## 🆘 Solução de Problemas

### Erro: "Módulo não encontrado"
```bash
# Certifique-se de estar no ambiente virtual
source venv/bin/activate
pip install -r requirements.txt
```

### Erro: "Porta já em uso"
```bash
# Mate processos na porta 5000
sudo lsof -t -i tcp:5000 | xargs kill -9
```

### Erro: "Banco de dados não encontrado"
```bash
# Recrie o banco de dados
rm src/database/app.db
python src/main.py
```

### WhatsApp não abre
1. Verifique se o link no `config.py` está correto
2. Teste o link manualmente no navegador
3. Certifique-se de que o grupo existe e está ativo

## 📞 Suporte

Para dúvidas ou problemas:
1. Verifique esta documentação
2. Consulte os logs do servidor
3. Teste em modo debug (`debug=True` no `main.py`)

## 🎉 Parabéns!

Seu sistema de confirmação de presença está pronto! 

**Lembre-se**:
- ✅ Personalizar o link do WhatsApp
- ✅ Testar com alguns convidados primeiro
- ✅ Fazer backup dos dados regularmente
- ✅ Monitorar as confirmações pelo painel admin

**Desejamos um casamento maravilhoso para Nicolas e Julia! 💒💕**


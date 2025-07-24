# Configurações do Sistema de Confirmação de Casamento

# ===== CONFIGURAÇÕES DO WHATSAPP =====
# Substitua pela URL real do seu grupo do WhatsApp
# Para obter a URL: Abra o grupo > Três pontos > Convidar via link > Copiar link
WHATSAPP_GROUP_URL = "https://chat.whatsapp.com/DWuroOdBooEKZYmLqF8O7W"

# ===== CONFIGURAÇÕES DO CASAMENTO =====
NOME_NOIVOS = "Nicolas e Julia"
VERSICULO_BIBLICO = '"Jesus disse: \'Seja o seu \'sim\', \'sim\', e o seu \'não\', \'não\'; o que passar disso vem do maligno.\'" - Mateus 5:37'

# ===== CONFIGURAÇÕES DO SISTEMA =====
# Permitir múltiplas confirmações do mesmo IP (útil para famílias)
PERMITIR_MULTIPLAS_CONFIRMACOES_MESMO_IP = True

# Limite de caracteres para o campo familiares
LIMITE_CARACTERES_FAMILIARES = 500

# ===== CONFIGURAÇÕES DE SEGURANÇA =====
# Chave secreta do Flask (altere para uma chave única em produção)
SECRET_KEY = "nicolas2025julia"

# ===== CONFIGURAÇÕES DE BANCO DE DADOS =====
# Caminho do banco de dados SQLite
DATABASE_PATH = "database/app.db"

# ===== INSTRUÇÕES DE USO =====
"""
COMO PERSONALIZAR:

1. LINK DO WHATSAPP:
   - Abra o grupo do WhatsApp do casamento
   - Toque nos três pontos (menu)
   - Selecione "Convidar via link"
   - Copie o link e substitua na variável WHATSAPP_GROUP_URL acima

2. NOMES DOS NOIVOS:
   - Altere a variável NOME_NOIVOS com os nomes corretos

3. VERSÍCULO BÍBLICO:
   - Se desejar outro versículo, altere a variável VERSICULO_BIBLICO

4. DEPLOY:
   - Após fazer as alterações, reinicie o servidor
   - Para deploy em produção, altere também a SECRET_KEY

EXEMPLO DE URL DO WHATSAPP:
https://chat.whatsapp.com/ABC123DEF456GHI789JKL

IMPORTANTE:
- Mantenha este arquivo seguro
- Não compartilhe a SECRET_KEY
- Teste o link do WhatsApp antes de usar
"""


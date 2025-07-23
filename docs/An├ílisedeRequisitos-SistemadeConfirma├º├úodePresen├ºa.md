# Análise de Requisitos - Sistema de Confirmação de Presença

## Requisitos Funcionais

1. **Página de Confirmação**
   - Título: "Casamento Nicolas e Julia – Confirmação de Presença"
   - Versículo bíblico: Mateus 5:37
   - Pergunta: "Você vai ao casamento?"
   - Dois botões: SIM e NÃO

2. **Funcionalidade do Botão SIM**
   - Redirecionar automaticamente para grupo do WhatsApp
   - Não necessita coleta de dados adicionais

3. **Funcionalidade do Botão NÃO**
   - Abrir formulário para coleta de dados
   - Campos: Nome e lista de familiares que não irão
   - Armazenar dados para consulta posterior

## Opções Tecnológicas Analisadas

### 1. WordPress + Plugin de Formulários
**Prós:**
- Interface familiar
- Plugins disponíveis (Contact Form 7, WPForms)
- Fácil gerenciamento

**Contras:**
- Necessita hospedagem WordPress
- Pode ser complexo para uma funcionalidade simples
- Dependência de plugins

### 2. Google Forms
**Prós:**
- Gratuito
- Fácil de configurar
- Armazena dados automaticamente no Google Sheets

**Contras:**
- Limitado em customização visual
- Não permite redirecionamento condicional nativo

### 3. Aplicação Web Personalizada (Flask + HTML/CSS/JS)
**Prós:**
- Controle total sobre funcionalidades
- Design personalizado
- Lógica condicional complexa
- Pode ser hospedada gratuitamente

**Contras:**
- Requer desenvolvimento

## Recomendação

Desenvolver uma **aplicação web personalizada** usando Flask (Python) com:
- Frontend responsivo (HTML/CSS/JavaScript)
- Backend para processar formulários
- Banco de dados simples (SQLite) para armazenar respostas
- Deploy gratuito

## Estrutura da Solução

1. **Página Principal**: Design elegante com os botões
2. **Lógica JavaScript**: Redirecionamento para WhatsApp no SIM
3. **Formulário Modal**: Para coleta de dados no NÃO
4. **Backend Flask**: Processar e armazenar dados
5. **Painel Admin**: Visualizar lista de confirmações

## Vantagens da Solução Proposta

- **Gratuita**: Hospedagem gratuita disponível
- **Personalizada**: Design único para o casamento
- **Funcional**: Atende todos os requisitos
- **Escalável**: Pode adicionar funcionalidades futuras
- **Mobile-friendly**: Funciona em todos os dispositivos


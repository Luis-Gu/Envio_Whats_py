# WhatsApp Bot Automation

Este projeto é um **bot de automação para o WhatsApp**, projetado para enviar mensagens personalizadas a partir de dados extraídos de uma planilha do Google Sheets. Ele utiliza as bibliotecas **Selenium**, **pandas** e integrações personalizadas para tornar o processo de envio de mensagens eficiente e automatizado.

## Funcionalidades

- **Extração de dados do Google Sheets**: Conecta-se a uma planilha do Google Sheets para obter informações de destinatários, como nome, número e status de pagamento.
- **Login automatizado no WhatsApp Web**: Realiza login no WhatsApp Web através do Selenium.
- **Envio de mensagens personalizadas**: Cria mensagens customizadas para cada destinatário e as envia automaticamente.
- **Gerenciamento de sessão**: Faz logout após o envio de todas as mensagens para manter a segurança.

---

## Pré-requisitos

Antes de rodar o projeto, certifique-se de ter os seguintes itens instalados/configurados:

1. **Python 3.8 ou superior**
2. **Google Sheets API** configurada:
   - Baixe o arquivo `credentials.json` e mantenha-o no diretório do projeto.
3. Dependências do Python (instale usando o `requirements.txt`):
   ```bash
   pip install -r requirements.txt
   
4. **Conta Google Configurada**
    - Certifique-se de que a conta tem permissões de acesso à planilha.
 
---

## Instalação e Configuração

1. **Clone este repositório:**
   ```bash
   git clone https://github.com/seu-usuario/whatsapp-bot.git
   cd whatsapp-bot
2. **Configure os IDs e faixas da planilha:**
   - No arquivo `main.py`, substitua:
     ```python
     self.id_sheets = 'ID da sua planilha'
     self.range_sheets = 'NomeDaAba!A:Z'
3. **Crie um ambiente virtual python*:*
   - No terminal, execute os seguintes comandos:
     ```bash
     python.exe -m venv venv
     
---

## Como Usar

1. **Inicie o ambiente virtual python**
   ```bash
   .\venv\Scripts\activate
2. **Inicie o bot:** Execute o script principal para iniciar o processo de envio de mensagens:
   ```bash
   .\venv\Scripts\python.exe .\main.py
3. **Acesse o WhatsApp Web:**
   - O navegador abrirá o WhatsApp Web.
   - Escaneie o código QR para logar na sua conta.
4. **Finalização:**
   - Após o envio, bot fará logout automaticamente.

---

## Estrutura do Projeto:


   
   
   

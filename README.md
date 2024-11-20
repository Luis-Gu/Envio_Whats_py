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
```plaintext
whatsapp-bot/
├── assets/
│   ├── chromedriver.exe       # WebDriver do Selenium
│   ├── credentials.json       # Arquivo de credenciais da API do Google (autenticação)
│   └── token.json             # Arquivo de token para autenticação da API do Google
├── modules/
│   ├── __init__.py            # Indica que a pasta é um módulo Python
│   ├── setup_selenium.py      # Configuração do WebDriver Selenium
│   ├── sheets_python.py       # Integração com Google Sheets API
│   └── loading_dec.py         # Decorador para exibir mensagens de carregamento
├── venv/
├── main.py                    # Script principal que executa o bot
├── requirements.txt           # Arquivo para instalar dependências do Python
├── SELENIUM_LOGS              # Arquivo para armazenar logs do Selenium
└── README.md                  # Documentação do projeto
```

---

## Observações:
- **Segurança:** Evite enviar mensagens para destinatários que não tenham autorizado a comunicação. Certifique-se de que todos os números são válidos.
- **Taxas de envio:** O WhatsApp pode impor limites ao número de mensagens enviadas por sessão. Use com moderação.
- **Melhoria contínua:** Este projeto foi desenvolvido como base; você pode expandi-lo para incluir recursos como:
   - Monitoramento de respostas.
   - Integração com outras APIs.
   - Personalização de mensagens mais avançada.

---

## Contato

Criado por **Luis Gustavo**
| [GitHub](https://github.com/Luis-Gu) | [E-mail](mailto:luis.gucn@gmail.com)

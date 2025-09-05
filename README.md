# Simple API
API em **FastAPI** desenvolvida para a atividade de Backend Frameworks.

## Como rodar a API localmente
1. Clone o repositório:
   ```bash
   git clone https://github.com/RailsonF/simple-API.git
   cd simple-API

## crie um ambiente virtual
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

### Instale as dependências
pip install -r requirements.txt

### Rode a aplicação
uvicorn app.main:app --reload

🌐 API no Render
## A API também está disponível publicamente em:
https://simple-api-k472.onrender.com/health/

https://simple-api-k472.onrender.com/about/
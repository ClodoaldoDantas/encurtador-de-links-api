# Encurtador de Links - API

Uma API simples para encurtamento de URLs desenvolvida com Flask.

## 📋 Funcionalidades

- ✅ Criar links encurtados
- ✅ Listar todos os links criados
- ✅ Redirecionamento automático para URL original
- ✅ Documentação interativa com Swagger

## 🚀 Tecnologias

- **Flask** - Framework web Python
- **SQLAlchemy** - ORM para banco de dados
- **SQLite** - Banco de dados
- **Flasgger** - Documentação Swagger/OpenAPI
- **NanoID** - Geração de IDs únicos

## 📁 Estrutura do Projeto

```
api/
├── app/
│   ├── __init__.py      # Inicialização da aplicação
│   ├── models.py        # Modelos do banco de dados
│   ├── routes.py        # Rotas da API
│   └── database.py      # Configuração do banco
├── run.py               # Arquivo principal para executar a API
├── requirements.txt     # Dependências do projeto
├── client.http          # Arquivo para testes das rotas
```

## ⚙️ Instalação e Execução

### 1. Clone o repositório
```bash
git clone <url-do-repositorio>
cd encurtador-de-links-api/
```

### 2. Crie um ambiente virtual
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Execute a aplicação
```bash
python run.py
```

A API estará disponível em: `http://localhost:5000`

## 📖 Documentação da API

Acesse a documentação interativa Swagger em: `http://localhost:5000/apidocs/`

## 🧪 Testes

Use o arquivo `client.http` para testar as rotas da API diretamente no VS Code com a extensão REST Client.
# ✅ Task Tracker API

![Python](https://img.shields.io/badge/Python-3.14-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.133.0-009688?style=for-the-badge&logo=fastapi)
![Pytest](https://img.shields.io/badge/Pytest-9.0.2-0A9EDC?style=for-the-badge&logo=pytest)
![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)

## 📌 Descrição

Task Tracker API é uma API REST simples e objetiva para gerenciamento de tarefas. O projeto permite criar tarefas, listar todas as tarefas cadastradas, marcar uma tarefa como concluída e remover tarefas pelo identificador.

Construída com **FastAPI**, a aplicação expõe endpoints claros e documentação interativa automática via Swagger UI. O projeto também conta com testes automatizados usando **Pytest**, cobrindo tanto as rotas HTTP quanto a camada de serviço responsável pelas regras de negócio.

Atualmente, os dados são armazenados em memória, o que torna o projeto leve e fácil de executar localmente para estudos, prototipação e demonstração de uma API REST com Python.

## ✨ Funcionalidades

- Criar uma nova tarefa com título.
- Listar todas as tarefas cadastradas.
- Marcar uma tarefa como concluída.
- Impedir que uma tarefa já concluída seja concluída novamente.
- Excluir uma tarefa pelo ID.
- Verificar a saúde da API por meio do endpoint `/health`.
- Acessar documentação interativa gerada automaticamente pelo FastAPI.
- Executar testes automatizados com Pytest.

## 🛠️ Tecnologias Utilizadas

- 🐍 **Python** - Linguagem principal do projeto.
- ⚡ **FastAPI** - Framework web para construção da API.
- 🚀 **Uvicorn** - Servidor ASGI para execução da aplicação.
- ✅ **Pytest** - Framework de testes automatizados.
- 📦 **Pydantic** - Validação e serialização dos dados.
- 🔁 **GitHub Actions** - Pipeline de CI para executar testes automaticamente.

## 📋 Pré-requisitos

Antes de começar, você precisa ter instalado:

- **Python 3.14** ou superior recomendado conforme o workflow de CI do projeto.
- **pip** para instalação das dependências.
- **Git** para clonar o repositório.

> Observação: em ambientes locais, versões recentes do Python 3 também podem funcionar, mas o projeto está configurado no CI para Python 3.14.

## 🚀 Como Executar o Projeto

### 1. Clone o repositório

```bash
git clone https://github.com/gustavolimacode/Task-Tracker-API.git
cd Task-Tracker-API
```

### 2. Crie e ative um ambiente virtual

No Linux/macOS:

```bash
python -m venv .venv
source .venv/bin/activate
```

No Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Execute a API

```bash
uvicorn app.main:app --reload
```

A aplicação ficará disponível em:

```text
http://localhost:8000
```

### 5. Acesse a documentação interativa

```text
http://localhost:8000/docs
```

Também é possível acessar a documentação ReDoc em:

```text
http://localhost:8000/redoc
```

## 🔐 Variáveis de Ambiente

O projeto **não possui variáveis de ambiente obrigatórias** no estado atual.

A API utiliza uma lista em memória para armazenar as tarefas, portanto não é necessário configurar banco de dados, chaves de API ou arquivo `.env` para executar a aplicação localmente.

Caso o projeto evolua para usar banco de dados ou autenticação, um exemplo de `.env` poderia seguir este formato:

```env
DATABASE_URL=SUA_URL_DO_BANCO_AQUI
SECRET_KEY=SUA_CHAVE_SECRETA_AQUI
```

## 📚 Endpoints da API

| Método | Rota | Descrição |
|---|---|---|
| `GET` | `/health` | Verifica se a API está respondendo. |
| `GET` | `/tasks/` | Lista todas as tarefas. |
| `POST` | `/tasks/` | Cria uma nova tarefa. |
| `PATCH` | `/tasks/{task_id}/done` | Marca uma tarefa como concluída. |
| `DELETE` | `/tasks/{task_id}` | Remove uma tarefa pelo ID. |

### Exemplo de criação de tarefa

```bash
curl -X POST "http://localhost:8000/tasks/" \
  -H "Content-Type: application/json" \
  -d '{"title": "Estudar FastAPI"}'
```

Resposta esperada:

```json
{
  "id": 1,
  "title": "Estudar FastAPI",
  "done": false
}
```

## 🧪 Como Rodar os Testes

Execute:

```bash
pytest
```

Os testes cobrem:

- Criação de tarefas.
- Listagem de tarefas.
- Remoção de tarefas.
- Marcação de tarefa como concluída.
- Tratamento de erro para tarefa inexistente.
- Tratamento de erro ao tentar concluir uma tarefa já concluída.

## 📁 Estrutura de Pastas

```text
Task-Tracker-API/
├── .github/
│   └── workflows/
│       └── ci.yml
├── app/
│   ├── routes/
│   │   └── tasks.py
│   ├── schemas/
│   │   └── task.py
│   ├── services/
│   │   └── task_service.py
│   ├── __init__.py
│   ├── database.py
│   └── main.py
├── tests/
│   ├── __init__.py
│   ├── test_task_routes.py
│   └── test_task_service.py
├── .gitignore
├── README.md
└── requirements.txt
```

## 🤝 Como Contribuir

Contribuições são bem-vindas!

Para contribuir:

1. Faça um fork do projeto.
2. Crie uma branch para sua feature:

```bash
git checkout -b minha-feature
```

3. Faça suas alterações e adicione testes quando necessário.
4. Execute os testes:

```bash
pytest
```

5. Envie suas alterações:

```bash
git commit -m "feat: adiciona nova funcionalidade"
git push origin minha-feature
```

6. Abra um Pull Request descrevendo suas mudanças.

## 📄 Licença

Este projeto está licenciado sob a licença **MIT**.

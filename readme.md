# 🐍 Python Profissional — Do Zero ao Projeto Corporativo

## 🧭 Visão Geral
Este guia prático e progressivo conduz você desde o domínio dos fundamentos até o desenvolvimento de um projeto com estrutura profissional, como se fosse feito dentro de uma empresa.

Ao final, você terá um projeto completo, modular, com testes, logs, API e deploy em Docker — além de um portfólio técnico forte.

---

## 🔹 Etapa 1 — Fundamentos sólidos e boas práticas
**Objetivo:** dominar os blocos de construção e aprender a escrever código limpo.

### Conteúdo:
- Estruturas de dados (listas, tuplas, dicionários, sets)
- Funções puras e funções com efeitos colaterais
- `*args`, `**kwargs`, `lambda`, `map`, `filter`, `zip`
- Programação orientada a objetos:
  - classes, herança, polimorfismo, encapsulamento
- `typing` e docstrings
- Tratamento de erros (`try`, `except`, `raise`)
- Boas práticas: PEP8, PEP20, e princípios *Clean Code*

### 🧩 Mini-projeto:
Criar uma **biblioteca de utilidades** com funções reutilizáveis bem documentadas.

---

## 🔹 Etapa 2 — Estrutura de projeto e modularização
**Objetivo:** aprender a organizar projetos reais como em empresas.

### Conteúdo:
- Módulos e pacotes (`__init__.py`)
- Estrutura de diretórios (`src/`, `tests/`, `data/`)
- Importações relativas e absolutas
- Logs com o módulo `logging`
- Configurações com `.env` e `dotenv`

### 🧩 Mini-projeto:
Criar um **gerenciador de tarefas em terminal (CLI)**:
- `core/` para lógica de negócio  
- `storage/` para persistência em arquivo JSON  
- `cli.py` como interface principal  

---

## 🔹 Etapa 3 — Testes, qualidade e automação
**Objetivo:** garantir que o código é confiável e fácil de manter.

### Conteúdo:
- Testes com `pytest`
- Mocks e fixtures
- Cobertura de testes
- Linter (`flake8`, `pylint`)
- Formatter (`black`, `isort`)
- Type checking com `mypy`

### 🧩 Mini-projeto:
Adicionar **testes automáticos** ao gerenciador de tarefas da etapa 2.

---

## 🔹 Etapa 4 — Aplicação Web / API
**Objetivo:** aprender a expor serviços e interagir via HTTP.

### Conteúdo:
- Introdução ao **Flask** ou **FastAPI**
- Estrutura MVC (Model, View, Controller)
- Rotas, parâmetros e respostas JSON
- Camada de serviços e repositórios
- Testes de integração

### 🧩 Mini-projeto:
Transformar o gerenciador de tarefas em uma **API REST** com FastAPI.

---

## 🔹 Etapa 5 — Banco de dados e persistência
**Objetivo:** introduzir o armazenamento persistente e ORM.

### Conteúdo:
- SQLite / PostgreSQL
- SQL básico
- ORM com SQLAlchemy ou Tortoise ORM
- Padrão Repository
- Migrations

### 🧩 Mini-projeto:
Conectar a API a um banco de dados e criar endpoints de CRUD completos.

---

## 🔹 Etapa 6 — Deploy, logs e boas práticas corporativas
**Objetivo:** preparar o projeto para rodar como em um ambiente real de produção.

### Conteúdo:
- `Dockerfile` e `docker-compose`
- Logs e configuração de níveis (`INFO`, `ERROR`)
- Variáveis de ambiente seguras
- Documentação com `README` e docstrings
- Introdução a CI/CD (GitHub Actions)

### 🧩 Mini-projeto final:
Deploy do sistema completo usando **Docker + FastAPI + PostgreSQL**.

---

## 🏁 Resultado Final
Você terá:
- Um projeto real com **arquitetura profissional**
- Entendimento de **boas práticas corporativas**
- Habilidade de trabalhar em **qualquer equipe Python**
- Portfólio técnico para apresentar em **entrevistas de desenvolvedor**

---

## 💡 Dica de progresso
Avance uma etapa por vez.  
A cada etapa, implemente o mini-projeto proposto e peça uma revisão de código.  
Essa prática é o que mais aproxima da rotina de um desenvolvedor Python em ambiente profissional.

# Distributed Test Automation Platform (DTAP)

Distributed Test Automation Platform (DTAP) is a Python-based test automation system that executes YAML-defined test scenarios through an asynchronous execution engine.

The project demonstrates modern backend development practices including Clean Architecture, FastAPI, AsyncIO, SQLAlchemy, Docker, and automated testing.

---

## Features

✅ YAML-based test scenarios

✅ Asynchronous test execution with AsyncIO

✅ Worker Pool architecture

✅ Command Pattern implementation

✅ Factory Pattern implementation

✅ Structured logging system

✅ FastAPI REST API

✅ Swagger/OpenAPI documentation

✅ SQLAlchemy ORM

✅ SQLite database support

✅ Docker containerization

✅ Unit testing with Pytest

---

## Architecture

```text
Client
  │
  ▼
FastAPI
  │
  ▼
YamlParser
  │
  ▼
Domain Models
  │
  ▼
TestExecutor
  │
  ▼
CommandFactory
  │
  ▼
Commands
  │
  ├── LogCommand
  ├── WaitCommand
  ├── CompareCommand
  └── FailCommand
  │
  ▼
WorkerPool
  │
  ▼
Database

Technologies

Python 3.13
FastAPI
Uvicorn
SQLAlchemy
SQLite
PyYAML
AsyncIO
Pytest
Docker


Project Structure

src/
├── api/
├── application/
├── commands/
├── database/
├── domain/
├── infrastructure/
└── workers/
 
tests/
docs/

Running Locally

Install dependencies:


pip install -r requirements.txt

Run API:


uvicorn src.api.app:app --reload

Open Swagger:

http://127.0.0.1:8000/docs
Running with Docker

Build container:


docker compose build

Run application:


docker compose up

Open Swagger UI:

Plain Text
http://localhost:8000/docs
 
Execute Test Scenario

Request:

HTTP
POST /run

Example body:

{
"file": "docs/examples/sample-test.yaml"
}

Response:

{
"success": true,
"test_name": "Login Test"
}


Run tests:


python -m pytest tests -v

Example output:

=========================
3 passed
=========================

Future Improvements
PostgreSQL support
GitHub Actions CI/CD
JWT Authentication
WebSocket execution monitoring
Distributed execution nodes

Author:
Vladyslav Polieshchuk

Software Engineering Student
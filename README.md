# Distributed Test Automation Platform

Distributed Test Automation Platform is a learning project inspired by real-world QA infrastructure systems.

The platform allows creating, executing and monitoring automated test scenarios through an asynchronous execution engine.

## Goals

- Learn software architecture
- Practice asyncio
- Apply design patterns
- Work with PostgreSQL
- Use Docker
- Write automated tests with Pytest
- Build CI/CD pipelines with GitHub Actions

---

## Planned Features

- YAML-based test scenarios
- Async test execution
- Test history tracking
- Execution logs
- PostgreSQL integration
- REST API
- Docker deployment
- GitHub Actions CI

---

## Architecture

```text
Client
 |
 v
FastAPI
 |
 v
Application Layer
 |
 v
Async Workers
 |
 v
PostgreSQL
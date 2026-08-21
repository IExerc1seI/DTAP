# Architecture Overview

## Project Goal

TestForge is an asynchronous test execution platform designed to manage, execute, and monitor automated test scenarios.

The system accepts test definitions, converts them into executable commands, schedules execution, stores results, and provides visibility through logs and execution history.

---

# High-Level Architecture

┌─────────────┐
│   Client    │
└──────┬──────┘
       │ HTTP
       ▼
┌─────────────┐
│   FastAPI   │
└──────┬──────┘
       │
       ▼
┌────────────────────┐
│ Application Layer  │
└──────┬─────────────┘
       │
       ├─────────────► PostgreSQL
       │
       ▼
┌────────────────────┐
│ Task Scheduler     │
└──────┬─────────────┘
       │
       ▼
┌────────────────────┐
│ Async Worker Pool  │
└──────┬─────────────┘
       │
       ▼
┌────────────────────┐
│ Command Executor   │
└──────┬─────────────┘
       │
       ▼
┌────────────────────┐
│ Test Commands      │
└────────────────────┘

---

# Architectural Principles

The project follows several principles:

- Separation of Concerns
- Dependency Inversion
- Single Responsibility Principle
- Domain-Driven Design concepts
- Clean Architecture
- Async-first design

Business logic must remain independent from FastAPI, PostgreSQL, or any external framework.

---

# Layers

## 1. Presentation Layer

### Responsibilities

- HTTP communication
- Request validation
- Response serialization

### Technologies

- FastAPI
- Pydantic

### Example Responsibilities

- Create test
- Start execution
- Query execution status
- Retrieve logs

---

## 2. Application Layer

### Responsibilities

Coordinates all business operations.

This layer contains use-cases:

- CreateTest
- RunTest
- StopTest
- GetRunStatus
- GetExecutionLogs

### Rules

Application layer may depend on:

- Domain Layer

Application layer must not depend on:

- FastAPI
- SQLAlchemy models
- PostgreSQL

---

## 3. Domain Layer

The most important layer.

Contains pure business logic.

### Entities

#### Test

Represents a test scenario.

Attributes:

- id
- name
- created_at
- steps

#### TestStep

Represents a single scenario action.

Attributes:

- type
- parameters

#### TestRun

Represents a test execution.

Attributes:

- run_id
- started_at
- finished_at
- status

#### ExecutionResult

Stores execution outcome.

Attributes:

- success
- logs
- duration

---

# Command Execution Model

Each test step is transformed into a command object.

Example:

YAML:

```yaml
steps:
  - click
  - wait
  - assert
# Domain Model

## Overview

Distributed Test Automation Platform is a system for managing, executing and monitoring automated test scenarios.

The core domain consists of the following entities:

- Test
- TestStep
- TestRun
- TestResult

---

# Test

Represents a reusable test scenario.

Example:

Login Test
Device Connection Test
API Health Check

## Attributes

- id
- name
- description
- created_at
- steps

## Relationships

One Test contains many TestSteps.

One Test can have many TestRuns.

---

# TestStep

Represents a single action within a test.

Examples:

- wait
- send_command
- log
- check_value

## Attributes

- id
- action
- parameters
- order

## Example

wait:
    seconds: 2

send_command:
    command: login

---

# TestRun

Represents a single execution of a Test.

A Test can be executed multiple times.

## Attributes

- id
- test_id
- status
- started_at
- finished_at

## Possible statuses

- PENDING
- RUNNING
- PASSED
- FAILED
- CANCELLED

---

# TestResult

Represents execution results.

## Attributes

- id
- run_id
- success
- duration
- logs

## Example

success: true

duration: 3.42

logs:
    Connecting...
    Command sent.
    Test finished successfully.
#!/usr/bin/env bash

exec uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

#!/bin/bash
celery -A app worker --loglevel=info --concurrency=1 &
CELERY_PID=$!

python3 send_task.py &
SEND_TASK_PID=$!

wait $CELERY_PID $SEND_TASK_PID
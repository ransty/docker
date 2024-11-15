#!/bin/bash
celery -A app worker --loglevel=info --pool=prefork --concurrency=12 --uid 65 &
CELERY_PID=$!

python3 send_task.py &
SEND_TASK_PID=$!

wait $CELERY_PID $SEND_TASK_PID

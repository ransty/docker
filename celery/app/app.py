from celery import Celery

app = Celery('simple_app', broker='pyamqp://guest@rabbitmq//', backend='rpc://')

app.conf.update(
        task_time_limit=3600,
        task_soft_time_limit=3500,
        result_expires=7200,
)

@app.task
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n -1) + fibonacci(n - 2)

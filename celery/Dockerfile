FROM python:3.8-slim-bookworm

RUN apt-get update && python3 -m pip install celery

COPY app/ /code/
COPY entrypoint.sh /usr/local/bin/entrypoint.sh

WORKDIR /code/

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
CMD ["-A", "app", "worker", "--loglevel=info"]

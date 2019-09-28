FROM python:3.6-alpine

RUN adduser -D kc-news-service

WORKDIR /home/src

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY app app
COPY news-service.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP app

RUN chown -R kc-news-service:kc-news-service ./
USER kc-news-service

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
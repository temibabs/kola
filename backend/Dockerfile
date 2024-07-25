FROM python:3.11-slim-bullseye

WORKDIR /kola

COPY backend/src /kola/
COPY backend/requirements.txt /kola/requirements.txt

RUN apt update
RUN pip install -r /kola/requirements.txt

ENV PYTHONPATH "/app"

EXPOSE 5000
ENTRYPOINT ["uvicorn", "kola.app:app", "--host=0.0.0.0", "--port=5000", "--workers=5"]

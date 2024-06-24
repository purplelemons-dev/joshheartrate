FROM python:3.12.2-slim-bookworm

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY src .

CMD ["python", "server.py"]

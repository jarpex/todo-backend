FROM python:3.13.3-alpine3.21

RUN apk update && \
    apk add --no-cache \
    bash \
    gcc \
    libpq-dev \
    postgresql-dev \
    musl-dev \
    build-base \
    python3-dev \
    libffi-dev \
    openssl-dev

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN chmod +x start.sh

ENV PYTHONPATH=/app

CMD ["./start.sh"]
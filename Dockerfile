FROM python:3.13.3-alpine3.21

RUN apk update && \
    apk add --no-cache \
    bash \
    gcc \
    libpq-dev \
    postgresql-dev \
    musl-dev

WORKDIR /app

COPY . .
RUN chmod +x start.sh

ENV PYTHONPATH=/app

CMD ["./start.sh"]
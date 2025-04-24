FROM python:3.13.3-alpine3.21

RUN apk update && \
    apk add --no-cache \
    bash \
    gcc \
    libpq-dev 

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY start.sh .
RUN chmod +x start.sh
CMD ["./start.sh"]
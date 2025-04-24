FROM python:3.13.3-alpine3.21

# RUN apt update || true && \
#     apt install -y gnupg && \
#     apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 0xA1BC0F19 && \
#     apt install -y gcc libpq-dev && \
#     rm -rf /var/lib/apt/lists/*

RUN apk update && \
    apk add --no-cache \
    gcc \
    libpq-dev 

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["./start.sh"]
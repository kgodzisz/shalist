FROM python:3-alpine
COPY . /app
WORKDIR /app
RUN apk add --no-cache python3-dev
ENTRYPOINT ["python", "check.py"]
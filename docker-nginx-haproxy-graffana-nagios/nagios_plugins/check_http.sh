#!/bin/bash

# Параметры
HOST=$1
PORT=$2

# Проверка наличия параметров
if [ -z "$HOST" ] || [ -z "$PORT" ]; then
  echo "Usage: $0 <host> <port>"
  exit 3
fi

# Выполнение HTTP-запроса
HTTP_RESPONSE=$(curl -s -o /dev/null -w "%{http_code}" http://$HOST:$PORT)

# Проверка кода ответа
if [ "$HTTP_RESPONSE" -eq 200 ]; then
  echo "HTTP OK - $HOST:$PORT responded with status $HTTP_RESPONSE"
  exit 0
else
  echo "HTTP CRITICAL - $HOST:$PORT responded with status $HTTP_RESPONSE"
  exit 2
fi


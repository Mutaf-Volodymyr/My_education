#!/bin/bash

THRESHOLD=80
USAGE=$(df / | grep -v Filesystem | awk '{print $5}' | sed 's/%//g')

if [ "$USAGE" -gt "$THRESHOLD" ]; then
  # в этом блоке необходимо прописать отправку
  # сообщения E-mail или SMS нужным людям
fi
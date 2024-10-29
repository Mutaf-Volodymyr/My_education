#!/bin/bash

address="3.73.44.38"
fail_count=0
while true
do
  ping_result=$(ping -c 1 "$address" 2>/dev/null)

  if [[ $? -ne 0 ]]; then
    ((fail_count++))
    if [[ $fail_count -ge 10 ]]; then
        # в этом блоке необходимо прописать отправку
        # сообщения E-mail или SMS нужным людям
    fi
  else
    fail_count=0
  fi
done
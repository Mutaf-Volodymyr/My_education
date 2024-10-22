#!/bin/bash

set -e

read -p "Enter address to ping: " address

fail_count=0

while true
do
  ping_result=$(ping -c 1 "$address" 2>/dev/null)

  if [[ $? -ne 0 ]]; then
    ((fail_count++))
    echo "Ping failed ($fail_count/3)"

    if [[ $fail_count -ge 3 ]]; then
      echo "Ping failed 3 times in a row!"
    fi
  else
    fail_count=0
    avg_time=$(echo "$ping_result" | tail -n 1 | awk -F '/' '{print $5}')

    if [[ $(echo "$avg_time > 100" | bc -l) -eq 1 ]]; then
      echo "Ping time too high: $avg_time ms"
    else
      echo "Ping time: $avg_time ms"
    fi
  fi

  sleep 1
done


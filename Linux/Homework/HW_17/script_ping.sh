#!/bin/bash

# Включаем режим завершения при ошибке
set -e

# Чтение адреса от пользователя
read -p "Enter address to ping: " address

# Инициализация счетчика неудачных попыток
fail_count=0

# Бесконечный цикл
while true
do
  # Пингуем адрес 1 раз и сохраняем результат
  ping_result=$(ping -c 1 "$address" 2>/dev/null)

  # Проверка на успех пинга
  if [[ $? -ne 0 ]]; then
    # Если пинг не прошел, увеличиваем счетчик неудач
    ((fail_count++))
    echo "Ping failed ($fail_count/3)"

    # Если три неудачных пинга подряд, выводим сообщение
    if [[ $fail_count -ge 3 ]]; then
      echo "Ping failed 3 times in a row!"
    fi
  else
    # Сбрасываем счетчик неудач, так как пинг успешен
    fail_count=0

    # Извлекаем среднее время пинга
    avg_time=$(echo "$ping_result" | tail -n 1 | awk -F '/' '{print $5}')

    # Проверяем, превышает ли время отклика 100 мс
    if [[ $(echo "$avg_time > 100" | bc -l) -eq 1 ]]; then
      echo "Ping time too high: $avg_time ms"
    else
      echo "Ping time: $avg_time ms"
    fi
  fi

  # Пауза на 1 секунду перед следующей попыткой
  sleep 1
done


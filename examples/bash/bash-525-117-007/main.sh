#!/bin/bash

attempt=0

until [ "$attempt" -ge 3 ]; do
    attempt=$((attempt + 1))
    echo "Попытка $attempt"
    
    # Имитация случайного успеха
    if [ $((RANDOM % 3)) -eq 0 ]; then
        echo "Успех достигнут!"
        break
    fi
done

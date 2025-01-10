import asyncio
import aiohttp

# Асинхронная функция для получения данных с API
async def fetch_data_from_api(url: str):
    print(f"Запрос к API: {url} начат...")
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()  # Получаем JSON-ответ
            print(f"Запрос к API: {url} завершен.")
            return data

# Основная асинхронная функция
async def main():
    # URL для асинхронных запросов (используем публичный API)
    url1 = 'https://jsonplaceholder.typicode.com/todos/1'  # Пример URL для запроса
    url2 = 'https://jsonplaceholder.typicode.com/todos/2'

    # Запускаем несколько запросов параллельно
    task1 = fetch_data_from_api(url1)
    task2 = fetch_data_from_api(url2)

    # Ожидаем завершения всех запросов и собираем их результаты
    result1, result2 = await asyncio.gather(task1, task2)

    # Выводим полученные результаты
    print("Результат 1:", result1)
    print("Результат 2:", result2)

# Запуск программы
asyncio.run(main())
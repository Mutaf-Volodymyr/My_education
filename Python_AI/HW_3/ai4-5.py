
import sys
from db_movi import MongoDBMFinder
import faiss
from google import genai
import numpy as np
import os
import dotenv
from pathlib import Path

dotenv.load_dotenv(Path('../.env'))
client = genai.Client(api_key=os.environ.get('GEMINI'))


def get_embedding(text):
    response = client.models.embed_content(
        model="text-embedding-004",
        contents=text)

    return np.array(response.embeddings[0].values)  # Возвращаем embedding как numpy array

finer_obj = MongoDBMFinder(100)
finer_obj.find_all()
texts_to_index = finer_obj.find_all()

embeddings_list = [get_embedding(text) for text in texts_to_index]
embeddings_array = np.array(embeddings_list)  # Преобразуем в numpy array для FAISS

dimension = embeddings_array.shape[1] # (6, 256)
index = faiss.IndexHNSWFlat(dimension, 32)
index.add(embeddings_array)  # Добавляем embeddings в индекс
print(sys.getsizeof(index))

# 4. Функция для выполнения семантического поиска
def semantic_search(query, index, texts, k=2):
    query_embedding = get_embedding(query).reshape(1, -1)  # Получаем embedding для запроса и меняем размерность
    D, I = index.search(query_embedding, k)  # Ищем k ближайших соседа
    results = [texts[i] for i in I[0]]  # Получаем тексты по индексам
    return results


# 5. Пример использования семантического поиска
search_query = "Gun"
search_results = semantic_search(search_query, index, texts_to_index, k=3)

print("\n--- Результаты семантического поиска ---")
print(f"Запрос: '{search_query}'")
print("Найденные соответствия:")
for result in search_results:
    print(f"- {result}")

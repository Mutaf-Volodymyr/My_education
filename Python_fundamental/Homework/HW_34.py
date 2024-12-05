# Напишите функцию extract_emails(text), которая извлекает все адреса
# электронной почты из заданного текста и возвращает их в виде списка.
#

from re import findall
def extract_emails(text:str):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
    return findall(pattern, text)


text = "Contact us at info@example.com or support.ich@example.com for assistance."
emails = extract_emails(text)
print(emails)  # Вывод: ['info@example.com', 'support@example.com']




# Напишите функцию highlight_keywords(text, keywords), которая выделяет все вхождения заданных ключевых
# слов в тексте, окружая их символами *. Функция должна быть регистронезависимой при поиске ключевых слов.

from re import sub, IGNORECASE
def highlight_keywords(text, keywords):
    for keyword in keywords:
        keyword = rf"\b({keyword})\b"
        text = sub(keyword, r'*\1*', text, flags=IGNORECASE)
    return text

text = "This is a sample text. We need to highlight Python and programming."
keywords = ["python", "programming"]
highlighted_text = highlight_keywords(text, keywords)
print(highlighted_text)

# Вывод: "This is a sample text. We need to highlight *Python* and *programming*."


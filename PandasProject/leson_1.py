import pandas as pd

# Series: одномерный массив данных с индексами.
# s = pd.Series([10, 20, 30, 40, 50])
# print(s)

# DataFrame: двумерная таблица данных, которая состоит из строк и столбцов.
# data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Score': [85, 90, 95]}
# df = pd.DataFrame(data)
# print(df)

# Увеличь каждую оценку на 5.
# df['Score'] +=5
# print(df)

# Добавь новый столбец Age и заполни его значениями: [20, 22, 21].
# df['Age'] =  [20, 22, 21]
# print(df)

# Выбери только имена студентов.
# print(df['Name'])

# print(df.loc[1])  # Выбирает строку с индексом 1 (по метке)
# print(df.loc[:, 'Name'])  # Выбирает столбец 'Name' для всех строк
# print(df.loc[1, 'Name'])  # Выбирает значение в строке 1 и столбце 'Name'

df = pd.read_json('updated_people.json')
# print(df.isna()) # для проверки пропущенных значений.

# df_cleaned = df.dropna() # Удаление строк с пропущенными значениями:
# df['phone'] = df['phone'].fillna('Unknown') # Замена пропущенных значений:
# df['age'] = df['age'].fillna(df['age'].mean()) # Заполнение пропусков средними значениями

# print(df[df['age'] == 30])

# Можно комбинировать несколько условий с
# использованием & (и) и | (или), при этом каждое условие нужно оборачивать в скобки:
# print(df[(df['age'] > 30) & (df['children'] == 'yes')])


# print(df.groupby('country')['age'].mean())  # Средний возраст по странам

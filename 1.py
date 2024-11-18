import json
def calculate_sum_of_products(file_path):
    # Чтение данных из JSON-файла
    with open(file_path, 'r') as file:
        data = json.load(file)

    # Вычисление суммы произведений значений "score" и "weight"
    result = sum(entry['score'] * entry['weight'] for entry in data)

    # Округление результата до 3 знаков после запятой
    return round(result, 3)


# Путь к файлу input.json
file_path = 'input.json'

# Вызов функции и вывод результата
print(calculate_sum_of_products(file_path))

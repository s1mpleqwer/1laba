import csv
import json


def csv_to_json(csv_file_path, delimiter=',', line_terminator='\n'):
    # Чтение данных из CSV файла
    with open(csv_file_path, mode='r', newline='') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=delimiter, lineterminator=line_terminator)

        # Фильтрация пустых строк
        data = [row for row in reader if any(row.values())]

    # Преобразование данных в формат JSON
    json_data = json.dumps(data, indent=4, ensure_ascii=False)
    return json_data


# Путь к CSV файлу
csv_file_path = 'input.csv'

# Вызов функции и вывод результата без пустой строки в конце
json_result = csv_to_json(csv_file_path)
print(json_result, end='')

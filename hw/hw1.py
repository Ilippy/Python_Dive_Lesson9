# Создайте функцию generate_csv_file(file_name, rows),
# которая будет генерировать по три случайны числа в каждой строке,
# от 100-1000 строк, и записывать их в CSV-файл. Функция принимает два аргумента:
#
# file_name (строка) - имя файла, в который будут записаны данные.
# rows(целое число) - количество строк (записей) данных, которые нужно сгенерировать.
#
# Создайте функцию find_roots(a, b, c),
# которая будет находить корни квадратного уравнения вида ax^2 + bx + c = 0.
# Функция принимает три аргумента:
#
# a, b, c (целые числа) - коэффициенты квадратного уравнения.
#
# Функция возвращает:
# None, если уравнение не имеет корней (дискриминант отрицателен).
# Одно число, если уравнение имеет один корень (дискриминант равен нулю).
# Два числа (корни), если уравнение имеет два корня (дискриминант положителен).
#
# Создайте декоратор save_to_json(func), который будет оборачивать функцию find_roots.
# Декоратор выполняет следующие действия:
# Читает данные из CSV-файла, переданного в аргументе функции, исходя из аргумента args[0].
# Для каждой строки данных вычисляет корни квадратного уравнения с помощью функции find_roots.
# Сохраняет результаты в формате JSON в файл results.json.
# Каждая запись JSON содержит параметры a, b, c и результаты вычислений.
# Таким образом, после выполнения функций generate_csv_file и find_roots
# в файле results.json будет сохранена информация о параметрах
# и результатах вычислений для каждой строки данных из CSV-файла.
#
# Пример
#
# На входе:
#
#
# generate_csv_file("input_data.csv", 101)
# find_roots("input_data.csv")
#
# with open("results.json", 'r') as f:
#     data = json.load(f)
#
# if 100<=len(data)<=1000:
#     print(True)
# else:
#     print(f"Количество строк в файле не находится в диапазоне от 100 до 1000.")
#
# print(len(data)==101)
# На выходе:
#
#
# True
# True
# Формат JSON файла определён следующим образом:
#
# [
#     {"parameters": [a, b, c], "result": result},
#     {"parameters": [a, b, c], "result": result},
#     ...
#
from random import randint
from functools import wraps
import csv
import json


def generate_csv_file(file_name: str, rows: int):
    min_random_number = 1
    max_random_number = 100
    with open(file_name, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        for _ in range(rows):
            writer.writerow([randint(min_random_number, max_random_number) for _ in range(3)])


def read_csv_file(file_name: str) -> list[list[int, int, int]]:
    with open(file_name, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        result = []
        for a, b, c in reader:
            result.append([int(x) for x in (a, b, c)])
        return result


def save_list_to_json(lst: list[dict], file_name='results.json'):
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(lst, f, indent=2, ensure_ascii=False)


def save_to_json(func):
    @wraps(func)
    def inner(*args, **kwargs):
        if len(args) == 3 and all(type(x) == int for x in args):
            return func(*args, **kwargs)
        csv_list = read_csv_file(args[0])
        results_list = []
        for a, b, c in csv_list:
            result = func(a, b, c)
            results_list.append({"parameters": [a, b, c], "result": result})
        for line in results_list:
            if line["result"]:
                print(line)
        save_list_to_json(results_list)

    return inner


@save_to_json
def find_roots(a: int, b: int, c: int):
    d = b ** 2 - 4 * a * c
    if d < 0:
        return None
    elif d == 0:
        return -b / (2 * a)
    else:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        return x1, x2


if __name__ == '__main__':
    csv_file_name = "input_data.csv"
    generate_csv_file(csv_file_name, 101)
    find_roots("input_data.csv")
    with open("results.json", 'r') as f:
        data = json.load(f)

    if 100 <= len(data) <= 1000:
        print(True)
    else:
        print(f"Количество строк в файле не находится в диапазоне от 100 до 1000.")

    print(len(data) == 101)

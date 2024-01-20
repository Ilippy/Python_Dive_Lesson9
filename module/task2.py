# Дорабатываем задачу 1.
# Превратите внешнюю функцию в декоратор.
# Он должен проверять входят ли переданные в функцию-угадайку числа в диапазоны [1, 100] и [1, 10].
# Если не входят, вызывать функцию со случайными числами из диапазонов.
from random import randint


def decorator(func):
    def inner(guess, amount_of_tries, *args, **kwargs):
        if guess < 1 or guess > 100:
            guess = randint(1, 100)
        if amount_of_tries < 1 or amount_of_tries > 10:
            amount_of_tries = randint(1, 10)
        return func(guess, amount_of_tries)

    return inner


@decorator
def task2(num1, num2):
    for i in range(num2):
        temp = int(input("Введите ваш вариант: "))
        if temp == num1:
            print("Вы победили. Попытка #", i + 1)

    return f"Загаданое число = {num1}"


if __name__ == '__main__':
    guess_number = int(input("Загадайте число от 1 до 100"))
    amount_of_tries = int(input("Введите количество попыток от 1 до 10"))
    print(task2(guess_number, amount_of_tries))

# Создайте функцию-замыкание, которая запрашивает два целых числа:
# ○ от 1 до 100 для загадывания,
# ○ от 1 до 10 для количества попыток
# Функция возвращает функцию, которая через консоль просит угадать загаданное число за указанное число попыток.
def task1(guess, amount_of_tries):
    def inner() -> bool:
        print(f"У вас {amount_of_tries} попыток, чтобы отгадать число в пределах (1, 100)")
        for i in range(1, amount_of_tries + 1):
            print(f"Попытка №{i}")
            guess_number = int(input("Введите число: "))
            if guess_number == guess:
                return True
            print("Больше" if guess > guess_number else "Меньше")
        return False

    return inner

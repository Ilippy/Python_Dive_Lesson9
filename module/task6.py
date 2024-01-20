# Доработайте прошлую задачу добавив декоратор wraps в каждый из декораторов.
from functools import wraps


def title(func):
    @wraps(func)
    def inner(*args, **kwargs):
        print("<title>")
        func(*args, **kwargs)
        print("</title>")

    return inner


def header(func):
    @wraps(func)
    def inner(*args, **kwargs):
        print("<h1>")
        func(*args, **kwargs)
        print("</h1>")

    return inner


@title
@header
def print_(string):
    print(string)


def main():
    print_("sss")


if __name__ == '__main__':
    main()

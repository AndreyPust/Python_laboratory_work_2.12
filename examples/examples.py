#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def hello_world():
    """
    Функция выводит надпись "Hello world!", пример простой функции.
    """
    print('Hello world!')


class Hello:
    """
    Определение нового класса по примеру.
    """
    pass


def wrapper_function():
    """
    Функция содержит внутри себя другую функцию и вызывает ее,
    которая выводит надпись 'Hello world!'.
    Пример функции, которая содержит в себе другую.
    """
    def hello_world_two():
        print('Hello world 2!')
    hello_world_two()


def higher_order(func):
    """
    Функция выводит информацию о функции, которую ей передали в качестве аргумента.
    """
    print('Получена функция {} в качестве аргумента'.format(func))
    func()
    return func


def decorator_function(func):
    """
    Пример функции декоратора, которая изменяет поведение функции при передаче этой функции
    в качестве аргумента другой функции.
    """
    def wrapper():
        print('Функция-обёртка!')
        print('Оборачиваемая функция: {}'.format(func))
        print('Выполняем обёрнутую функцию...')
        func()
        print('Выходим из обёртки')
    return wrapper


@decorator_function
def hello_world_thee():
    """
    Функция выводит надпись 'Hello world!'.
    Пример использования декоратора decorator_function.
    """
    print('Hello world 3!')


def benchmark(func):
    """
    Пример декоратора, который получает время выполнения функции.
    """
    import time

    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print('[*] Время выполнения: {} секунд.'.format(end-start))
    return wrapper


@benchmark
def hello_world_four():
    """
    Функция выводит надпись 'Hello world!'.
    Пример использования декоратора benchmark для измерения времени.
    """
    print('Hello world 4!')


def benchmark_mod(func):
    """
    Модифицированный пример декоратора, который получает время выполнения функции.
    """
    import time

    def wrapper_two(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        print('[*] Время выполнения: {} секунд.'.format(end-start))
        return return_value
    return wrapper_two


@benchmark_mod
def hello_world_five():
    """
    Функция выводит надпись 'Hello world!'.
    Пример использования декоратора benchmark_mod.
    """
    print('Hello world 5!')


if __name__ == "__main__":
    print(type(hello_world))   # hello_world принадлежит типу <class 'function'>

    print(type(Hello))         # Класс Hello принадлежит классу type

    print(type(10))            # Пример класса 'int'

    hello = hello_world        # Пример хранения функции в переменной
    hello()

    wrapper_function()         # Пример функции, которая содержит в себе другую функцию

    print(higher_order(hello_world))  # Пример передачи функции в качестве аргумента

    hello_world_thee()         # Пример использования функции декоратора

    hello_world_four()         # Пример использования декоратора benchmark

    print(hello_world_five)    # Пример использования декоратора benchmark_mod

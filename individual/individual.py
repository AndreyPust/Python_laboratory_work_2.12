#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def tag_decorator(func):
    """
    Функция декоратор, которая обращает строку, которую возвращает функция string_lover
    в соответствующий тег.
    """

    def wrapper(text):
        result = func(text)
        print(f"<{tag_html}>{result}</{tag_html}>")
    return wrapper


@tag_decorator
def string_lover(text):
    """
    Функция переводит переданную ей строку в нижний регистр.
    """
    return str(text).lower()


if __name__ == "__main__":

    # Необходимо объявить функцию, которая переводит переданную ей строку в нижний регистр.
    # Необходимо определить декоратор для этой функции, который имеет один параметр «tag»,
    # определяющий строку с названием тега. Начальное значение тега это «h1». Этот декоратор
    # должен заключать возвращенную функцией строку в соответствующий тег и возвращать результат.
    # Пример заключения строки «Python» в тег «h1»: «<h1>python</h1>». Необходимо в качестве
    # примера вызвать декорированную функцию со значением тега tag = div и вывести результат на
    # экран (Вариант 26 (6)).

    unmarked_text = str(input("Введите строку, которую необходимо перевести в нижний регистр:"))
    tag_html = str(input("Введите тег, в который необходимо заключить строку:"))

    string_lover(unmarked_text)
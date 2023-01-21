from flask import session
from functools import wraps


def check_logged_in(func):
    @wraps(func)   # декорация функции wrapper()
    def wrapper(*args, **kwargs):   # функция принимает ЛЮБОЕ кол-во ЛЮБЫХ аргументов
        if 'logged_in' in session:
            return func(*args, **kwargs)
        return 'You are NOT logged in.'
    return wrapper

# !!!
# py -3 dunder.py - в данном случае имя переменной будет '__main__'
# import dunder - в данном случае импортируется модуль dunder и имя переменной будет 'dunder' и условие не выполнится
print('We start off in: ', __name__)
if __name__ == '__main__':
    print('And end up in: ', __name__)

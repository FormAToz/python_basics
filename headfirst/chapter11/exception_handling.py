import sys

# общая обработка исключений
try:
    1 / 0
except:
    err = sys.exc_info()
    for e in err:
        print(e)


# обработка конкретных исключений (и общая)
try:
    with open('my_file.txt') as fh:
        file_data = fh.read()
    print(file_data)
except FileNotFoundError:
    print('The data file is missing')
except PermissionError:
    print('This is not allowed')
except Exception as err:
    print('Some other error occurred: ', str(err))

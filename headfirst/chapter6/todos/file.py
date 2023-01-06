# открыть файл в режиме "перезаписать данные"
todos = open('todos.txt', 'w')
print('Put out the trash.', file=todos)
print('Feed the cat.', file=todos)
print('Prepare tax return.', file=todos)
todos.close()

tasks = open('todos.txt')
for chore in tasks:
    print(chore, end='')  # вывод без дополнительного перевода строки
tasks.close()

# тот же метод чтения, но с автоматическим закрытием файла
with open('todos.txt') as tasks:
    for chore in tasks:
        print(chore, end='')

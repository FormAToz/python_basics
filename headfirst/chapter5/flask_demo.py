from flask import Flask, render_template, request
from vsearch import search4letters

# '__name__' имя текущего активного модуля (пространства имен), которое надо передать
app = Flask(__name__)


# декоратор ф-ии - настраивает поведение ф-ии (без изменения кода)
@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Welcome to search4letters on the web!')


@app.route('/search', methods=['POST'])
def result_page() -> str:
    title = 'Here are your results:'
    phrase = request.form['phrase']
    letters = request.form['letters']
    result = str(search4letters(phrase, letters))
    return render_template('results.html', the_title=title, the_phrase=phrase, the_letters=letters, the_results=result)


# 'debug=True' flask будет автоматически перезапускаться после изменения кода
app.run(debug=True)

# Для развертывания приложения в облаке следует убирать строку с запуском приложения, т.к. облачные сервисы могут
# сами запускать приложение. Реализация:
# if  __name__ == '__name__':
#     app.run(debug=True)

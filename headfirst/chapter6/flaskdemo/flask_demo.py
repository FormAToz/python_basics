from flask import Flask, render_template, request, escape
from vsearch import search4letters

# '__name__' имя текущего активного модуля (пространства имен), которое надо передать
app = Flask(__name__)


def log_request(req: 'flask_request', res: str) -> None:
    with open('flask_demo.log', 'a') as log:
        print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')


# декоратор ф-ии - настраивает поведение ф-ии (без изменения кода)
@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Welcome to search4letters on the web!')


@app.route('/search', methods=['POST'])
def result_page() -> 'html':
    title = 'Here are your results:'
    phrase = request.form['phrase']
    letters = request.form['letters']
    result = str(search4letters(phrase, letters))
    log_request(request, result)
    return render_template('results.html', the_title=title, the_phrase=phrase, the_letters=letters, the_results=result)


@app.route('/viewlog')
def view_the_log() -> 'html':
    contents = []
    with open('flask_demo.log') as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
    titles = ('Form data', 'Remote address', 'User agent', 'Results')
    return render_template('viewlog.html', the_title='View log', the_row_titles=titles, the_data=contents)


# 'debug=True' flask будет автоматически перезапускаться после изменения кода
app.run(debug=True)

# Для развертывания приложения в облаке следует убирать строку с запуском приложения, т.к. облачные сервисы могут
# сами запускать приложение. Реализация:
# if  __name__ == '__name__':
#     app.run(debug=True)

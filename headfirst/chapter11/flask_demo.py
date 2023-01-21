from flask import Flask, render_template, request, session
from vsearch import search4letters
from DBcm import UseDatabase, ConnectionException, CredentialsException, SQLException
from check_logged_in import check_logged_in

# '__name__' имя текущего активного модуля (пространства имен), которое надо передать
app = Flask(__name__)
# добавление конфига в глобальное пространство веб-приложения (внутр. конфигурацию)
app.config['dbconfig'] = {'database': 'hf_py', 'user': 'hfuser', 'password': '123', 'host': 'localhost', 'port': 5432}
app.secret_key = 'YouWillNeverGuessMySecretKey'


@app.route('/login')
def login() -> str:
    session['logged_in'] = True
    return 'You are now logged in'


@app.route('/logout')
def logout() -> str:
    session.pop('logged_in')
    return 'You are now logged out'


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
    try:
        log_request(request, result)
    except Exception as err:
        print('[ERROR] Logging failed with this error: ', str(err))
    return render_template('results.html', the_title=title, the_phrase=phrase, the_letters=letters, the_results=result)


def log_request(req: 'flask_request', res: str) -> None:
    """Запись в БД параметров вэб-запроса и возвращаемого результата"""

    insert_sql = """
        INSERT INTO log (phrase, letters, ip, browser_string, results)
        VALUES (%s, %s, %s, %s, %s)
        """
    with UseDatabase(app.config['dbconfig']) as cursor:
        cursor.execute(insert_sql, (req.form['phrase'], req.form['letters'], req.remote_addr, str(req.user_agent), res))


@app.route('/viewlog')
@check_logged_in
def view_the_log() -> 'html':
    """Отображение записей из БД в виде HTML"""

    try:
        select_all_sql = """SELECT phrase, letters, ip, browser_string, results FROM log"""

        with UseDatabase(app.config['dbconfig']) as cursor:
            cursor.execute(select_all_sql)
            contents = cursor.fetchall()
        titles = ('Phrase', 'Letters', 'Remote address', 'User agent', 'Results')
        return render_template('viewlog.html', the_title='View log', the_row_titles=titles, the_data=contents)
    except ConnectionException as err:
        print('[ERROR] Is database switched on? Error: ', str(err))
    except CredentialsException as err:
        print('[ERROR] UserId/Password issues. Error: ', str(err))
    except SQLException as err:
        print('[ERROR] Is query correct? Error: ', str(err))
    except Exception as err:
        print('[ERROR] Something went wrong: ', str(err))


# 'debug=True' flask будет автоматически перезапускаться после изменения кода
app.run(debug=True)

# Для развертывания приложения в облаке следует убирать строку с запуском приложения, т.к. облачные сервисы могут
# сами запускать приложение. Реализация:
# if  __name__ == '__name__':
#     app.run(debug=True)

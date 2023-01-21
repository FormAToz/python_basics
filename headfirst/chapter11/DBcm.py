import psycopg2


class ConnectionException(Exception):
    pass


class CredentialsException(Exception):
    pass


class SQLException(Exception):
    pass


class UseDatabase:

    # инициализация (при необходимости)
    def __init__(self, config: dict) -> None:
        self.configuration = config

    # настройка при выполнении инструкции with
    def __enter__(self) -> 'cursor':
        try:
            self.conn = psycopg2.connect(**self.configuration)
            self.cursor = self.conn.cursor()
            return self.cursor
        except psycopg2.InterfaceError as err:
            raise ConnectionException(err)
        except psycopg2.ProgrammingError as err:
            raise CredentialsException(err)

    # завершающие операции (после выполнения with)
    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
        if exc_type is psycopg2.ProgrammingError:
            raise SQLException(exc_val)
        elif exc_type:
            raise exc_type(exc_val)

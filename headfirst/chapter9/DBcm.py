import psycopg2


class UseDatabase:

    # инициализация (при необходимости)
    def __init__(self, config: dict) -> None:
        self.configuration = config

    # настройка при выполнении инструкции with
    def __enter__(self) -> 'cursor':
        self.conn = psycopg2.connect(**self.configuration)
        self.cursor = self.conn.cursor()
        return self.cursor

    # завершающие операции (после выполнения with)
    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

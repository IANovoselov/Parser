import psycopg2


class ConnectionErrors(Exception):
    pass


class SQLError(Exception):
    pass


class UseDataBase:

    def __init__(self, config: dict) -> None:
        self.configuration = config

    def __enter__(self):
        try:
            self.conn = psycopg2.connect(**self.configuration)
            self.cursor = self.conn.cursor()
            return self.cursor
        except psycopg2.InterfaceError as err:
            raise ConnectionErrors(err)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
        if exc_type is psycopg2.ProgrammingError:
            raise  SQLError(exc_val)
        elif exc_type:
            raise  exc_type(exc_val)

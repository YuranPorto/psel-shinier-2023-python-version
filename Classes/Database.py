import firebirdsql
from .credentials import *


class DataBase:
    conn = firebirdsql.connect(
        host=HOST,
        database=DATABASE,
        port=PORT,
        user=USER,
        password=PASSWORD,
        charset='WIN1252'
    )
    def execute(self, sql):
        try:
            cur =self.conn.cursor()
            cur.execute(sql)
            return cur

        except Exception(BaseException):
            print(f'Erro ao conectar no banco de dados {Exception(BaseException)}')



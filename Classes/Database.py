import firebirdsql
import credentials


class DataBase:
    conn = firebirdsql.connect(
        host=credentials.HOST,
        database=credentials.DATABASE,
        port=credentials.PORT,
        user=credentials.USER,
        password=credentials.PASSWORD,
        charset='WIN1252'
    )

    def execute(self, sql):
        try:
            cur =self.conn.cursor()
            cur.execute(sql)
            return cur

        except Exception(BaseException):
            print(f'Erro ao conectar no banco de dados {Exception(BaseException)}')



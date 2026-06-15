from database.database import cursor

class VerificacaoLogin:
    def verificar(self, login, senha):
        sql = """
            SELECT idUsuario,
                   nome,
                   tipo_usuario,
                   partidas_ganhas,
                   partidas_perdidas,
                   pontuacao
            FROM usuario
            WHERE email = %s AND senha = %s
        """
        cursor.execute(sql, (login, senha))
        return cursor.fetchone()
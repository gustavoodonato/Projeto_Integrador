from database.database import cursor

def verificar_login(login, senha):

    sql = """
    SELECT nome,
           tipo_usuario,
           partidas_ganhas,
           partidas_perdidas,
           pontuacao
    FROM usuario
    WHERE email = %s AND senha = %s
    """

    cursor.execute(sql, (login, senha))

    return cursor.fetchone()
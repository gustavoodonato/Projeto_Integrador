from database.database import cursor

def listar_alunos():

    sql = """
    SELECT nome,
           partidas_ganhas,
           partidas_perdidas,
           pontuacao
    FROM usuario
    WHERE tipo_usuario = 'Aluno'
    """

    cursor.execute(sql)

    return cursor.fetchall()
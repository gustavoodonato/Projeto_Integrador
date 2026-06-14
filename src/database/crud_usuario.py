from database.database import conexao, cursor

def adicionar_usuario(nome, email, senha, tipo_usuario):

    sql = """
    INSERT INTO usuario
    (
        nome,
        email,
        senha,
        tipo_usuario,
        partidas_ganhas,
        partidas_perdidas,
        pontuacao
    )
    VALUES (%s, %s, %s, %s, 0, 0, 0)
    """

    cursor.execute(
        sql,
        (nome, email, senha, tipo_usuario)
    )

    conexao.commit()


def listar_usuarios():

    sql = """
    SELECT
        idUsuario,
        nome,
        email,
        senha,
        tipo_usuario,
        partidas_ganhas,
        partidas_perdidas,
        pontuacao
    FROM usuario
    """

    cursor.execute(sql)

    return cursor.fetchall()



def buscar_usuario(email, senha):

    sql = """
    SELECT
        idUsuario,
        nome,
        email,
        senha,
        tipo_usuario,
        partidas_ganhas,
        partidas_perdidas,
        pontuacao
    FROM usuario
    WHERE email = %s
    AND senha = %s
    """

    cursor.execute(sql, (email, senha))

    return cursor.fetchone()


def atualizar_usuario(
    id_usuario,
    nome,
    email,
    senha,
    tipo_usuario
):

    sql = """
    UPDATE usuario
    SET
        nome = %s,
        email = %s,
        senha = %s,
        tipo_usuario = %s
    WHERE idUsuario = %s
    """

    cursor.execute(
        sql,
        (
            nome,
            email,
            senha,
            tipo_usuario,
            id_usuario
        )
    )

    conexao.commit()


def deletar_usuario(id_usuario):

    sql = """
    DELETE FROM usuario
    WHERE idUsuario = %s
    """

    cursor.execute(sql, (id_usuario,))

    conexao.commit()
def atualizar_senha(email, nova_senha):

    sql = """
    UPDATE usuario
    SET senha = %s
    WHERE email = %s
    """

    cursor.execute(
        sql,
        (nova_senha, email)
    )

    conexao.commit()
def deletar_usuario_email(email):

    sql = """
    DELETE FROM usuario
    WHERE email = %s
    """

    cursor.execute(sql, (email,))

    conexao.commit()
from datetime import datetime
from database.database import conexao, cursor


def buscar_pedras_por_nivel(nivel: str):
    sql = """
    SELECT idPeca, lado_esquerdo, tipo_esquerdo, lado_direito, tipo_direito
    FROM Peca
    WHERE nivel = %s
    """
    cursor.execute(sql, (nivel,))
    return cursor.fetchall()


def criar_partida(id_usuario: int) -> int:
    sql = """
        INSERT INTO Partida (data_inicio, situacao_partida, Usuario_idUsuario)
        VALUES (%s, 'em_andamento', %s)
    """
    cursor.execute(sql, (datetime.now(), id_usuario))
    conexao.commit()
    return cursor.lastrowid


def finalizar_partida(id_partida: int):
    sql = """
        UPDATE Partida
        SET data_fim = %s, situacao_partida = 'finalizada'
        WHERE idPartida = %s
    """
    cursor.execute(sql, (datetime.now(), id_partida))
    conexao.commit()


def buscar_pontuacao_usuario(id_usuario: int) -> int:
    sql = "SELECT pontuacao FROM usuario WHERE idUsuario = %s"
    cursor.execute(sql, (id_usuario,))
    resultado = cursor.fetchone()
    return resultado[0] if resultado else 0


def atualizar_pontuacao_usuario(id_usuario: int, pontuacao_nova: int):
    pontuacao_atual = buscar_pontuacao_usuario(id_usuario)
    if pontuacao_nova > pontuacao_atual:
        sql = "UPDATE usuario SET pontuacao = %s WHERE idUsuario = %s"
        cursor.execute(sql, (pontuacao_nova, id_usuario))
        conexao.commit()


def incrementar_partidas_ganhas(id_usuario: int):
    sql = """
        UPDATE usuario
        SET partidas_ganhas = partidas_ganhas + 1
        WHERE idUsuario = %s
    """
    cursor.execute(sql, (id_usuario,))
    conexao.commit()
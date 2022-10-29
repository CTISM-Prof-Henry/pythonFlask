import os
import sqlite3


def main(query: str = None, database_path: str = None):
    # pega o caminho absoluto do arquivo do banco de dados
    # por exemplo, se o banco.db estiver na pasta C:\Users\aluno,
    # database_path vai ser C:\Users\aluno\banco.db
    if database_path is None:
        database_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'banco.db')

    if query is None:
        raise ValueError('query não pode ser None!')

    # se conecta ao arquivo do banco
    with sqlite3.connect(database_path) as con:
        # pega um cursor para executar as operações
        # um cursor é uma conexão para o banco de dados (e.g. cria, deleta, insere, etc)
        cur = con.cursor()

        answer = cur.execute(query).fetchall()
        return answer


if __name__ == '__main__':
    main()

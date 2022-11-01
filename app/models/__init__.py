"""
Arquivo que deleta o banco de dados (se ele existir) e recria as tabelas e tuplas.
"""

import sqlite3
import os
from datetime import datetime as dt


def data_para_string(data: dt) -> str:
    """
    Converte uma data para uma string, no formato ANO-MÊS-DIA.
    """
    string = data.strftime('%Y-%m-%d')
    return string


def string_para_data(string: str) -> dt:
    """
    Converte uma string no formato ANO-MÊS-DIA para uma data.
    """
    data = dt.strptime(string, '%Y-%m-%d')
    return data


def query_function(query: str = None, database_path: str = None) -> list:
    """
    Função para fazer pesquisas no banco de dados.

    :param query: A string de consulta sqlite.
    :param database_path: Caminho do banco de dados. Caso não seja provido, irá assumir que o banco é um arquivo
                          banco.db na pasta deste script.
    :return: Uma lista de tuplas, onde cada tupla é uma tupla do banco de dados.
    """
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


def cria_tabelas(cur: sqlite3.Cursor) -> sqlite3.Cursor:
    """
    Cria as tabelas do banco de dados.

    :param cur: um cursor para o banco de dados.
    :return: um cursor para o banco de dados.
    """

    cur.execute('''
        CREATE TABLE IF NOT EXISTS materias (
            id_materia INTEGER NOT NULL,
            nome TEXT NOT NULL,
            periodos INTEGER NOT NULL,
            PRIMARY KEY (id_materia)
        )
    ''')

    cur.execute('''
        CREATE TABLE IF NOT EXISTS professores (
            id_professor INTEGER NOT NULL,
            nome TEXT NOT NULL,
            cabelo TEXT NOT NULL,
            barba TEXT NOT NULL,
            PRIMARY KEY (id_professor)
        )
    ''')

    cur.execute('''
        CREATE TABLE IF NOT EXISTS professores_para_materias (
            id_professor INTEGER NOT NULL,
            id_materia INTEGER NOT NULL,
            data_inicio TEXT NOT NULL DEFAULT '2022-04-11',
            data_fim TEXT NOT NULL DEFAULT '2023-02-15',
            PRIMARY KEY (id_professor, id_materia, data_inicio, data_fim),
            FOREIGN KEY (id_professor) REFERENCES professores(id_professor),
            FOREIGN KEY (id_materia) REFERENCES materias(id_materia)
        )
    ''')

    return cur


def insere_tuplas(cur: sqlite3.Cursor) -> sqlite3.Cursor:
    """
    Insere tuplas no banco de dados.

    :param cur: um cursor para o banco de dados.
    :return: um cursor para o banco de dados.
    """

    cur.execute('''INSERT INTO professores(id_professor, nome, cabelo, barba) VALUES (1, 'Fábio', 'não', 'não');''')
    cur.execute('''INSERT INTO professores(id_professor, nome, cabelo, barba) VALUES (2, 'Henry', 'sim', 'sim');''')
    cur.execute('''INSERT INTO professores(id_professor, nome, cabelo, barba) VALUES (3, 'Rafael Pereira', 'sim', 'sim');''')
    cur.execute('''INSERT INTO professores(id_professor, nome, cabelo, barba) VALUES (4, 'Lairane', 'sim', 'não');''')
    cur.execute('''INSERT INTO professores(id_professor, nome, cabelo, barba) VALUES (5, 'Mário', 'sim', 'não');''')
    cur.execute('''INSERT INTO professores(id_professor, nome, cabelo, barba) VALUES (6, 'Gustavo', 'sim', 'sim');''')
    cur.execute('''INSERT INTO professores(id_professor, nome, cabelo, barba) VALUES (7, 'Karina', 'sim', 'não');''')
    cur.execute('''INSERT INTO professores(id_professor, nome, cabelo, barba) VALUES (8, 'Roberto', 'sim', 'não');''')
    cur.execute('''INSERT INTO professores(id_professor, nome, cabelo, barba) VALUES (9, 'Priscila', 'sim', 'não');''')
    cur.execute('''INSERT INTO professores(id_professor, nome, cabelo, barba) VALUES (10, 'Shirley', 'sim', 'não');''')

    cur.execute('''INSERT INTO materias(id_materia, nome, periodos) VALUES (1, 'Internet das Coisas', 3);''')
    cur.execute('''INSERT INTO materias(id_materia, nome, periodos) VALUES (2, 'Banco de Dados', 3);''')
    cur.execute('''INSERT INTO materias(id_materia, nome, periodos) VALUES (3, 'Desenvolvimento de Sistemas', 3);''')
    cur.execute('''INSERT INTO materias(id_materia, nome, periodos) VALUES (4, 'Sociologia', 1)''')
    cur.execute('''INSERT INTO materias(id_materia, nome, periodos) VALUES (5, 'Física', 3)''')
    cur.execute('''INSERT INTO materias(id_materia, nome, periodos) VALUES (6, 'Princípios de Gestão', 3)''')
    cur.execute('''INSERT INTO materias(id_materia, nome, periodos) VALUES (7, 'História', 2)''')

    cur.execute('''INSERT INTO professores_para_materias(id_professor, id_materia) VALUES (1, 1);''')
    cur.execute('''INSERT INTO professores_para_materias(id_professor, id_materia) VALUES (1, 2);''')
    cur.execute('''INSERT INTO professores_para_materias(id_professor, id_materia) VALUES (2, 3);''')

    cur.execute('''INSERT INTO professores_para_materias(id_professor, id_materia, data_inicio, data_fim) VALUES (4, 5, '2022-04-11', '2022-05-11');''')
    cur.execute('''INSERT INTO professores_para_materias(id_professor, id_materia, data_inicio, data_fim) VALUES (5, 5, '2022-05-11', '2022-06-11');''')
    cur.execute('''INSERT INTO professores_para_materias(id_professor, id_materia, data_inicio, data_fim) VALUES (6, 5, '2022-06-11', '2023-02-15');''')

    cur.execute('''INSERT INTO professores_para_materias(id_professor, id_materia, data_inicio, data_fim) VALUES (7, 6, '2022-04-11', '2022-05-11');''')
    cur.execute('''INSERT INTO professores_para_materias(id_professor, id_materia, data_inicio, data_fim) VALUES (8, 6, '2022-05-11', '2022-06-11');''')
    cur.execute('''INSERT INTO professores_para_materias(id_professor, id_materia, data_inicio, data_fim) VALUES (9, 6, '2022-06-11', '2023-02-15');''')
    cur.execute('''INSERT INTO professores_para_materias(id_professor, id_materia, data_inicio, data_fim) VALUES (10, 6, '2022-06-11', '2023-02-15');''')

    return cur


def main(database_path: str = None):
    print('---------- rotina do banco de dados ----------')

    # pega o caminho absoluto do arquivo do banco de dados
    # por exemplo, se o banco.db estiver na pasta C:\Users\aluno,
    # database_path vai ser C:\Users\aluno\banco.db
    if database_path is None:
        database_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'banco.db')

    # se o banco de dados existir, deleta-o
    # isso facilita a vida na hora que formos re-gerar o banco, pois evita que tuplas
    # com ID repetido sejam inseridas novamente
    if os.path.exists(database_path):
        print('removendo banco de dados antigo encontrado...')
        os.remove(database_path)
        print('banco de dados antigo removido!')

    # cria o arquivo do banco se ele não existe
    # ou se conecta ao arquivo se existir
    with sqlite3.connect(database_path) as con:
        print('banco de dados criado!')
        # pega um cursor para executar as operações
        # um cursor é uma conexão para o banco de dados (e.g. cria, deleta, insere, etc)
        cur = con.cursor()

        cur = cria_tabelas(cur)
        print('tabelas criadas!')
        cur = insere_tuplas(cur)
        print('tuplas inseridas!')

        # salva as modificações feitas no banco
        con.commit()
        print('banco de dados salvo!')

    print('---------- rotina do banco de dados ----------')


if __name__ == '__main__':
    main()

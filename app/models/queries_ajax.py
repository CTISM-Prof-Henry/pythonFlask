import flask
from flask import request, jsonify

try:
    # esse bloco de código roda se o código for executado pelo Pycharm
    folder = ''
    from app.models import query_function
except ModuleNotFoundError:
    # esse bloco de código roda se o código for executado pela linha de comando
    from models import query_function


def main(app: flask.app.Flask) -> flask.app.Flask:
    @app.route('/generate_table', methods=['POST'])
    def generate_table():
        table_name = request.form['opcao_selecionada']
        # pega o nome das colunas
        table_columns = query_function('''select name from pragma_table_info("{0}");'''.format(table_name))
        table_columns = tuple([x[0] for x in table_columns])  # transforma a lista de tuplas numa tupla
        # pega os dados
        answer = query_function('''SELECT * FROM {0}'''.format(table_name))
        # transforma os dados
        new_answer = []
        for line in answer:
            new_answer.append({k: v for k, v in zip(table_columns, line)})
        # monta a resposta
        response = jsonify(new_answer)
        response.headers.add('Access-Control-Allow-Origin', '*')  # Essa linha é necessária. Requisição dos navegadores
        return response  # retorna resposta para a página Web

    return app

import os
import sys
import flask

from flask import Flask, jsonify, request, Response


def main():
    app = Flask(
        'Minha primeira aplicação Flask',
        template_folder='templates',
        static_folder='static',
        instance_relative_config=True
    )

    app.config.from_object('config')
    app.config.from_pyfile('config.py')

    # define os métodos de acesso ao backend. Perceba que estes métodos estão
    # definidos dentro do escopo da função main, e que o servidor é definido
    # e inicializado dentro deste escopo

    @app.route('/')
    def initial_page():
        return flask.render_template('main.html')

    # @app.route('/server_generated_page', methods=['POST'])
    @app.route('/server_generated_page', methods=['GET'])
    def server_generated_page():
        return flask.render_template(
            'server_generated_page.html',
            paragrafo='<p class="center">Este parágrafo foi renderizado pelo servidor!</p>',
            imagem='<img class="center" src="' + flask.url_for('static', filename='images/ye_smiling.jpg') + '">'
        )

    @app.route('/ajax_generated_table', methods=['GET'])
    def ajax_generated_table():
        return flask.render_template('ajax_generated_table.html')

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
        response.headers.add('Access-Control-Allow-Origin', '*')  # essa linha é necessária. requisição dos navegadores
        return response  # retorna resposta para a página Web

    # coloca o backend a rodar no modo debug; modificações feitas nos arquivos de código-fonte
    # irão ser refletidas em tempo real nas páginas Web
    app.run(use_reloader=app.config["USE_REALODER"])


if __name__ == '__main__':
    cur_path = os.sep.join(os.path.dirname(os.path.abspath(__file__)).split(os.sep)[:-1])
    cur_path = os.path.join(cur_path, 'app')
    os.chdir(cur_path)

    project_path = os.sep.join(os.path.dirname(os.path.abspath(__file__)).split(os.sep)[:-1])
    sys.path.append(project_path)

    from app.models import main as database_routine
    from app.models.query import main as query_function
    database_routine()
    main()

import os
import sys
import flask

from flask import Flask, jsonify, request, Response


def main():
    app = Flask(
        'Minha primeira aplicação Flask',
        template_folder='templates',
        static_folder='static'
    )

    # define os métodos de acesso ao backend. Perceba que estes métodos estão
    # definidos dentro do escopo da função main, e que o servidor é definido
    # e inicializado dentro deste escopo

    @app.route('/')
    def initial_page():
        return flask.render_template('main.html')

    @app.route('/server_generated_page', methods=['POST'])
    def server_generated_page():
        folder = request.form['textfield_folder']
        folders = os.listdir(folder)
        response = jsonify({group_name: os.path.join(folder, group_name) for group_name in folders})
        response.headers.add('Access-Control-Allow-Origin', '*')  # deve estar sempre presente
        return response

    @app.route('/ajax_generated_table', methods=['POST'])
    def ajax_generated_table():
        folder = request.form['textfield_folder']
        folders = os.listdir(folder)
        response = jsonify({group_name: os.path.join(folder, group_name) for group_name in folders})
        response.headers.add('Access-Control-Allow-Origin', '*')  # deve estar sempre presente
        return response

    # coloca o backend a rodar
    app.run()


if __name__ == '__main__':
    cur_path = os.sep.join(os.path.dirname(os.path.abspath(__file__)).split(os.sep)[:-1])
    cur_path = os.path.join(cur_path, 'app')
    os.chdir(cur_path)

    project_path = os.sep.join(os.path.dirname(os.path.abspath(__file__)).split(os.sep)[:-1])
    sys.path.append(project_path)

    main()

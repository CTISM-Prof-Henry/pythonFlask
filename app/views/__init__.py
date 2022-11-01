"""
Arquivo com definições de roteamento para a aplicação.

É uma boa prática de programação colocar o mesmo nome do roteamento, da função e do arquivo HTML.
"""

import flask


def main(app: flask.app.Flask) -> flask.app.Flask:
    @app.route('/')
    def initial_page():
        return flask.render_template('main.html')

    @app.route('/server_generated_page', methods=['GET'])
    def server_generated_page():
        return flask.render_template(
            'server_generated_page.html',
            paragrafo='<p class="center">Este parágrafo foi renderizado pelo servidor!</p>',
            imagem='<img class="center" src="' + flask.url_for('static', filename='img/ye_smiling.jpg') + '">'
        )

    @app.route('/ajax_generated_table', methods=['GET'])
    def ajax_generated_table():
        return flask.render_template('ajax_generated_table.html')

    return app

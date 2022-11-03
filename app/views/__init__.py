"""
Arquivo com definições de roteamento para a aplicação.

É uma boa prática de programação colocar o mesmo nome do roteamento, da função e do arquivo HTML.
"""

import flask

try:
    # esse bloco de código roda se o código for executado pelo Pycharm
    folder = ''
    from app.models import query_function
except ModuleNotFoundError:
    # esse bloco de código roda se o código for executado pela linha de comando
    from models import query_function


def main(app: flask.app.Flask) -> flask.app.Flask:
    @app.route('/')
    def initial_page():
        return flask.render_template('main.html')

    @app.route('/materias/<nome_da_materia>', methods=['GET'])
    def materias(nome_da_materia):
        texto_paragrafos = '<p class="center">Esta é a página da matéria {0}!</p>\n'.format(nome_da_materia)
        texto_paragrafos += '<p class="center">Veja abaixo os professores que já deram essa disciplina:</p>\n'

        answer = query_function('''
            SELECT p.nome
            FROM professores p
            INNER JOIN professores_para_materias ppm on p.id_professor = ppm.id_professor
            INNER JOIN materias m on ppm.id_materia = m.id_materia
            WHERE m.nome = '{0}';
        '''.format(nome_da_materia))

        texto_paragrafos += '<ul class="center">\n'
        for prof in answer:
            texto_paragrafos += '\t<li>{0}</li>\n'.format(prof[0])
        texto_paragrafos += '</ul>'

        return flask.render_template(
            'server_generated_page.html',
            paragrafo=texto_paragrafos,
            imagem=''
        )

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

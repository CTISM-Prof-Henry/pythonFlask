import os
import sys

from flask import Flask

try:
    # esse bloco de código roda se o código for executado pelo Pycharm
    folder = 'config.py'
    from app.static.database import main as database_routine
    from app.models import query_function, main as models_func
    from app.views import main as views_func
except ModuleNotFoundError:
    # esse bloco de código roda se o código for executado pela linha de comando
    folder = os.sep.join(os.path.dirname(os.path.abspath(__file__)).split(os.sep)[:-1])
    os.chdir(os.path.join(folder, 'app'))
    folder = os.path.join(folder, 'app', 'config.py')

    from static.database import main as database_routine
    from models import query_function, main as models_func
    from views import main as views_func


def main():
    # configura a aplicação e define as pastas onde ela deve procurar os itens
    app = Flask(
        'Minha primeira aplicação Flask',
        template_folder='templates',
        static_folder='static',
        instance_relative_config=True
    )
    # configura os arquivos de definições, app/config.py e app/instance/config.py
    app.config.from_object('config')
    try:
        app.config.from_pyfile(folder)
    except FileNotFoundError:
        print('--' * 55, file=sys.stderr)
        print(
            ' O arquivo app/instance/config.py não foi encontrado, '
            'então o arquivo app/config.py será usado no seu lugar.',
            file=sys.stderr
        )
        print('--' * 55, file=sys.stderr)

    # se
    #   GENERATE_DB = True
    # em app/instance/config.py ou em app/config.py, deleta o banco
    # de dados antigo e cria-o de novo
    if app.config["GENERATE_DB"]:
        database_routine()

    app = models_func(app)  # carrega as definições de funções ajax na aplicação
    app = views_func(app)  # carrega as definições de roteamento na aplicação

    # coloca o backend a rodar no modo debug; modificações feitas nos arquivos de código-fonte
    # se refletirão em tempo real nas páginas Web (basta dar um F5 no navegador)
    app.run(use_reloader=app.config["USE_REALODER"])


if __name__ == '__main__':
    main()

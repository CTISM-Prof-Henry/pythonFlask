import os

from flask import Flask

try:
    # esse bloco de código roda se o código for executado pelo Pycharm
    folder = ''
    from app.models import main as database_routine, query_function
    from app.views import main as view_func
    from app.models.queries_ajax import main as queries_ajax_func
except ModuleNotFoundError:
    # esse bloco de código roda se o código for executado pela linha de comando
    if os.name == 'nt':
        folder = os.path.join('..', 'app')
    else:
        folder = os.sep.join(os.path.dirname(os.path.abspath(__file__)).split(os.sep)[:-1])
        folder = os.path.join(folder, 'app', 'instance')
    from models import main as database_routine, query_function
    from views import main as view_func
    from models.queries_ajax import main as queries_ajax_func


def main():
    app = Flask(
        'Minha primeira aplicação Flask',
        template_folder='templates',
        static_folder='static',
        instance_relative_config=True
    )
    print(folder)
    app.config.from_object('config')
    app.config.from_pyfile(os.path.join(folder, 'config.py'))

    app = view_func(app)
    app = queries_ajax_func(app)

    # coloca o backend a rodar no modo debug; modificações feitas nos arquivos de código-fonte
    # irão ser refletidas em tempo real nas páginas Web
    app.run(use_reloader=app.config["USE_REALODER"])


if __name__ == '__main__':
    database_routine()
    main()

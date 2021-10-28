from flask import Flask, jsonify
from datetime import datetime as dt


def main():
    app = Flask(__name__)  # inicia uma aplicação do flask (o backend)

    # define os métodos de acesso ao backend. Perceba que estes métodos estão
    # definidos dentro do escopo da função main, e que o servidor é definido
    # e inicializado dentro deste escopo

    @app.route('/')
    def initial_page():
        return '''
        <h1>Olá mundo!</h1>
        <p>Você acessou a página inicial da Web API.</p>
        '''

    @app.route('/tell_time', methods=[])
    def populate_table():
        current_time = dt.now()

        response = jsonify(
            {
                'ano': current_time.year,
                'mes': current_time.month,
                'dia': current_time.day,
                'hora': current_time.hour,
                'minuto': current_time.minute,
                'segundo': current_time.second
            }
        )
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    # coloca o backend a rodar
    app.run()


if __name__ == '__main__':
    main()


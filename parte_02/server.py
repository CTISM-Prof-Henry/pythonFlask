import os

from flask import Flask, jsonify, request, send_file, Response, send_from_directory


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

    @app.route('/soundboard', methods=['POST'])
    def soundboard():

        # request é um método para pegar as requisições que vêm da view.
        # então, da lista de formulários (form) da requisição (request),
        # pega o valor do seletor que possui nome 'soundboard_dropdown'
        # quem definiu o nome dessa variável fomos nós mesmos, através da
        # construção da página HTML (view)
        soundboard_dropdown = request.form['soundboard_dropdown']
        print('O áudio solicitado foi', soundboard_dropdown)

        # pega o diretório do script atual
        response = Response(
            'esta mensagem foi escrita pelo servidor. O áudio solicitado foi %s.mp3' % soundboard_dropdown
        )
        # adiciona um cabeçalho à resposta
        response.headers.add('Access-Control-Allow-Origin', '*')
        # devolve a resposta ao AJAX - ele que irá tratar agora
        return response

    # outras coisas interessantes, mas que não serão usadas no trabalho

    # @app.route('/soundboard/<path:filename>')
    @app.route('/soundboard/<path:filename>')
    def uepa(filename):
        # pega o diretório do script atual
        current_script_path = os.path.dirname(os.path.abspath(__file__))

        response = send_from_directory(
            directory=os.path.join(current_script_path, 'audios'),
            filename=filename,  # 'uepa.mp3'
            as_attachment=True
        )

        # adiciona um cabeçalho à resposta
        response.headers.add('Access-Control-Allow-Origin', '*')
        # devolve a resposta ao AJAX - ele que irá tratar agora
        return response

    # coloca o backend a rodar
    app.run()


if __name__ == '__main__':
    main()


import flask
from flask_bcrypt import Bcrypt


def hash_function(app: flask.app.Flask, password: str) -> None:
    bcrypt = Bcrypt(app)  # para encriptar senhas de usuários
    # passando o hash na senha 12 vezes. o número de vezes depende do poder computacional do servidor
    # quanto maior o número de vezes que o hash for aplicado, mas demorada será a resposta do servidor
    # porém, quanto maior o número, também mais segura a aplicação será
    from flask_bcrypt import generate_password_hash
    generate_password_hash('password1', 12)

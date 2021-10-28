import flask
from flask import request, jsonify
import pandas as pd

app = flask.Flask(__name__)
app.config["DEBUG"] = True

produtos = pd.DataFrame(
    data=[
        ['refrigerante A', 'bebida', 5],
        ['refrigerante B', 'bebida', 7],
        ['pizza pequena', 'pizza', 30],
        ['pizza média', 'pizza', 40],
        ['pizza grande', 'pizza', 50],
        ['bombom', 'doce', 1]
    ],
    columns=['nome', 'tipo', 'valor']
)

sabores = pd.DataFrame(
    data=[
        ['calabresa'], 
        ['portuguesa'],
        ['chocolate']
    ],
    columns=['nome']
)

produto_para_sabor_index = pd.MultiIndex.from_tuples([
        (2, 2),
        (3, 0),
        (3, 1),
        (4, 0),
        (4, 1)
    ], names=['id_produto', 'id_sabor'])

produto_para_sabor = pd.DataFrame(
    index=produto_para_sabor_index
)


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>O recurso solicitado não pôde ser encontrado.</p>", 404


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Pizzaria do Henry</h1>
<p>Bem vindo à pizzaria do Henry! Sente-se e sinta-se a vontade!</p>'''


@app.route('/api/v1/recursos/produtos/all', methods=['GET'])
def produtos_all():
    return jsonify(produtos.to_json())


@app.route('/api/v1/recursos/sabores/all', methods=['GET'])
def sabores_all():
    return jsonify(sabores.to_json())

@app.route('/api/v1/recursos/produtos', methods=['GET'])
def api_filter():
    query_parameters = request.args

    some_id = query_parameters.get('id')
    tipo = query_parameters.get('tipo')

    res = produtos

    if some_id:
        res = produtos.loc[int(some_id)]
    if tipo:
        res = res.loc[res['tipo'] == tipo]
    if (not some_id) and (not tipo):
        return page_not_found(404)
    
    return jsonify(res.to_json())

app.run()
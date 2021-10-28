# pythonFlask

## Introdução

## Importante

Para realizar estes exercícios, recomenda-se que você abra dois Prompts de Comando do seu Sistema Operacional,
um para rodar o código do servidor, e outro para rodar o código do cliente. 

Você pode rodar pelo menos um dos dois códigos na sua IDE de escolha (Pycharm, VS Code, etc), **mas não é possível rodar
os dois códigos ao mesmo tempo na IDE**.

## Exercícios

Existem três formas de acessar o servidor: 

a. Pelo seu navegador (Chrome, Firefox, Waterfox, Opera, Brave, Safari)
b. Pelo código-fonte em Python do cliente, [client.py](client.py)
c. Pela página HTML de testes, [index.html](index.html)

1. Sem modificar o código-fonte do servidor, coloque script do servidor a rodar, pela linha de comando:
   
   ```bash
   python server.py
   ```
   
   a. Abra seu navegador e acesse a URL [http://127.0.0.1:5000/tell_time](http://127.0.0.1:5000/tell_time). O que é mostrado
      na tela?
   b. Em outro prompt de comando, e sem interromper a execução do servidor, rode o script do cliente, `python client.py`.
      O que é mostrado no console?
   c. Abra a página HTML [index.html](index.html) no seu navegador. Abra o console de desenvolvedor (tecla F12), e selecione
      a aba "Console". Agora aperte no (único) botão desta página. O que acontece? 

2. Interrompa a execução do servidor (`CTRL + C` na janela do console em que ele está executando). Abra o arquivo 
   [server.py](server.py) e modifique o decorador da função `tell_time` de forma que ele fique assim:

   ```python
   @app.route('/tell_time', methods=['GET'])
   ```
   
   Coloque o servidor a rodar novamente no prompt de comando, e repita os passos **a**, **b** e **c** do primeiro exercício 
   anterior. O que ficou diferente, em cada um dos métodos de acesso?

3. Interrompa a execução do servidor (`CTRL + C` na janela do console em que ele está executando). Abra o arquivo 
   [server.py](server.py) e modifique o decorador da função `tell_time` de forma que ele fique assim:

   ```python
   @app.route('/tell_time', methods=['GET', 'POST'])
   ```
   
   Coloque o servidor a rodar novamente no prompt de comando, e repita os passos **a**, **b** e **c** do primeiro exercício 
   anterior. O que ficou diferente, em cada um dos métodos de acesso?

4. No console que está rodando o código do servidor, você reparou que ele imprime uma nova linha a cada vez que uma nova
   requisição é feita? Se não reparou, repare agora.

5. Com o servidor rodando, acesse a URL [http://127.0.0.1:5000](http://127.0.0.1:5000). O que é mostrado na tela? Analise
   o código-fonte do servidor. De qual função está vindo o que é mostrado na tela, quando acessamos a URL?

## Referências

* [Métodos do protocolo HTTP - W3Schools](https://www.w3schools.com/tags/ref_httpmethods.asp) (em inglês)
* [Métodos do protocolo HTTP - MDN](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Methods)
* [REST API](https://www.redhat.com/pt-br/topics/api/what-is-a-rest-api)
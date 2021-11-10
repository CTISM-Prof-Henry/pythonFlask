# pythonFlask

## Introdução

Flask é uma biblioteca em Python que implementa um micro-controlador (no sentido do modelo de desenvolvimento de Software 
[Model-View-Controller](https://pt.wikipedia.org/wiki/MVC)). Flask **não é** uma das bibliotecas mais populares; ele não
é nem mesmo a biblioteca mais popular implementada em Python -- [Django](https://www.djangoproject.com/), por exemplo,
é bem mais popular.

Todavia, por ser um _micro-controlador_, muitas das complexidades de implementar um backend são abstraídas. Como você verá
neste exercício, é muito fácil definir uma aplicação e colocá-la a rodar, em poucos passos.

Um detalhe importante para ter-se em mente é que Flask segue o protocolo 
[REST](https://www.redhat.com/pt-br/topics/api/what-is-a-rest-api). Ou seja, a comunicação entre cliente e servidor (backend)
não é baseada em estados, mas sim em requisições. O servidor não sabe em que estado atual o cliente está, e isso não importa
para aplicações que são implementadas utilizando o protocolo REST. Um protocolo que leva em consideração o estado do cliente
é o protocolo [SOAP](https://pt.wikipedia.org/wiki/SOAP).

Você pode ler mais sobre as particularidades destes protocolos nos [slides](slides/slides.html) que acompanham este repositório.

## Importante

Para realizar estes exercícios, recomenda-se que você abra dois Prompts de Comando do seu Sistema Operacional,
um para rodar o código do servidor, e outro para rodar o código do cliente. 

Você pode rodar pelo menos um dos dois códigos na sua IDE de escolha (Pycharm, VS Code, etc), **mas não é possível rodar
os dois códigos ao mesmo tempo na IDE**.

## Requisitos

É necessário ter a biblioteca `flask` instalada no seu Python. Você pode instalar tanto pelo `conda`

```bash
conda install --file requirements.txt
```

Ou pelo `pip` (caso você não esteja usando o Python Anaconda) 

```bash
pip install --requirement requirements.txt
```

## Exercícios

* [Parte 1](parte_01/README.md)
* [Parte 2](parte_02/README.md)

## Referências

* [Métodos do protocolo HTTP - W3Schools](https://www.w3schools.com/tags/ref_httpmethods.asp) (em inglês)
* [Métodos do protocolo HTTP - MDN](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Methods)
* [REST API](https://www.redhat.com/pt-br/topics/api/what-is-a-rest-api)
* [Slides - REST, SOAP, Web API](slides/slides.html)
* [Flask](https://flask.palletsprojects.com/en/2.0.x/) (em inglês)
# pythonFlask

Flask é uma biblioteca em Python que implementa um micro-controlador, no sentido do modelo de desenvolvimento de Software 
[Model-View-Controller](https://pt.wikipedia.org/wiki/MVC). O objetivo de Flask é implementar pequenos servidores, com  
poucas requisições de tráfego, para projetos pequenos. Por ser um micro-controlador, Flask não é uma das bibliotecas
mais populares para desenvolvimento de servidores em Python, sendo [Django](https://www.djangoproject.com/) mais popular.

Todavia, por ser um _micro-controlador_, muitas das complexidades de implementar um backend são abstraídas. Como você verá
neste exercício, é muito fácil definir uma aplicação e colocá-la a rodar, em poucos passos.

Flask segue o protocolo [REST](https://www.redhat.com/pt-br/topics/api/what-is-a-rest-api). Ou seja, a comunicação 
entre cliente e servidor (backend) não é baseada em estados, mas sim em requisições. O servidor não sabe em que estado 
atual o cliente está, e isso não importa para aplicações que são implementadas utilizando o protocolo REST. Por exemplo,
um site de compras que usa o protocolo REST não mantém informações do carrinho de compras do usuário no lado do servidor
(essas informações são guardadas do lado do cliente). Ou seja, se o usuário sair do site e não comprar nada, o servidor
jamais saberá quais produtos o usuário colocou no carrinho. Já um site de compras que usa o protocolo 
[SOAP](https://pt.wikipedia.org/wiki/SOAP), que leva em consideração o estado do cliente, terá armazenado as informações
do carrinho de compras e poderá, em um outro momento, enviar um e-mail de lembrete ao usuário pedindo para que ele
conclua a compra no site.

Você pode ler mais sobre as particularidades destes protocolos nos [slides](slides/slides.html) que acompanham este 
repositório.

```mermaid
flowchart TD
    model["model"]
    view["view"]
    controller["controller"]
    user["usuário"]

    view -- "visualiza" --> user
    user -- "utiliza" --> controller

    controller -- "manipula" --> model
    model -- "atualiza" --> view
```

## Sumário


## Índice de termos

* **Model-View-Controller (ou MVC):** modelo de desenvolvimento de Software. Pode ser 
  aplicado a qualquer software compatível com esse modelo de desenvolvimento, como por exemplo sites e aplicativos para 
  celular.
* **Model:** no sistema MVC, é o banco de dados.
* **View:** no sistema MVC, e no desenvolvimento de sites, é o frontend, a página da Web escrita em HTML.
* **Controller:** no sistema MVC, e no desenvolvimento de sites, é o backend, o servidor. Neste repositório, é ensinado 
  como programar um backend com a biblioteca Flask.
* **Frontend:** no desenvolvimento de sites, é a parte que é executada pelo cliente. Compreende a página HTML, o CSS, o 
  Javascript da página e o AJAX.
* **Backend:** no desenvolvimento de sites, é a parte que é executada pelo servidor. Pode ser implementada em qualquer 
  linguagem de programação e usando qualquer biblioteca. Opções populares são: PHP e Laravel; Python e Django; Javascript 
  e node.js; etc.
* **Internet:** a rede de computadores interconectados. Possui diversos protocolos, como TCP/IP, HTTP, HTTPS, FTP, SSH, 
  POP, etc. Cada protocolo cumpre uma função distinta na rede.
* **Web:** é a parte da Internet que contém páginas escritas em HTML, e portanto são legíveis à humanos.
* **HTML:** é como a página Web é estruturada (por exemplo, onde o menu é posicionado, onde o texto é posicionado, o 
  número de imagens em uma página, etc)
* **CSS:** é como a página Web é estilizada (por exemplo, a fonte do texto, a cor do fundo, efeitos gráficos, etc)
* **Javascript:** é uma linguagem de programação interpretada, executada pelo navegador. Páginas da Web costumam possuir
  código Javascript que é rodado diretamente pelo navegador. Este código adiciona interatividade à página (por exemplo,
  permite que uma janela seja aberta quando clicamos em um botão, ou então que um produto seja adicionado ao carrinho)
* **Asynchronous JavaScript and XML (ou AJAX):** conjunto de tecnologias que permitem que uma página da Web seja 
  atualizada de forma assíncrona sem interferir na exibição do conteúdo. Por exemplo, quando um usuário insere seu CEP
  em uma página de compras, o AJAX permite que o servidor responda qual o preço do frete, e a página Web atualize esta
  informação, sem que seja necessário recarregar toda a página.

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

* [Parte 1](atividades/parte_01/README.md)
* [Parte 2](atividades/parte_02/README.md)

## Referências

* [Métodos do protocolo HTTP - W3Schools](https://www.w3schools.com/tags/ref_httpmethods.asp) (em inglês)
* [Métodos do protocolo HTTP - MDN](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Methods)
* [REST API](https://www.redhat.com/pt-br/topics/api/what-is-a-rest-api)
* [Slides - REST, SOAP, Web API](slides/slides.html)
* [Flask](https://flask.palletsprojects.com/en/2.0.x/) (em inglês)
* [AJAX](https://developer.mozilla.org/pt-BR/docs/Web/Guide/AJAX)
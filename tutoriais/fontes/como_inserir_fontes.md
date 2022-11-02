# Como inserir fontes

Se você quiser usar uma fonte customizada (como por exemplo do [Google Fonts](https://fonts.google.com/)), siga o seguinte
passo-a-passo:

1. Ache uma fonte que você gosta. Neste tutorial, usaremos a fonte 
   [Kolker Brush](https://fonts.google.com/specimen/Kolker+Brush) como exemplo.
2. A URL desta fonte no Google Fonts é 
   ```
   https://fonts.google.com/specimen/Kolker+Brush
   ```
   Trocando-a para o formato da API do Google Fonts, a URL da fonte ficará
   ```
   https://fonts.googleapis.com/css?family=Kolker+Brush
   ```
   
   > O site do Google Fonts (https://fonts.google.com/) é uma **página Web**, feita para ser lida por seres humanos. A 
   > **API** do Google Fonts (https://fonts.googleapis.com/css), por outro lado, é feita para que aplicações (como 
   > programas e robôs) acessem-na. Como 1) queremos inserir a fonte no nosso site, 2) o site precisa baixar a fonte do 
   > servidor do Google, e 3) o nosso site não é um ser humano, usamos a API do Google ao invés do site da Web.

3. No arquivo HTML que queremos adicionar a fonte, iremos adicionar uma nova tag `link` dentro do `head`:

```html
<html lang="pt-br">
<head>
    <meta charset="utf-8">
    <link rel="https://fonts.googleapis.com/css?family=Kolker+Brush">
    <title>Olá mundo!</title>
    <style>
        * {
            font-family: "Kolker Brush", sans-serif;
        }
    </style>
</head>
<body>
<h1>Olá mundo!</h1>

<p>
    Esta página usa a fonte <a href="https://fonts.google.com/specimen/Kolker+Brush">Kolker Brush</a> 
    do <a href="https://fonts.google.com/">Google Fonts.</a>
</p>
</body>
</html>
```

Você pode consultar a diferença entre um arquivo [sem fonte do Google Fonts](sem_fonte.html) e outro 
[com fonte](com_fonte.html).

> Neste tutorial, o CSS está sendo definido internamente. Mas você pode definí-lo 
> [inline ou externamente](https://www.w3schools.com/css/css_howto.asp) também.

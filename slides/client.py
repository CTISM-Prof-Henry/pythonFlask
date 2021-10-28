import urllib.request as request
import json

with request.urlopen('http://localhost:5000/api/v1/recursos/sabores/all') as response:
    source = response.read()
    data = json.loads(source)
    print(data)
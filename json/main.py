import json
dados = {
    'nome':'Matheus Vieira',
    'telefone': '21980721158' 
}

with open('dados.json', 'w') as json.__file__:
    json.dump(dados, json.__file__, indent=4)
    dados_json = json.dumps(dados)
    print(dados_json)


with open('dados.json', 'r') as json.__file__:
    file = json.load(json.__file__)
    file_json = json.loads(dados_json)
    print(file)
    print(type(file_json))
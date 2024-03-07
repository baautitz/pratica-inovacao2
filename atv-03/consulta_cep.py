import requests

url = "https://viacep.com.br/ws/85852000/json"

request = requests.get(url)

if request.status_code == 200:
    data = request.json()
    print(f"CEP: {data['cep']}")
    print(f"Logradouro: {data['logradouro']}")
    print(f"Bairro: {data['bairro']}")
    print(f"Cidade: {data['localidade']}")
    print(f"Estado: {data['uf']}")
else:
    print("Falha ao consultar o CEP")

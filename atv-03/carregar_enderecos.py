from os import path
import pandas
import requests


def main():
    nome_arquivo = input("Digite o nome do arquivo .xlsx: ")

    if nome_arquivo[-5:] != ".xlsx":
        nome_arquivo += ".xlsx"

    if not path.isfile(nome_arquivo):
        print("Arquivo não encontrado.")
        return

    arquivo_dataframe = pandas.read_excel(nome_arquivo)
    arquivo_dict = arquivo_dataframe.to_dict()

    if arquivo_dict['nome'][0] is None or arquivo_dict['email'][0] is None or arquivo_dict['cep'][0] is None:
        print("Arquivo inválido")
        return

    logradouros = {}
    bairros = {}
    cidades = {}
    estados = {}

    numeros_pessoas = len(arquivo_dataframe['nome'])
    for x in range(numeros_pessoas):
        print(f"Buscando {x + 1} de {numeros_pessoas}...")

        url = f"https://viacep.com.br/ws/{arquivo_dict['cep'][x]}/json"
        req = requests.get(url)

        if req.status_code != 200:
            logradouros[x] = " "
            bairros[x] = " "
            cidades[x] = " "
            estados[x] = " "
            print("Erro ao consultar CEP!")
            continue

        data = req.json()
        logradouros[x] = data['logradouro']
        bairros[x] = data['bairro']
        cidades[x] = data['localidade']
        estados[x] = data['uf']

    arquivo_dict["logradouro"] = logradouros
    arquivo_dict["bairro"] = bairros
    arquivo_dict["cidade"] = cidades
    arquivo_dict["estado"] = estados

    new_dataframe = pandas.DataFrame(arquivo_dict)
    new_dataframe.to_excel("resultado_enderecos.xlsx", index=False)


main()

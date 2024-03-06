# Faça uma pesquisa sobre a biblioteca Pandas e faça um programa que carregue os dados
# diretamente de um arquivo do excel com a extensão xlsx e faça a impressão na tela informando:
#
# A Quantidade de Alunos.
# RA, Nome, Idade.
from os import path

import pandas


def main():
    nome_arquivo = input("Digite o nome do arquivo .xlsx: ")

    if nome_arquivo[-5:] != ".xlsx":
        nome_arquivo += ".xlsx"

    if not path.isfile(nome_arquivo):
        print("Arquivo não encontrado.")
        return

    arquivo_dataframe = pandas.read_excel(nome_arquivo)
    arquivo_dict = arquivo_dataframe.to_dict()

    if arquivo_dict['RA'][0] is None or arquivo_dict['Nome'][0] is None or arquivo_dict['Idade'][0] is None:
        print("Arquivo inválido")
        return

    if len(arquivo_dict['RA']) < 0:
        print("Arquivo não contém nenhum aluno")
        return

    for x in range(len(arquivo_dict['RA'])):
        print(30 * "-")
        print(f"RA: {arquivo_dict['RA'][x]}")
        print(f"Nome: {arquivo_dict['Nome'][x]}")
        print(f"Idade: {arquivo_dict['Idade'][x]}")
        print(30 * "-")


main()

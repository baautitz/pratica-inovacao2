# Faça um programa que leia os dados de N Alunos e Imprima a lista na tela.
# Adicione a funcionalidade de Imprimir na tela a lista informando a quantidade de alunos na lista e salvar em arquivo TXT. 
# Adicione a funcionalidade de Salvar a Lista em arquivo CSV.

from os import system, path

def ler_aluno():
    nome = input("Digite o nome do aluno: ")
    ra = input("Digite o RA: ")
    disciplina = input("Digite a disciplina: ")

    return {"nome": nome, "ra": ra, "disciplina": disciplina}


def add_aluno(aluno, lista_alunos):
    lista_alunos.append({
        "nome": aluno["nome"],
        "ra": aluno["ra"],
        "disciplina": aluno["disciplina"]
    })


def rem_aluno(nome, lista_alunos):
    for x in range(len(lista_alunos)):
        if nome.lower() != lista_alunos[x]["nome"].lower():
            continue

        lista_alunos.pop(x)
        return True
    return False


def listar_alunos(lista_alunos):
    print("Lista de alunos:")
    for x in range(len(lista_alunos)):
        print(30*"-")
        print(f'Nome: {lista_alunos[x]["nome"]}')
        print(f'RA: {lista_alunos[x]["ra"]}')
        print(f'Disciplina: {lista_alunos[x]["disciplina"]}')
        print(30*"-")


def salvar_txt(arquivo, lista_alunos):
    with open(arquivo, 'w') as f:
        for x in range(len(lista_alunos)):
            f.write(f'Nome: {lista_alunos[x]["nome"]}\n')
            f.write(f'RA: {lista_alunos[x]["ra"]}\n')
            f.write(f'Disciplina: {lista_alunos[x]["disciplina"]}\n\n')


def salvar_csv(arquivo, lista_alunos):
    with open(arquivo, 'w') as f:
        f.write("Nome,RA,Disciplina\n")
        for x in range(len(lista_alunos)):
            f.write(f"{lista_alunos[x]["nome"]},")
            f.write(f"{lista_alunos[x]["ra"]},")
            f.write(f"{lista_alunos[x]["disciplina"]}\n")


def main():
    alunos = []
    while True:
        system("cls")
        print("SISTEMAS DE ALUNOS:")
        print("")
        print(" - A: adicionar um aluno")
        print(" - R: remover um aluno")
        print(" - L: listar alunos")
        print(" - T: exportar lista para TXT")
        print(" - C: exportar lista para CSV")
        print(" - Q: para sair do programa")
        print("")
        opcao = input("Digite a opção desejada: ").lower()
        if opcao == "a":

            print(30*"-")

            a = ler_aluno()
            add_aluno(a, alunos)

            print(30*"-")
            print("Aluno adicionado com sucesso.")

        elif opcao == "r":

            nome = input("Digite o nome do aluno: ")
            if not rem_aluno(nome, alunos):
                print("Aluno não encontrado.")
            else:
                print("Aluno removido com sucesso.")

        elif opcao == "l":
            if not len(alunos) > 0:
                print("Não há alunos na lista")
            else:
                listar_alunos(alunos)

        elif opcao == "t":

            if not len(alunos) > 0:
                print("Não há alunos na lista")
            else:
                arquivo = input("Digite o nome do arquivo: ")
                arquivo += ".txt"

                if path.isfile(arquivo):
                    print("Arquivo já existe")
                else:
                    salvar_txt(arquivo, alunos)
                    print("Arquivo salvo com sucesso.")

        elif opcao == "c":

            if not len(alunos) > 0:
                print("Não há alunos na lista")
            else:
                arquivo = input("Digite o nome do arquivo: ")
                arquivo += ".csv"

                if path.isfile(arquivo):
                    print("Arquivo já existe")
                else:
                    salvar_csv(arquivo, alunos)
                    print("Arquivo salvo com sucesso.")

        elif opcao == "l":
            print("")
        elif opcao == "q":
            return
        else:
            print("")

        system("pause")


main()

import pandas as pd


def verificar_cidade(cidade):
    if cidade.lower() == "Foz Do Iguaçu":
        return "OK"
    else:
        return "Não"


# Leitura das planilhas
planilha1 = pd.read_excel('planilha1.xlsx')
planilha2 = pd.read_excel('planilha2.xlsx')

# Adicionando a coluna de verificação de cidade
planilha1['Cidade OK'] = planilha1['Cidade'].apply(verificar_cidade)
planilha2['Cidade OK'] = planilha2['Cidade'].apply(verificar_cidade)

# União das duas planilhas
uniao = pd.concat([planilha1, planilha2])

# Interseção das duas planilhas
intersecao = pd.merge(planilha1, planilha2, how='inner')

# Diferença da primeira planilha em relação à segunda
diferenca1 = planilha1[~planilha1.isin(planilha2)].dropna()

# Diferença da segunda planilha em relação à primeira
diferenca2 = planilha2[~planilha2.isin(planilha1)].dropna()

# Salvando as planilhas
uniao.to_excel('uniao.xlsx', index=False)
intersecao.to_excel('intersecao.xlsx', index=False)
diferenca1.to_excel('diferenca1.xlsx', index=False)
diferenca2.to_excel('diferenca2.xlsx', index=False)

print("Planilhas criadas com sucesso!")

import pandas as pd

planilha1 = "Planilha1.xlsx"
planilha2 = "Planilha2.xlsx"

# Lendo os dados das planilhas
df_planilha1 = pd.read_excel(planilha1, sheet_name="SeuNome")
df_planilha2 = pd.read_excel(planilha2, sheet_name="SeuNome")


def cidade_valida(cidade):
    if cidade.lower() == "Foz Do Iguaçu":
        return "OK"
    else:
        return "Não"


# Adicionando coluna "OK" para cidades na Planilha 1
df_planilha1["OK (Cidade)"] = df_planilha1["Cidade"].apply(cidade_valida)

# Adicionando coluna "OK" para cidades na Planilha 2
df_planilha2["OK (Cidade)"] = df_planilha2["Cidade"].apply(cidade_valida)

# Unindo as planilhas
df_uniao = pd.concat([df_planilha1, df_planilha2], ignore_index=True)

# Intersecção das planilhas
df_interseccao = df_planilha1.merge(
    df_planilha2, how='inner', on=['Nome', 'Email', 'CEP'])

# Diferença (Planilha 1)
df_diferenca1 = df_planilha1[~df_planilha1['Nome'].isin(df_planilha2['Nome'])]

# Diferença (Planilha 2)
df_diferenca2 = df_planilha2[~df_planilha2['Nome'].isin(df_planilha1['Nome'])]

# Nome das planilhas novas (substitua por nomes de sua preferência)
planilha_uniao = "Planilha_Uniao.xlsx"
planilha_interseccao = "Planilha_Interseccao.xlsx"
planilha_diferenca1 = "Planilha_Diferenca1.xlsx"
planilha_diferenca2 = "Planilha_Diferenca2.xlsx"

# Salvando as planilhas
df_uniao.to_excel(planilha_uniao, index=False)
df_interseccao.to_excel(planilha_interseccao, index=False)
df_diferenca1.to_excel(planilha_diferenca1, index=False)
df_diferenca2.to_excel(planilha_diferenca2, index=False)

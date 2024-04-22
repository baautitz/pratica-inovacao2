import pandas as pd
import requests

planilha_original = "Pessoas.xlsx"

# Lendo os dados da planilha
df_original = pd.read_excel(planilha_original, sheet_name="SeuNome")

# Criando colunas para logradouro, bairro, cidade e estado
df_original["Logradouro"] = ""
df_original["Bairro"] = ""
df_original["Cidade"] = ""
df_original["Estado"] = ""

for index, row in df_original.iterrows():

    if pd.notna(row["CEP"]):
        cep = row["CEP"]
        response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
        if response.status_code == 200:
            endereco = response.json()
            row["Logradouro"] = endereco["logradouro"]
            row["Bairro"] = endereco["bairro"]
            row["Cidade"] = endereco["localidade"]
            row["Estado"] = endereco["uf"]

planilha_final = "Resultado.xlsx"

# Salvando a planilha com as informações completas
df_original.to_excel(planilha_final, index=False)

import pandas as pd
import requests

# Função para obter os dados do CEP
def obter_dados_do_cep(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get('logradouro'), data.get('bairro'), data.get('localidade'), data.get('uf')
    else:
        return None, None, None, None


# Leitura da planilha original
planilha_original = pd.read_excel('planilha_original.xlsx')

# Adicionando os cabeçalhos para os novos dados
planilha_original['Logradouro'] = ''
planilha_original['Bairro'] = ''
planilha_original['Cidade'] = ''
planilha_original['Estado'] = ''

# Preenchendo os dados de endereço
for index, linha in planilha_original.iterrows():
    cep = linha['CEP']
    logradouro, bairro, cidade, estado = obter_dados_do_cep(cep)
    planilha_original.at[index, 'Logradouro'] = logradouro
    planilha_original.at[index, 'Bairro'] = bairro
    planilha_original.at[index, 'Cidade'] = cidade
    planilha_original.at[index, 'Estado'] = estado

# Salvando a planilha final
planilha_original.to_excel('planilha_final.xlsx', index=False)

print("Planilha final criada com sucesso!")

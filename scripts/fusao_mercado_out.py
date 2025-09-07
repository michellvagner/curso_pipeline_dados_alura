# %%
import json
import csv
from processamento_dados import Dados

#%%

# def leitura_json(path_json):
#     with open(path_json, 'r') as file:
#         dados_json = json.load(file)

#     return dados_json

# def leitura_csv(path_csv):
#     dados_csv = []
#     with open (path_csv, 'r') as file:
#         spamreader = csv.DictReader(file, delimiter=',')
        
#         for linha in spamreader:
#             dados_csv.append(linha)

#     return dados_csv

# def leitura_dados(path, tipo_arquivo):

#     if tipo_arquivo == 'csv':
#         dados = leitura_csv(path)
        

#     elif tipo_arquivo == 'json':
#         dados = leitura_json(path)

#     return dados

def identificar_colunas(dados):
    return list(dados[0].keys())

def renomear_colunas(dados, key_mapping):
    new_dados_csv = [{key_mapping.get(old_key): value for old_key, value in old_dict.items()} for old_dict in dados ]
    return new_dados_csv

def tamanho_arquivo(dados):
    return len(dados)

def fusao(dadosA, dadosB):
    combined_list = []
    combined_list.extend(dadosA)
    combined_list.extend(dadosB)
    return combined_list

def transformando_dados_tabela(dados, nomes_colunas):
    
    dados_combinados_tabela = [nomes_colunas]

    for row in dados:
        linha = [] 
        for coluna in nomes_colunas:
            linha.append(row.get(coluna, 'Indisponivel'))
        dados_combinados_tabela.append(linha)

    return dados_combinados_tabela

def salvando_dados(dados, caminho):
    with open(caminho, 'w') as file:
        writer = csv.writer(file)
        writer.writerows(dados)
#%%

path_json = '../data_raw/dados_empresaA.json'
path_csv = '../data_raw/dados_empresaB.csv'

dados_empresaA = Dados(path_json, 'json')
print(dados_empresaA.dados)

dados_empresaB = Dados(path_csv, 'csv')
print(dados_empresaB.dados)

# ## Iniciando leitura

# dados_json = leitura_dados(path_json, 'json')
# dados_csv = leitura_dados(path_csv, 'csv')
# tamanho_dados_json = tamanho_arquivo(dados_json)
# tamanho_dados_csv = tamanho_arquivo(dados_csv)

# nome_colunas_json = identificar_colunas(dados_json)
# nome_colunas_csv = identificar_colunas(dados_csv)

# # %%

# #Transformação dados

# key_mapping = {'Nome do Item': 'Nome do Produto', 
#                'Classificação do Produto': 'Categoria do Produto',
#                'Valor em Reais (R$)': 'Preço do Produto (R$)',
#                'Quantidade em Estoque': 'Quantidade em Estoque',
#                'Nome da Loja': 'Filial',
#                'Data da Venda': 'Data da Venda'
#                }

# dados_csv = renomear_colunas(dados_csv, key_mapping)
# nome_colunas_csv = identificar_colunas(dados_csv)
# print(f"Tamanho arquivos json: {tamanho_dados_json}")
# print(f"Tamanho arquivos csv: {tamanho_dados_csv}")

# dados_fusao = fusao(dados_csv, dados_json)
# nome_colunas_fusao = identificar_colunas(dados_fusao)
# tamanho_dados_fusao = tamanho_arquivo(dados_fusao)

# print(f"Tamanho arquivos fusao: {tamanho_dados_fusao}")

# # %%

# #Salvando dados

# dados_fusao_tabela = transformando_dados_tabela(dados_fusao, nome_colunas_fusao)

# path_dados_combinados = '../data_processed/dados_combinados.csv'

# salvando_dados(dados_fusao_tabela, path_dados_combinados)

# print(f'Arquivo salvo em: {path_dados_combinados}')

# %%

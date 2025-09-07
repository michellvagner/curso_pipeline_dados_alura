#%%
from processamento_dados import Dados

path_json = '../data_raw/dados_empresaA.json'
path_csv = '../data_raw/dados_empresaB.csv'

##Extração

dados_empresaA = Dados(path_json, 'json')
print(f'Os dados da empresaA: {dados_empresaA.nome_colunas} com {dados_empresaA.qtd_linhas} linhas.')

dados_empresaB = Dados(path_csv, 'csv')
print(f'Os dados da empresaB: {dados_empresaB.nome_colunas} com {dados_empresaB.qtd_linhas} linhas.')

##Transformação

key_mapping = {'Nome do Item': 'Nome do Produto', 
               'Classificação do Produto': 'Categoria do Produto',
               'Valor em Reais (R$)': 'Preço do Produto (R$)',
               'Quantidade em Estoque': 'Quantidade em Estoque',
               'Nome da Loja': 'Filial',
               'Data da Venda': 'Data da Venda'
               }

dados_empresaB.renomear_colunas(key_mapping)

print(f'Novos nomes de coluna da empresa B {dados_empresaB.nome_colunas}')

dados_fusao = Dados.fusao(dados_empresaA, dados_empresaB)
print(f'A junção dos dados trouxe as colunas: {dados_fusao.nome_colunas} e {dados_fusao.qtd_linhas} linhas retornadas')

##Carga

caminho_destino = '../data_processed/dados_combinados.csv'
dados_fusao.salvando_dados(caminho_destino)
print(f'Arquivo salvo em: {caminho_destino}')
#%%

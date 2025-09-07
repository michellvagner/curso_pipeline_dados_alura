import json
import csv

class Dados:

    def __init__(self, path, tipo_dados):
        self.path = path 
        self.tipo_dados = tipo_dados
        self.dados = self.leitura_dados()
        self.nome_colunas = self.identificar_colunas()
        self.qtd_linhas = self.tamanho_arquivo()

    def leitura_json(self):
        with open(self.path, 'r') as file:
            dados_json = json.load(file)

        return dados_json

    def leitura_csv(self):
        dados_csv = []
        with open (self.path, 'r') as file:
            spamreader = csv.DictReader(file, delimiter=',')
            
            for linha in spamreader:
                dados_csv.append(linha)

        return dados_csv

    def leitura_dados(self):

        if self.tipo_dados == 'csv':
            dados = self.leitura_csv()
            
        elif self.tipo_dados == 'json':
            dados = self.leitura_json()

        elif self.tipo_dados == 'list':
            dados = self.path
            self.path = 'lista em memoria'

        return dados
    
    def identificar_colunas(self):
        return list(self.dados[-1].keys())
    
    def renomear_colunas(self, key_mapping):
        new_dados_csv = [{key_mapping.get(old_key): value for old_key, value in old_dict.items()} for old_dict in self.dados ]
        
        self.dados = new_dados_csv
        self.nome_colunas = self.identificar_colunas()
        
    def tamanho_arquivo(self):
        return len(self.dados)
    
    def fusao(dadosA, dadosB):
        combined_list = []
        combined_list.extend(dadosA.dados)
        combined_list.extend(dadosB.dados)
        return Dados(combined_list, 'list')
    
    def transformando_dados_tabela(self):
    
        dados_combinados_tabela = [self.nome_colunas]

        for row in self.dados:
            linha = [] 
            for coluna in self.nome_colunas:
                linha.append(row.get(coluna, 'Indisponivel'))
            dados_combinados_tabela.append(linha)

        return dados_combinados_tabela
    
    def salvando_dados(self, caminho):

        dados_combinados_tabela = self.transformando_dados_tabela()

        with open(caminho, 'w') as file:
            writer = csv.writer(file)
            writer.writerows(dados_combinados_tabela)
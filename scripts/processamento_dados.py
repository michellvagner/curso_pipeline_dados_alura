import json
import csv

class Dados:

    def __init__(self, path, tipo_dados):
        self.path = path 
        self.tipo_dados = tipo_dados
        self.dados = self.leitura_dados()

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

        return dados
import pandas as pd
from tabulate import tabulate
import numpy as np

df = pd.read_excel(r"C:\Users\Lucas Santos\OneDrive\Desktop\ProjetoPython\Projeto_Investimento\Dados_forte_investimento.xlsx")

#Correção de nomes e sobrenomes
df.loc[df['id_funcionario'] == 3, "sobrenome"] = "Oliveira"
df.loc[df['id_funcionario'] == 7, 'sobrenome'] = "Ferreira"
df.loc[df['id_funcionario'] == 16, 'sobrenome'] = "Texeira"
df.loc[df['id_funcionario'] == 31, 'nome'] = "Brendo"
df.loc[df['id_funcionario'] == 37, 'sobrenome'] = "Costa"
df.loc[df['id_funcionario'] == 44, 'nome'] = "James"
df.loc[df['id_funcionario'] == 30, 'nome'] = "Beatriz"
df.loc[df['id_funcionario'] == 3, 'sobrenome'] = "Oliveira"



#Correção de idades
df.loc[df['id_funcionario'] == 4, 'idade'] = 33
df.loc[df['id_funcionario'] == 7, 'idade'] = 28
df.loc[df['id_funcionario'] == 16, 'idade'] = 26
df.loc[df['id_funcionario'] == 20, 'idade'] = 31
df.loc[df['id_funcionario'] == 24, 'idade'] = 26
df.loc[df['id_funcionario'] == 32, 'idade'] = 29
df.loc[df['id_funcionario'] == 36, 'idade'] = 26
df.loc[df['id_funcionario'] == 37, 'idade'] = 25
df.loc[df['id_funcionario'] == 38, 'idade'] = 24

#Correção mais rápida de idades
df.loc[df['id_funcionario'].isin([39, 40, 41, 42, 45]), 'idade'] = [25, 25, 36, 29, 46]





# Exibir id_funcionario, nome, sobrenome e idade.
#print(tabulate(df[['id_funcionario', 'Leads Parados']], headers='keys', tablefmt='grid'))

#localizando e corrigindo a coluna Leads Parados
df.loc[df['Leads Parados'].isnull()]
#print(tabulate(df.loc[df['Leads Parados'].isnull(), ['id_funcionario', 'Leads Parados']], headers='keys', tablefmt='grid'))

df.loc[df['id_funcionario'].isin([20,25,45]), 'Leads Parados'] = [216, 246, 184]
#print(tabulate(df[['id_funcionario', 'Leads Recebidos', 'Leads Parados', 'conversão de lead']], headers='keys', tablefmt='grid'))

#Exclusão da conluna conversão de leads, é melhor excluir e fazer uma nova
df = df.drop('conversão de lead', axis=1)
#print(tabulate(df[['id_funcionario', 'Leads Recebidos', 'Leads Parados']], headers='keys', tablefmt='grid'))

df['Conversão Leads'] = df['Leads Recebidos'] - df['Leads Parados']

#print(tabulate(df[['id_funcionario', 'Leads Recebidos','Leads Parados']], headers='keys', tablefmt='grid'))
#print(tabulate(df[['id_funcionario', 'fat_1° trimestre']]))

df.loc[df['id_funcionario'].isin([15, 33]), 'fat_1° trimestre'] = [64545.01, 65884.06]

#print(tabulate(df, headers= 'keys', tablefmt= 'grid'))
#print(tabulate(df[['id_funcionario', 'Leads Recebidos', 'Leads Parados', 'conversão de lead']], headers='keys', tablefmt='grid'))

print(tabulate(df[['fat_1° trimestre', 'fat_2° trimestre', 'fat_3° trimestre', 'fat_4° trimestre']], headers= 'keys', tablefmt= 'grid'))
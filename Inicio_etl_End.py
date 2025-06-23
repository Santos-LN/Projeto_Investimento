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



df.loc[df['id_funcionario'].isin([5,21,30]), ['fat_2° trimestre']] = [131504.05,132558.02, 140147.06]


df.loc[df['id_funcionario'].isin([3,11,24]), ['fat_3° trimestre']] = [191004, 192300,194210]


# id 9

df.loc[df['id_funcionario'].isin([9,44]), ['fat_4° trimestre']] = [165222, 165222]

#quero excluir a coluna comissão anual e criar uma nova, a Comissão_Anual, nela preciso do valo de 25% do somatorio dos 4 trimesntres
# Exclui a coluna 'comissão Anual'
#df = df.drop('comissão Anual', axis=1)

# Cria a nova coluna 'Comissão_Anual' com 25% do somatório dos 4 trimestres
df['Comissão_Anual'] = (df['fat_1° trimestre'] + df['fat_2° trimestre'] + df['fat_3° trimestre'] + df['fat_4° trimestre']) * 0.25

# print(tabulate(df[['id_funcionario', 'fat_2° trimestre', 'fat_3° trimestre', 'fat_4° trimestre', 'Comissão_Anual']], headers= 'keys', tablefmt= 'grid'))
# print(tabulate(df, headers= 'keys', tablefmt= 'grid'))

df.loc[df['id_funcionario'].isin([20,25,45]), ['Clientes Premium']] = [55,56,50]
# df = df.drop('Clientes_Gold', axis=1)


df['Clientes_Gold'] = df['Conversão Leads'] - df['Clientes Premium']

# print(tabulate(df[['id_funcionario','Clientes Premium', 'Clientes_Gold']], headers= 'keys', tablefmt= 'grid'))

print(df.columns)

#Definindo a ordem das colunas
ordem_colunas = [
    'id_funcionario', 
    'nome', 
    'sobrenome', 
    'idade', 
    'Cargo', 
    'dia de admissão', 
    'Leads Recebidos', 
    'Leads Parados', 
    'Conversão Leads', 
    'fat_1° trimestre', 
    'fat_2° trimestre', 
    'fat_3° trimestre', 
    'fat_4° trimestre', 
    'Comissão_Anual',
    'Clientes Premium',
    'Comissão_Anual'
]

# Reorganizando as colunas
df = df[ordem_colunas]


# print(df.columns)

# print(tabulate(df, headers= 'keys', tablefmt= 'grid'))

df.to_excel(r"C:\Users\Lucas Santos\OneDrive\Desktop\ProjetoPython\Projeto_Investimento\Dados_forte_investimento_editado.xlsx", index=False)

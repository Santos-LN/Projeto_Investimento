import pandas as pd
from tabulate import tabulate
import numpy as np

df = pd.read_excel(r"C:\Users\Lucas Santos\OneDrive\Desktop\ProjetoPython\Projeto_Investimento\Dados_forte_investimento.xlsx")

df = df[['id_funcionario', 'nome','sobrenome', 'idade']]


df.loc[df['id_funcionario'] == 3, "sobrenome"] = "Oliveira"


df.loc[df['id_funcionario'] == 7, 'sobrenome'] == "Ferreira"
df.loc[df['id_funcionario'] == 16, 'sobrenome'] == "Texeira"
df.loc[df['id_funcionario'] == 31, 'nome'] == "Brendo"
df.loc[df['id_funcionario'] == 37, 'sobrenome'] == "Costa"
df.loc[df['id_funcionario'] == 44, 'nome'] == "James"
df.loc[df['id_funcionario'] == 30, 'nome'] == "Beatriz"
print(tabulate(df, headers= 'keys', tablefmt= 'grid'))

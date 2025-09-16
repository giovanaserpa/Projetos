import pandas as pd

tabela = pd.read_csv("cancelamentos_sample.csv") #importar tabela 

tabela = tabela.drop(columns="CustomerID")
display(tabela) #visualizar tabela

display(tabela.info())
tabela = tabela.dropna() #remover linhas com dados faltantes

display(tabela.info())

display(tabela["cancelou"].value_counts()) # quantidade de pessoas que cancelaram e que não cancelaram

display(tabela["cancelou"].value_counts(normalize=True)) # porcentagem de pessoas que cancelaram

import plotly.express as px


for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color="cancelou")
    
    grafico.show()
    
tabela = tabela[tabela["duracao_contrato"]!="Mensal"]
tabela = tabela[tabela["ligacoes_callcenter"]<=4]
tabela = tabela[tabela["dias_atraso"]<=20]

display(tabela["cancelou"].value_counts())

display(tabela["cancelou"].value_counts(normalize=True))

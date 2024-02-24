import pandas
import plotly.express as px

tabela =  pandas.read_csv("cancelamentos (1).csv")

tabela = tabela.drop(columns=["CustomerID", "idade", "sexo"])
print(tabela)
print(tabela.info)
tabela  = tabela.dropna()
print(tabela["cancelou"].value_counts())
print(tabela["cancelou"].value_counts(normalize=True))

for coluna in tabela.columns:

    grafico = px.histogram(tabela, x=coluna , color="cancelou")
    grafico.show()
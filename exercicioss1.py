import pandas as pd #importar a biblioteca que sera chamada pelo apelido "pd"

dados = { #dicionario que será transformado em um dataframe
'cargos': ["assistentes", "auxiliar", "gerente"],
'salario': [2500, 3000, 6000]
}

dados_pi = pd.DataFrame(dados) #.DataFrame é o comando para criar o dataframe (a partir de algum dado)

#print(dados_pi.head(2))
#print(dados_pi.tail(2)) 
#print(dados_pi.shape) #mostra as linhas e colunas
#print(dados_pi.info()) #mostrar informações do dataframe
print(dados_pi.describe)
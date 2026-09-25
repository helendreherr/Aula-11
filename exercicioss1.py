#import pandas as pd #importar a biblioteca que sera chamada pelo apelido "pd"

#dados = { #dicionario que será transformado em um dataframe
#'cargos': ["assistentes", "auxiliar", "gerente"],
#'salario': [2500, 3000, 6000]
#}

#dados_pi = pd.DataFrame(dados) #.DataFrame é o comando para criar o dataframe (a partir de algum dado)

#print(dados_pi.head(2))
#print(dados_pi.tail(2)) 
#print(dados_pi.shape) #mostra as linhas e colunas
#print(dados_pi.info()) #mostrar informações do dataframe
#print(dados_pi.describe)



################## exercicio 2

# import pandas as pd

# dados = [
#     {"título": "A ameaça fantasma", "ano": 1999, "trilogia": 2, "nota": 6.5, "ranking": 356},
#     {"título": "Ataque dos Clones", "ano": 2002, "trilogia": 2, "nota": 6.6, "ranking": 874},
#     {"título": "A vingança dos sith", "ano": 2005, "trilogia": 2, "nota": 7.6, "ranking": 808},
#     {"título": "Uma nova esperança", "ano": 1977, "trilogia": 1, "nota": 8.6, "ranking": 188},
#     {"título": "Uma nova esperança", "ano": 1977, "trilogia": 1, "nota": 8.6, "ranking": 188},
# ]

# dados2 = pd.DataFrame(dados)

# print(dados2.head())

########## exercicio 3

import pandas as pd

dados = {"nome" : ["patrick", "marcio", "fabio", "thomas", "sergio"],
        "matricula" : [545213, 745697, 65214, 644852, 548634],
        "endereço":  ["Rio de Janeiro", "São Paulo", "recife", "Bahia", "Minas Gerais"]}

dados2 = pd.DataFrame(dados)
print(dados2.head(3))
print(dados2.tail(3))

# Universidade Federal de Santa Catarina
# Engenharia Aeroespacial

import math

def dp(v):
    
    #Recebe um conjunto de números e retorna a média e o desvio padrão
    

    n = len(v)       # quantidade de termos 
    dp = 0           # desvio padrao
    soma = 0         # soma dos termos      
    somatorio = 0    # soma o quadrado da diferença
    media = soma/n
    
    for i in v:
        soma += i             # soma os valores
        media = soma/n        # divide a soma pela quantidade de termos
    for i in v:
        x = math.pow((i - media), 2)  # (cada valor menos a media) ao quadrado
        somatorio += x                # somatorio do passo anterior

    dp = round(math.sqrt(somatorio / (n-1)),2) # calcula o desvio padrão c/ 2 decimais
    
    var = round((somatorio / (n-1)),2)        #calcula variancia
    
    print(' ')
    print(' Média    DP   Variancia ')
    
    return media,   dp,   var

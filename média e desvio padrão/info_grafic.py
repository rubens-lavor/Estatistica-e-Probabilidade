from estatistica import dp
import matplotlib.pyplot as plt
import math


#-----------------------------------------------------------------------------
# Abre arquivo .txt e lê os dados

abrir = open('data.txt') 
ler = [float(n) for n in abrir.readlines()]
print(dp(ler))

#-----------------------------------------------------------------------------
# Separador
print(' ------------------'*4)
#-----------------------------------------------------------------------------
# Colocar os dados em ordem crescente

ler.sort(key=int)
print('Dados em ordem crescente:')
print(ler)

#-----------------------------------------------------------------------------
# Verificando 2º quartil (mediana)

mediana = (len(ler) + 1) / 2

if mediana %5:
    x = int(mediana + 0.5)
    y = int(mediana - 0.5)
else:
    mediana = (len(ler) + 1) / 2
mediana =( ler[x-1] + ler[y-1] )/ 2
print(' ')

#-----------------------------------------------------------------------------
# Verificando 1º quartil

quartil1 = (len(ler) +1) / 4
teste1 = quartil1 / 2

if teste1 % 1:
    q = math.ceil(quartil1)    
else:
    q = (int(quartil1))
q1 = ler[q-1]

#-----------------------------------------------------------------------------
# Verificando 3º quartil

quartil3 = (3*(len(ler)+1)) / 4
teste3 = quartil3 / 2

if teste3 % 1:
    qqq = math.ceil(quartil3)
else:
    qqq = (int(quartil3))
q3 = ler[qqq-1]

#-----------------------------------------------------------------------------
# Separador
print(' ------------------'*4)
#-----------------------------------------------------------------------------

print('1º quartil: {}'.format(q1))
print('2º quartil: (mediana): {}'.format(mediana))
print('3º quartil: {}'.format(q3))

#-----------------------------------------------------------------------------
# Separador
print(' ------------------'*4)
#-----------------------------------------------------------------------------
# Classe do histograma

kk = len(ler)                           #calcula a classe para o histograma
k = math.ceil(math.sqrt(kk))            #arredonda para cima

amplitude = (ler[39]-ler[0])
classe = amplitude / k
teste4 = classe /2
if teste4 % 1:
    cl = math.ceil(classe)
    classe = cl
else:
    cl = int(math.ceil(classe))
    classe = cl
print('A classe do seu histograma é: {} '.format(classe))
print('Amplitude: {}'.format(amplitude))
print('Colunas = {}'.format(k))

#-----------------------------------------------------------------------------
# Plotar Gráfico

plt.title('gráfico do maurício', fontsize=20)
plt.xlabel('Tempo (ms)', fontsize=15)
plt.ylabel('Frequência Absoluta', fontsize=15)
plt.tick_params(labelsize=15)
plt.hist(ler, 7, rwidth=1, color='b', alpha=0.8, edgecolor='black')
plt.axis((90,300,0,20))
plt.show()

#-----------------------------------------------------------------------------
'''
font_1 = {'family': 'serif', 'color': 'darkred', 'size':'14'}

plt.figure(figsize=(8, 10))
plt.boxplot(ler)
plt.title('Boxplot Tempos')
plt.ylabel('Altura')
plt.text(1, q1, fontdict=font_1)
plt.text(1, mediana, fontdict = font_1)
plt.text(1, q2, fontdict = font_1)
plt.show()
'''
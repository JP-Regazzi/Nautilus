#Q3
# Analisando o crescimento de maneiras que podemos juntar dinheiro com moedas, é perceptível o seguinte padrão:
#  -Utilizando apenas moedas de 1 centavo, somente existe uma maneira de juntar dinheiro, para qualquer quantia
#  -Utilizando outras moedas, o numero de possibilidades aumenta segundo a formula:
#    -> num_maneiras = num_maneiras com moedas menores + num_maneiras com moedas menores ou iguais para o (dinheiro atual - valor da moeda)
#  - Podemos escrever isso de forma matematica, i sendo o dinheiro juntado e j uma moeda
#    -> tabela[i][j] = tabela[i][j-1] + tabela[i-moedas[j]][j]

def ManeirasEconomizar(x):
    moedas = [1, 2, 5, 10, 20, 50, 100, 200]
    tabela = []
    for i in range(x+1):
        tabela.append([1, 0, 0, 0, 0, 0, 0, 0] )
    for j in range(1, 8):
        for i in range(x+1):
            tabela[i][j] = tabela[i][j-1] + tabela[i-moedas[j]][j]
    return tabela[-1][-1]
    
print(f'Existem {ManeirasEconomizar(200)} maneiras de juntar 200 centavos com as moedas dadas')



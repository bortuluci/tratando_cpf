# Crie um programa capaz de gerar um cpf válido e imprimir na tela para o usuario
#E tambem criar um validador de cpf caso o usuario insira o próprio cpf para verificar se é válido
'''--------------------------------------------------------------------------
Ex: CPF = 168.995.350-09
1 * 10 = 10                 #   1 * 11 = 11             #CALCULO PARA VALIDAR CPF
6 * 9  = 54                 #   6 * 10 = 11             # 1 coluna soma os 9 primeiros digitos do CPF
8 * 8  = 64                 #   8 * 9  = 11             # Como na conta da coluna a esquerda
9 * 7  = 63                 #   9 * 8  = 11             # Com a formula na parte de baixo o resultado será o penultimo Numero do CPF
9 * 6  = 54                 #   9 * 7  = 11             # Agora você repete a mesma conta mas com o 10 numeros que
5 * 5  = 25                 #   5 * 6  = 11             # na segunda coluna para descobrir o ultimo digito
3 * 4  = 12                 #   3 * 5  = 11
5 * 3  = 15                 #   5 * 4  = 11
0 * 2  = 0                  #   0 * 3  = 11
                            #   0 * 2  = 11

    297                          343
11 - (297 % 11) = 11            11 - (343 % 11) = 9
11>9 = 0                        Digito 2 = 9            
Digito 1 = 0
'''



#random.randint     loop para gerar cpf

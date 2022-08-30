#GERADOR
import random

cpf = random.randint(00000000000,99999999999)

while len(str(cpf)) < 11:
  cpf = '0' + str(cpf)
cpf = int(cpf)
print(f'CPF gerado: {cpf}')

#Caso queira informar um CPF, comente tudo que estiver acima dessa linha e descomente a linha abaixo
# cpf=int(input('Informe um CPF para verificação: '))

#VALIDAÇÃO
if  len(str(cpf)) == 11:
#pegar os 9 primeiros digitos do CPF multiplicá-los de 10 a 2, soma os resultados, fazer resultadoMulti*10/11 == o 10º digito
  resultadoMulti = 0
  cpf = str(cpf)
  for i in range(0,9):
    resultadoMulti = resultadoMulti + int(cpf[i])*(10-i)

  if (resultadoMulti*10)%11 == int(cpf[9]):
    resultadoMulti = 0
    for i in range(0, 10):
      resultadoMulti = resultadoMulti + int(cpf[i])*(11-i)
      print(resultadoMulti)

    #verificar se a conta a partir do digito 11 é válida
    if (resultadoMulti*10)%11 == int(cpf[10]):
      print('CPF Válido! \o/ ')
    else:
      print('CPF inválido!')
  else:
    print('CPF inválido!')
else:
  print('CPF inválido!')


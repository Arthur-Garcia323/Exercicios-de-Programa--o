
##Calcualadora

escolha_operação=input('Escolha uma operação? (soma/subtração/multiplicação/divisão): ')

num1=float(input('Digite um numero:'))
num2=float(input('Digite um numero:'))

if escolha_operação == 'soma':
    resultado = num1 + num2
    print('O resultado da soma é:', resultado)

elif escolha_operação == 'subtração':
    resultado = num1 - num2
    print('O resultado da subtração é:', resultado)

elif escolha_operação == 'multiplicação':
    resultado = num1 * num2
    print('O resultado da multiplicação é:', resultado)

elif escolha_operação == 'divisão':
   if num2 != 0:
      resultado = num1 / num2
      print('O resultado da divisão é:', resultado)
   else:
      print('Erro: divisão por zero')

else:
  print('Operação invalida.')

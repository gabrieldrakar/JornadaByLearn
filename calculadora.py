primeiro_numero = float(input('insira o primeiro numero '))
segundo_numero = float(input('insira o segundo numero '))
operacao = input('você deseja somar, dividir, multiplicar ou subtrair? ')

if operacao.lower() == 'somar':
  print(primeiro_numero + segundo_numero)
elif operacao.lower() == 'subtrair':
   print(primeiro_numero - segundo_numero)
elif operacao.lower() == 'dividir':
   print(primeiro_numero / segundo_numero)
elif operacao.lower() == 'multiplicar':
   print(primeiro_numero * segundo_numero)
else:
  print('erro')
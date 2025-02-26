print('Calculadora simples')

num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))
opcao = input('Digite a operação (+,-,*,/): ')

if opcao == '+':
    resultado = num1 + num2
elif opcao == '-':
    resultado = num1 - num2
elif opcao == '*':
    resultado = num1 * num2
elif opcao == '/':
    resultado = num1 / num2
elif num2 != 0:
    print('Erro na divisão por zero')
    resultado = None
else:
    print('operação invalida')
    resultado = None
if resultado is not None:
    print(f'Resultado: {resultado}')


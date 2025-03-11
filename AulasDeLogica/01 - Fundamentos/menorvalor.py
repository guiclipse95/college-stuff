
# entrada de dados

num1 = int(input('Digite um numero: '))
num2 = int(input('Digite o segundo numero: '))
num3 = int(input('Digite o terceiro numero: '))

# saida de dados

if num1 <= num2 and num1 <= num3:
    print(f'O menor valor foi: {num1}') # O primeiro valor será  menor

elif num2 <= num1 and num2 <= num3:
    print(f'O menor valor foi: {num2}') # O segundo valor será menor

elif num3 <= num1 and num3 <= num2:
    print(f'O menor valor foi: {num3}') # O terceiro valor será menor
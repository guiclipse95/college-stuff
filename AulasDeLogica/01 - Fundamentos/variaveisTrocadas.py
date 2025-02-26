var1 = input('Digite a primeira variavel: ')
var2 = input('Digite a segunda variavel: ')


var_auxiliar = var1
var1 = var2
var2 = var_auxiliar

print(f'Variavel 1: {var1}')
print(f'Variavel 2: {var2}')
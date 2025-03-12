nome = input('Informe um nome: ')
quant_vogais = 0

for vogal in nome:
    if vogal in 'aeiouAEIOU':
        quant_vogais += 1

print(f'A palavra tem {quant_vogais} vogais')
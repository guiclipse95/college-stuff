nome = input('Informe um nome: ')
quant_vogais = 0
quant_conso = 0

# Processamento para indentificar as vogais e consoantes!

for vogal in nome:
    if vogal in 'aeiouAEIOU':
        quant_vogais += 1

for consoante in nome:
    if consoante in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
        quant_conso += 1

# Saida dos dados

print(f'A palavra tem {quant_vogais} vogais e {quant_conso} consoantes!')
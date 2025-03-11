
# Entrada de dados

renda_anual = float(input('Digite sua renda anual: '))
quant_dependentes = int(input('Digite a quantidade de dependentes: '))

# Processamento de dados

percentual_desconto = quant_dependentes * 2
valor_desconto = (renda_anual / 100) * percentual_desconto
renda_liquida = renda_anual - valor_desconto

# Saida de dados

if renda_liquida <= 2000:
    print('Isento de imposto de renda')

elif renda_liquida >= 2000 and renda_liquida <= 5000:
    valor_imposto = renda_liquida * 0.05
    print(f'O imposto a pagar é: {valor_imposto:.2f}')

elif renda_liquida > 5000 and renda_liquida <= 10000:
    valor_imposto = renda_liquida * 0.10
    print(f'Imposto a pagar é: {valor_imposto:.2f}')

else:
    valor_imposto = renda_liquida * 0.15
    print(f'Imposto a pagar é: {valor_imposto:.2f}')
import os

os.system("clear")

quant_produtos = int((input('Dgite a quantidade de produtos: ')))

caixa_extra = 0
caixa_grande = 0
caixa_media = 0
caixa_pequena = 0
total = quant_produtos

while quant_produtos != 0:
    
    if quant_produtos >= 50:
        caixa_extra += 1
        quant_produtos -= 50
    
    elif quant_produtos >= 20:
        caixa_grande += 1
        quant_produtos -= 20        
    
    elif quant_produtos >= 5:
        caixa_media += 1
        quant_produtos -= 5
    
    elif quant_produtos >= 1:
        caixa_pequena += 1
        quant_produtos -= 1

print('-' * 20)
print('Logistica de Entraga')
print('-' * 20)

print(f'Total:        {total}')
print(f'Extragrande:  {caixa_extra}')
print(f'Grande:       {caixa_grande}')
print(f'Media:        {caixa_media}')
print(f'Pequena:      {caixa_pequena}')

print('-' * 20)



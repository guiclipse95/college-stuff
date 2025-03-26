
contador = 1
menor_nota = None
maior_nota = None
soma_notas = 0

while contador <= 6:
    nota = float(input(f'Informe a nota {contador}.: '))
    soma_notas += nota

    if contador == 1:
        menor_nota = nota
        maior_nota = nota
    else:
        if nota < menor_nota:
            menor_nota = nota

        elif nota > maior_nota:
            maior_nota = nota


    contador += 1



media = (soma_notas - menor_nota - maior_nota) / 4

print(f'A media do atleta foi: {media:.1f}')
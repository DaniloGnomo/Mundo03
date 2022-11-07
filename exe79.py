lista = list()
qtnum = 0
while True:
    num = int(input('Digite um valor: '))
    if num in lista:
        print(f'Valor {num} já foi digitado não será adicionado a lista!')
        conti = input('Quer continuar [S/N] ? ').upper()
        if conti not in 'SN':
            conti = input('Faça uma escolha valida [S/N] ').upper()
        elif conti == 'N':
            break
    else:
        print(f'Adicionando numero {num} a lista!')
        lista.append(num)
        qtnum += 1
        conti = input('Quer continuar [S/N] ? ').upper()
        if conti not in 'SN':
            conti = input('Faça uma escolha valida [S/N] ').upper()
        elif conti == 'N':
            break
print(f'Foram digitados {qtnum} numeros,\n'
      f'Seus numeros foram {lista}\n'
      f'Os numeros de forma ordenada {sorted(lista)}')

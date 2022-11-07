lista = list()
qtnum = 0
while True:
    num = int(input('Digite um valor: '))
    conti = input('Quer adicionar outro valor [S/N] ? ').upper()
    if conti not in 'SN':
        print('Escolha uma opção correta entre S ou N')
        conti = input('Qual a sua escolha ? ')
    elif conti == 'S':
        lista.append(num)
        qtnum += 1
    elif conti == 'N':
        break
print(f'Você digitou {qtnum} valores')
print('O valores em ordem decrescente foram', sorted(lista, reverse=True))
if 5 in lista:
    print('O valor 5 esta na lista')
else:
    print('O valor 5 não esta na lista')

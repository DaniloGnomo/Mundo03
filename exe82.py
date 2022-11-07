listag = list()
listai = list()
listap = list()
while True:
    num = int(input('Digite um valor inteiro: '))
    listag.append(num)
    if num % 2 == 0:
        listap.append(num)
    else:
        listai.append(num)
    conti = input('Quer continuar [S/N] ?').upper()
    if conti not in 'SN':
        conti = input('Faça uma escolha valida entre S ou N: ').upper()
    elif conti == 'N':
        break
print(f'A lista de valores que você digitou foi: {listag}')
print(f'Os Numeros impares são: {listai}')
print(f'Os numeros pares são: {listap}')



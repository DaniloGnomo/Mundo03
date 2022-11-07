num = list()
listaim = list()
listapa = list()
while True:
    num.append(int(input('Digite um valor inteiro: ')))
    conti = input('Quer continuar [S/N] ? ').upper()
    if conti not in 'SN':
        conti = input('Quer continuar [S/N] ? ')
    elif conti == 'N':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        listapa.append(v)
    elif v %2 == 1:
        listaim.append(v)
print(f'A lista contem os valores: {num}\n'
      f'O valores ímpares são: {listaim}\n'
      f'E os valores pares são: {listapa}')

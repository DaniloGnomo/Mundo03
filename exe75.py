num = (int(input('Digite o primeiro valor: ')),\
     int(input('Digite o segundo valor: ')),\
     int(input('Digite o terceiro valor: ')),\
     int(input('Digite o quarto valor: ')))

print(f'Os numeros digitados são: {num}')
if 9 in num:
    print(f'O Numero 9 apareceu {num.count(9)} vezes')
else:
    print('O numero 9 não foi digitado')
if 3 in num:
    print(f'O numero 3 apareceu na {num.index(3)+1}ª posição')
else:
    print('O numero 3 não foi digitado')
print('Os Numeros Pares são: ', end='')
for c in num:
    if c % 2 == 0:
        print(c, end=', ')

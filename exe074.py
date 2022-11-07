from random import randint
num = randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10)
mr = mn = sorted(num)
print(f'Os números sorteados foram: {num}')
print('O maior numero foi:', mr[-1])
print('O menor numero foi:', mn[0])

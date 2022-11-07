num = list()
for pos in range(0, 5):
    num.append(int(input(f'Digite um valor para posição {pos}: ')))
print(f'Os numeros digitados foram {num}')
print(f'O maior numero é: {max(num)} e está na posição: ', end='')
for i, v in enumerate(num):
    if v == max(num):
        print(f'{i}...', end='')
print(f'\nO menor numero é: {min(num)} e está na posição: ', end='')
for i, v in enumerate(num):
    if v == min(num):
        print(f'{i}...', end='')

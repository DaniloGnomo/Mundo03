lista = list()
for c in range(0, 5):
    num = int(input(f'Digite o {c} numero: '))
    if c == 0 or num > lista[-1]:
        lista.append(num)
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                break
print(lista)

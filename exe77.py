vogais = 'bala', 'bola', 'cachorro', 'dente', 'televisao', 'radio', 'ovo', 'geladeira', 'trabalho', 'picole'
for p in vogais:
    print(f'\nA Palavra {p.upper()} tem as vogais: ', end='')
    for v in p:
        if v.lower() in 'aeiou':
            print(v, end=' ')


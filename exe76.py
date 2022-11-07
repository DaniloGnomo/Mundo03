tabela = 'Alho', 1.00, 'Batata', 3.00, 'Chocolate', 2.00, 'Danone', 4.00, 'Ervilha', 3.75, 'Frango', 17.00
print('=*='*5, 'TABELA DE PREÇOS', '=*='*5)
print('=*='*16)
for form in range(0, len(tabela)):
    if form % 2 == 0:
        print(f'{tabela[form]:.<38}', end='')
    else:
        print(f'R${tabela[form]:_>8.2f}')

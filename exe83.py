qpa = 0
qpb = 0
expre = str(input('Digite sua expressão usando parentes ?'))
for c in range(len(expre)):
    c += 1
    for i, d in enumerate(expre):
        if d == '(':
            qpa += 1
        if d == ')':
            qpb += 1

if qpa == qpb:
    print('A expressão é valida')
else:
    print('A expressão não é valida')


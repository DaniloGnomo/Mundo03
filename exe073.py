times = 'Palmeiras', 'Internacional', 'Flamengo', 'Fluminense', 'Corinthians', 'Athletico PR', 'Atletico MG',\
        'São Paulo', 'Fortaleza', 'Botafogo', 'América MG', 'Santos', 'Goias', 'Bragantino', 'Coritiba', 'Cuiaba',\
        'Ceara', 'Atlético GO', 'Avaí', 'Juventude'
print(f'Colocação atual do times em 01/11/22: {times}')
print('=-='*35)
print(f'Os cinco primeiros são: {times[:5]}')
print('=-='*35)
print(f'Os ultimos 4 colocados são: {times[-4:]}')
print('=-='*35)
print(f'Lista em ordem Alfabetica: {sorted(times)}')
print('=-='*35)
print(f'O time do São Paulo está em: {times.index("São Paulo")+1}º lugar')
print('=-='*35)
c = 0
for time in range(0, 20):
        c += 1
        print('\33[1;34m', c, times[time])
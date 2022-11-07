listn = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', \
      'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte'
num = int(input('Escolha um numero de 0 até 20: '))
while True:
    if num < 0 or num > 20:
        print('Faça uma escolha correta de 0 até 20: ')
        num = int(input('Sua escolha: '))
    else:
        print(f'O número {num} em extenso é: {listn[num]}')
        break

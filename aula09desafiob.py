numero = input('Digite um número: ')

if len(numero) == 4:  # Verifica se o número tem 4 dígitos
    milhar = numero[0:1]
    print('Milhar: {}'.format(milhar))
    centena = numero[1:2]
    print('Centena: {}'.format(centena))
    dezena = numero[2:3]
    print('Dezena: {}'.format(dezena))
    unidade = numero[3:4]
    print('Unidade: {}'.format(unidade))
else:
    print('Por favor, digite um número de 4 dígitos.')

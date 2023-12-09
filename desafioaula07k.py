d = int(input('Você alugou o carro por quantos dias?'))
k = int(input('Quantos km você rodou com o carro?'))
di = d*60
km = k*0.15
print('O total a pagar é {}R$'.format(di+km))
n1 = int(input('Um valor'))
n2 = int(input('Outro valor'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
d1 = n1 // n2
e = n1 ** n2
print('A soma é {}, o produto é {}, a divisão é {:.3f}'.format(s, m, d),end=' ')
print('a divisão inteira {} e a potência {}'.format(d1, e))
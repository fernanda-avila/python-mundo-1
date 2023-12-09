import math
cat1 = int(input('Comprimento do cateto oposto:'))
cat2 = int(input('Comprimento do cateto adjacente'))

print('O comprimento da hipotenusa desse triângulo retângulo é {:.3f}'.format(math.hypot(cat1,cat2)))

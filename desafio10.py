d = float(input(' Quanto de dinheiro voce tem na carteira? R$ '))
print(' legal!! voce tem {} reais de dinheiro na carteira! '.format(d))
print('vamos converter em dolares?')
c = float(input('qual a cotação do dolar hoje? '))
s = d / c
print('convertendo, voce tem US${} dolares na carteira'.format(s))
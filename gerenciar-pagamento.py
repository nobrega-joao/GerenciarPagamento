print('{:=^40}' .format(' WALLMART '))
compras = float(input('\033[1mValor das compras: R$\033[m'))
print('''\033[32mFORMAS DE PAGAMENTO
[ 1 ] À vista dinheiro/cheque
[ 2 ] À vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão\033[m''')
opção = int(input('\033[1mQual é a opção? \033[m'))

if opção == 1:
    desconto = compras - (compras * 10) / 100
    print('Sua compra de R${:.2f} irá custar \033[1mR${:.2f}\033[m com os 10% de desconto.' .format(compras, desconto))
elif opção == 2:
    desconto = compras - (compras * 5) / 100
    print('Sua compra de R${:.2f} irá custar \033[1mR${:.2f}\033[m com os 5% de desconto.'.format(compras, desconto))
elif opção == 3:
    parcelas = compras / 2
    print('Sua compra será dividida em 2x de R${:.2f}' .format(parcelas))
    print('Sua compra irá custar \033[1mR${:.2f}\033[m' .format(compras))
elif opção == 4:
    parcelas = int(input('\033[1mQuantas parcelas? \033[m'))
    juros = compras + (compras * 20) / 100
    preço = juros / parcelas
    print('Sua compra será parcelada em {}x de R${:.2f}' .format(parcelas, preço))
    print('Sua compra de R${:.2f} irá custar \033[1mR${:.2f}\033[m com os 20% de juros.' .format(compras, juros))
else:
    print('\033[1;31mOpção inválida!\033[m')

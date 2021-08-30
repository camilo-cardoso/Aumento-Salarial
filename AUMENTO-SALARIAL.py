"""

salários até R$ 1600,00 aumento de 20%
salários entre R$ 1600,00 e R$ 2000,00 : aumento de 15%
salários entre R$ 2000,00 e R$ 2800,00 : aumento de 10%
salários de R$ 2800,00 em diante : aumento de 5% 

o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.
"""
while True:

    print('======================Calculo aumento Salarial=================')
    print()
    sl1 = float(input('digite seu salario ? R$ '))

    print('======================================================================')
    if sl1 <= 1600:
        nv1 = sl1+(sl1*20/100)
        nv2 = nv1-sl1
        print(f'Seu salario antes do reajuste erá R${sl1:.2f}')
        print(f'Voçe teve um percentual de aumento de 20%')
        print(f'Voçe recebeu um aumento de R${nv2:.2f}')
        print('------------------------------------------------------------------')
        print(f'Seu novo salario è R${nv1:.2f}')

    elif sl1 >= 1600 and sl1 <= 2000:
        nv1 = sl1+(sl1*15/100)
        nv2 = nv1-sl1
        print(f'Seu salario antes do reajuste erá R${sl1:.2f}')
        print(f'Voçe teve um percentual de aumento de 15%')
        print(f'Voçe recebeu um aumento de R${nv2:.2f}')
        print('------------------------------------------------------------------')
        print(f'Seu novo salario è R${nv1:.2f}')
    elif sl1 >= 2000 and sl1 <= 2800:
        nv1 = sl1+(sl1*10/100)
        nv2 = nv1-sl1
        print(f'Seu salario antes do reajuste erá R${sl1:.2f}')
        print(f'Voçe teve um percentual de aumento de 10%')
        print(f'Voçe recebeu um aumento de R${nv2:.2f}')
        print('------------------------------------------------------------------')
        print(f'Seu novo salario è R${nv1:.2f}')
    elif sl1 > 2800:
        nv1 = sl1+(sl1*5/100)
        nv2 = nv1-sl1
        print(f'Seu salario antes do reajuste erá R${sl1:.2f}')
        print(f'Voçe teve um percentual de aumento de 5%')
        print(f'Voçe recebeu um aumento de R${nv2:.2f}')
        print('------------------------------------------------------------------')
        print(f'Seu novo salario è R${nv1:.2f}')
    else:
        print('Erro')
    print()
    print()
    print()

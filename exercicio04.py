#Crie um algoritmo que receba 3 números e informe qual o maior entre eles.
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

if n1>n2:
    if n1>n3:
        print(f'O maior número entre {n1}, {n2} e {n3} é: {n1}')
    else:
        print(f'O maior número entre {n1}, {n2} e {n3} é: {n3}')
elif n2>n3:
    print(f'O maior número entre {n1}, {n2} e {n3} é: {n2}')
else:
    print(f'O maior número entre {n1}, {n2} e {n3} é: {n3}')
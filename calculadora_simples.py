# Define our function
def calculadora():
    operacao = input('''
Entre com o tipo de operacao:
+ for adicao
- for subtracao
* for multiplicacao
/ for divisao
''')

    numero_1 = int(input('Entre com o Primeiro numero: '))
    numero_2 = int(input('Entre com o Segundo numero: '))

    if operacao == '+':
        print('{} + {} = '.format(numero_1, numero_2))
        print(numero_1 + numero_2)

    elif operacao == '-':
        print('{} - {} = '.format(numero_1, numero_2))
        print(numero_1 - numero_2)

    elif operacao == '*':
        print('{} * {} = '.format(numero_1, numero_2))
        print(numero_1 * numero_2)

    elif operacao == '/':
        print('{} / {} = '.format(numero_1, numero_2))
        print(numero_1 / numero_2)

    else:
        print('voce digitou um operador invalido .')

# chama a  calculadora() fora da funcao
calculadora()


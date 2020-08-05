def calculadora(numero1, operador, numero2):
    if operador == '+':
        suma = numero1 + numero2
        print(f'{numero1} + {numero2} = {suma}')
    elif operador == '-':
        resta = numero1 - numero2
        print(f'{numero1} - {numero2} = {resta}')
    elif operador == '*':
        multiplicacion = numero1 * numero2
        print(f'{numero1} * {numero2} = {multiplicacion}')
    elif operador == '/':
        division = numero1 / numero2
        print(f'{numero1} / {numero2} = {division}')

if __name__ == "__main__":
    valor1_usuario = float(input('Escribe un número: '))
    operador_usuario = input('Elige un operador [  +  -  *  /  ] ')
    valor2_usuario = float(input('Escribe otro número: '))

    calculadora(valor1_usuario, operador_usuario, valor2_usuario)
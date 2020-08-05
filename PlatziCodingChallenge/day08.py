from math import pi

def volumen_cilindro(altura, radio):
    volumen = pi * (radio**2) *  altura
    print(f'EL volumen de tu cilindro es: {round(volumen, 1)} unidades.')

if __name__ == "__main__":
    print("""
    Volumen de un cilindro
    """)
    altura_user = float(input('Escribe la altura de tu cilindro: '))
    radio_user = float(input('Escribe el radio de tu cilindro: '))

    volumen_cilindro(altura_user, radio_user)
def piedra_papel_tijeras(jugador1, jugador2):
    j1 = jugador1.lower()
    j2 = jugador2.lower()
    pi = 'piedra'
    pa = 'papel'
    t = 'tijeras'

    if (j1 == pi and j2 == t) or (j1 == pa and j2 == pi) or (j1 == t and j2 == pa):
        print('¡Gana jugador 1!')
    elif j1 == j2:
        print('Empate, jueguen de nuevo.')
    elif (j2 == pi and j1 == t) or (j2 == pa and j1 == pi) or (j2 == t and j1 == pa):
        print('¡Gana jugador 2!')
    else:
        print('Error, intenta otra vez')


if __name__ == "__main__":
    print("""
    ¡Bienvenidos a piedra, papel o tijeras!
    """)
    jugador1 = input('Jugador 1, elige tu jugada: ')
    jugador2 = input('Jugador 2, elige tu jugada: ')
    
    piedra_papel_tijeras(jugador1, jugador2)
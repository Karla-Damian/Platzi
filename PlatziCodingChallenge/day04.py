def repite_palabra(string, repeticion):
    n = 1
    print(repeticion)
    if repeticion == n:
        print(string)
    elif repeticion > n:
        print(string)
        repeticion_user = repeticion - 1
        repite_palabra(string_user, repeticion_user)

if __name__ == "__main__":
    string_user = input('Escribe una palabra: ')
    repeticion_user = int(input('¿Cuántas veces quieres que se repita? '))
    repite_palabra(string_user, repeticion_user)

    
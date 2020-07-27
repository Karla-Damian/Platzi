def convertidor_segundos(horas, minutos):
    horas_a_segundos = horas * 60 * 60
    minutos_a_segundos = minutos * 60
    segundos_totales = horas_a_segundos + minutos_a_segundos
    print(f'{horas} horas con {minutos} minutos es igual es igual a {segundos_totales} segundos.')

if __name__ == "__main__":
    print('Convertidor de horas y minutos a segundos ⏱')
    horas_usuario = float(input('Escribe la(s) horas: '))
    minutos_usuario = float(input('Escribe los minutos: '))

    convertidor_segundos(horas_usuario, minutos_usuario)
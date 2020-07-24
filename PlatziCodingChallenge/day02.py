def area_triangulo(b, h):
    A = (b * h ) / 2
    print(f'El área de tu triángulo es: {A}')
    

if __name__ == "__main__":
    print('Área de un triángulo')
    base = float(input('¿Cuánto mide la base de tu triángulo? '))
    altura = float(input('¿Cuánto mide la altura de tu triángulo? '))
    
    area_triangulo(base, altura)
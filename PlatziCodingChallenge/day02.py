def area_triangulo(base, altura):
    area = (base * altura ) / 2
    print(f'El área de tu triángulo es: {area} unidades.')
    

if __name__ == "__main__":
    print('Área de un triángulo')
    base_usuario = float(input('¿Cuánto mide la base de tu triángulo? '))
    altura_usuario = float(input('¿Cuánto mide la altura de tu triángulo? '))
    
    area_triangulo(base_usuario, altura_usuario)
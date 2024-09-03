# Bool contiene los valores de true y false
# Los tipos numericos, es false para el 0, true para los demás valores
valor = 0
resultado = bool(valor)
print(f'valor: {valor}, Resultado: {resultado}')

valor = 15
resultado = bool(valor)
print(f'valor: {valor}, Resultado: {resultado}')

# Tipo string -> false '', true demás valores
valor = ''
resultado = bool(valor)
print(f'valor: {valor}, Resultado: {resultado}')

valor = 'hola'
resultado = bool(valor)
print(f'valor: {valor}, Resultado: {resultado}')

# tipo colecciones -> false para colecciones vacias
# tipo colecciones -> true para todas las demás
# lista
valor = []
resultado = bool(valor)
print(f'valor de una lista vacia: {valor}, Resultado: {resultado}')

valor = [2, 3, 4]
resultado = bool(valor)
print(f'valor de una lista con elementos: {valor}, Resultado: {resultado}')

# tupla
valor = ()
resultado = bool(valor)
print(f'valor tupla vacia: {valor}, Resultado: {resultado}')

valor = (1, 2, 3)
resultado = bool(valor)
print(f'valor tupla con elementos: {valor}, Resultado: {resultado}')

# diccionario
valor = {}
resultado = bool(valor)
print(f'valor de un diccionario vacio: {valor}, Resultado: {resultado}')

valor = {"nombre":"Flor", "apellido": "Carballo"}
resultado = bool(valor)
print(f'valor de un diccionario con elementos: {valor}, Resultado: {resultado}')

# sentencias de control con bool
if '':
    print('Regresa verdadero')
else:
    print('Regresa falso')


# ciclos
variable = 17
while variable:
    print('Regresa verdadero')
    break
else:
    print('Regresa falso')


#Bool contiene los valores de True y False
#Los tipos numericos, es false para el 0 (cero), true para los demas valores
valor = 0
resultado = bool(valor)
print(f'valor: {valor}, Resultado: {resultado}')

valor = 0.1
resultado = bool(valor)
print(f'valor: {valor}, Resultado: {resultado}')


# Tipo string -> False '', True demas valores
valor = ''
resultado = bool(valor)
print(f'valor: {valor}, Resultado: {resultado}')

valor = 'Hola'
resultado = bool(valor)
print(f'valor: {valor}, Resultado: {resultado}')


#Tipo coleccions -> False para colecciones vacias
#Tipo colecciones -> true para todas las demas
#Lista

valor = []
resultado = bool(valor)
print(f'valor: {valor}, Resultado: {resultado}')

#Tupla
valor = (5,)
resultado = bool(valor)
print(f'valor: {valor}, Resultado: {resultado}')

#Diccionario
valor = {}
resultado = bool(valor)
print(f'valor: {valor}, Resultado: {resultado}')

valor = {'Nombre': 'Juan','Apellido': 'Perez'}
resultado = bool(valor)
print(f'valor: {valor}, Resultado: {resultado}')

#Sentencias de control con bool
if (1,):
    print('Regresa verdadero')
else:
    print('Regresa falso')

#Ciclos
variable = 17
while variable:
    print('Regresa verdadero')
    break
else:
    print('Regresa falso')



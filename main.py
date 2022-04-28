# Operadores aritméticos con Python

# operandoA = 3
# operandoB = 2
# suma = operandoA + operandoB
#
# # print('Resultado suma:', suma)
# print(f'Resultado suma : {suma}')
#
# resta = operandoA - operandoB
# print(f'Resultado  resta: {resta}')
#
# multiplicacion = operandoA * operandoB
# print(f'Resultado multiplicación: {multiplicacion}')
#
# division = operandoA / operandoB
# print(f'Resultado división: {division}')
#
# divisionInt = operandoA // operandoB
# print(f'Resultado división entera: {divisionInt}')
#
# exponente = operandoA ** operandoB
# print(f'Resultado potencia: {exponente}')
#
# residuo = operandoA % operandoB
# print(f'Resultado residuo: {residuo}')


# Ejercicio: Calcular Área y Perímetro de un Rectangulo
# base = int(input('Ingrese la base: '))
# altura = int(input('Ingrese la altura: '))
#
# area = base * altura
# perimetro = (base * 2) + (altura * 2)
#
# print(f'El área es {area}')
# print(f'El perímetro es {perimetro}')


# Operadores de asignación con Python

# Asignación
# miVariable = 10
# # print(miVariable)
#
# # Reasignación
# miVariable = miVariable + 1
# print(miVariable)
#
# # Incremento con reasignación
# miVariable += 1
# print(miVariable)
#
# # Decremento con reasignación
# # miVariable = miVariable - 2
# miVariable -= 2
# print(miVariable)
#
# # Multiplicación con reasignación
# miVariable *= 3
# print(miVariable)
#
# # División con reasignación
# miVariable /= 2
# print(miVariable)


# Operadores de comparación

# a = 4
# b = 2
#
# # Igual
# resultado = (a == b)
# print(f'Resultado == : {resultado}')
#
# # Diferente
# resultado = (a != b)
# print(f'Resultado != : {resultado}')
#
# # Mayor que
# resultado = (a > b)
# print(f'Resultado > : {resultado}')
#
# # Mayor o igual que
# resultado = (a >= b)
# print(f'Resultado >= : {resultado}')
#
# # Menor que
# resultado = (a < b)
# print(f'Resultado < : {resultado}')
#
# # Menor o igual que
# resultado = (a <= b)
# print(f'Resultado <= : {resultado}')


# Ejercicio: Número par o impar

# numero = int(input('Por favor ingrese un número: '))
#
# if numero % 2 == 0:
#     print(f'El número {numero} es par')
# else:
#     print(f'El número {numero} es impar')


# Ejercicio: Determina si es myor de edad

# edadAdulto = 18
# edadPersona = int(input('Escribe tu edad: '))
#
# if edadPersona >= edadAdulto:
#     print(f'La persona con edad {edadPersona} es un adulto')
# else:
#     print(f'La persona con edad {edadPersona} es menor de edad')


# Operadores lógicos en Python

# a = True
# b = False
# resultado = a and b
# # print(resultado)
#
#
# resultado = a or b
# # print(resultado)
#
# resultado = not a
# print(resultado)


# Ejercicio: Valor dentro de rango (and)

# valor = int(input('Escribe el valor: '))
# valorMinimo = 0
# valorMaximo = 5
#
# # dentroRango = (valor >= valorMinimo) and (valor <= valorMaximo)
# dentroRango = (valorMinimo <= valor <= valorMaximo)
#
# if dentroRango:
#     print(f'El valor {valor} está dentro de rango')
# else:
#     print(f'El valor {valor} está fuera de rango')


# Ejercicio: Asistir juego (or)

# vacaciones = True
# diaDescanso = True
#
# if vacaciones or diaDescanso:
#     print('Puede asistir al juego')
# else:
#     print('Tiene deberes por hacer')


# Ejercicio: (not)

# vacaciones = False
# diaDescanso = False
#
# if not (vacaciones or diaDescanso):
#     print('Tiene deberes por hacer')
# else:
#     print('Puede asistir al juego')


# Ejercicio: Rango entre 20's y 30's

# edad = int(input('Introduce tu edad: '))
#
# # veintes = (edad >= 20 and edad < 30)
# # veintes = (20 <= edad < 30)
#
# # treintas = (edad >= 30 and edad < 40)
# # treintas = (30 <= edad < 40)
#
# if (20 <= edad < 30) or (30 <= edad < 40):
#     print('Dentro  de rango (20\'s) o (30\'s)')
#     # if veintes:
#     #     print('Dentro de los 20\'s')
#     # elif treintas:
#     #     print('Dentro de los 30\'s')
#     # else:
#         # print('Fuera de rango')
# else:
#     print("No está dentro de los 20's ni 30's")


# Ejercicio: El mayor de dos números

# numero1 = int(input('Proporciona el número 1: '))
# numero2 = int(input('Proporciona el número 2: '))
#
# if numero1 > numero2:
#     print(f'El número {numero1} es mayor')
# elif numero2 > numero1:
#     print(f'El número {numero2} es mayor')
# else:
#     print('Los números son iguales')


# Ejercicio: Tienda de libros

# print('Proporciones los siguientes datos del libro:')
# nombre = input('Proporciona el nombre del Libro: ')
# ide = int(input('Proporciona el ID del Libro: '))
# precio = float(input('Proporcione el precio: '))
# envio = input('Indica si el envio es gratuito (True/False): ')
#
# if envio == 'True':
#     envio = True
# elif envio == 'False':
#     envio = False
# else:
#     envio = 'Valor incorrecto, debe escribir True/False'
#
# print(f'''
#     Nombre: {nombre}
#     Id: {ide}
#     Precio: {precio}
#     Envio Gratuito?: {envio}
# ''')

























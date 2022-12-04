#change 1
"""
1).escribir un hola mundo
"""
print("hola mundo")
#change 2
"""
2). escribir un programa que almacene la cadena Hola Mundo en una variable y 
luego la muestre por pantalla
"""
saludo="Hola Mundo"

print(saludo)

"""
3).Escribir un programa que pregunte el nombre del usuario en la consola y 
después de que el usuario lo introduzca muestre por pantalla la cadena ¡Hola <nombre>!, 
donde <nombre> es el nombre que el usuario haya introducido.
"""
name=input("Escriba su nombre: ")

print("Hola ", name)

"""
Escribir un programa que muestre por pantalla el resultado de la siguiente 
operación aritmética 
(3+2/2*5)^2 
.
"""
resultado=(((3+2)/(2*5))**2)

print(resultado)

"""
Escribir un programa que pregunte al usuario por el número de horas trabajadas 
y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.
"""
horas_trabajadas=int(input("Cuantas horas laboro el dia de hoy: "))
coste_hora=float(input("Valor de hora trabajada: "))

print("su pago corresponde a " + str(horas_trabajadas*coste_hora))
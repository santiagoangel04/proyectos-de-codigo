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

"""
Escribir un programa que lea un entero positivo,n, 
introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta n. 
La suma de los n primeros enteros positivos puede ser calculada de la siguiente forma:

suma= n(n+1)/2
"""

"""
Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros),
calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase 
Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.
"""

"""
Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente
<c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el 
resto de la división entera respectivamente.
"""

"""
Escribir un programa que pregunte al usuario una cantidad a invertir, 
el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.
"""

"""
Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. 
Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben 
calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g.
Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete 
que será enviado.
"""

"""
Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año.
Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance 
final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada 
en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla 
la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.
"""

"""
Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.
"""
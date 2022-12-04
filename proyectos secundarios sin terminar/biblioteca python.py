 # utilizaremos la siguiente linea de codigo para abrir archivos externos con una herramienta llamada io
"""empezamos con la declaracion from la cual utulizaremo para hacer lo deseado, despues de esto
utilizaremos la declaracion import acompañado de un open"""
print("biblioteca de python")
print("segun la siguiente lista podra ingresar lo que quiera buscar, nuestra informacion es reducida sin envargo usted nos podra ayudar a mejorar")

busqueda=input(":-:")

from io import open

archivo_texto=open("archivo.txt","w")

oracion="!Hola a ti mi lea lector¡ \n que tal como estas de acuerdo con lo planeado estaremos probando a ver si servira nuestro archivo si sirve sera un gran, paso para la biblioteca"

archivo_texto.write(oracion)

archivo_texto.close()

pyi= "informacion python"
 
if busqueda == 'pyi':
    from io import open

    archivo_texto=open("archivo.txt","r")

    texto=archivo_texto.read()

    archivo_texto.close()

    print("si ud desea que la informacion pueda aparecer en este idle escriba la letra 'l'")

    ml=input(":-:")

    if ml == 'l':
        print(texto)

else:
    print("gracias")

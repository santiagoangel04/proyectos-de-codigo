#cuestionario mejorado, cambie el modo de evaluar las respuestas
import time 
print("CUESTIONARIO")
time.sleep(3)
print("el cuestionario empezara en pocos segundos")
time.sleep(5)
print("bienvenido a este cuestionario, esperamos su conmodidad previo a este cuestionario")
print("!esta listo o lista ¡")
time.sleep(2)
print("si su respuesta es si marque 'si' \n por el contrario si la respuesta es no marque 'no'")
respuesta =input("digite su respuesta: ")
time.sleep(1)

#bucle iterador de carga
i= 42
for x in range (1, i):
    if x % 7 == 0:
        time.sleep(2)
        print("cargando...")
    elif x % 2 == 0:
        time.sleep(2)
        print("validando información...")
    elif x % 3 == 0:
        time.sleep(2)
        print("esperenos un momento...")
    elif x % 5 == 0:
        time.sleep(2)
        print("esperamos su comodidad con nuestro cuestionario..")
if respuesta == 'si':
    print("su respuesta a sido analizada - :)")
    time.sleep(1)
    print("1.) como es su nombre")
    nombre = input("nombre: ")
    time.sleep(1)
    print("2.) donde vive especifique,ejemplo \n ciudad bogota, pais")
    ciudad = input("donde  vive usted: ")
    time.sleep(1)
    print("4.) en que año nacio")
    año = int(input("año de nacimiento: "))
    edad = int(2021) - int(año)
    time.sleep(2)
    print(f"su edad es de {edad} años")
    print("especifiquenos su tipo de educación siendo esto de la siguiente manera.\n Marque el tipo de educación que cursa usted, segun la siguiente lista.\n ejemplo educación media, escogeria entonces la segunda opcion 2 ")
    time.sleep(3)
    print("1. educaión basica ")
    print("2. educación media ")
    print("3. educación superior ")
    print("4. empleabilidad")
    y = int(input("marque su respuesta segun la lista anterior:"))
    time.sleep(2)
    if y == 1:
        print("anlizando su respuesta...\n respuesta verificada")
        print("donde estudia usted ")
        time.sleep(1)
        colegio = input("nombre del colegio: ")
        print(f"especifiquenos el grado segun como se organiza en su pais de recidencia en este caso {ciudad}")
        time.sleep(2)
        print("segun la ista entre que grados se encuentra usted")
        print("1. entre quinder a primer grado")
        print("2. primer a tercer grado ")
        print("3. tercer a quinto grado")
        grado = int(input("responda: "))
        if grado == 1:
            time.sleep(2)
            print("que ha aprendido en ese grado")
            from io import open
            archivo_texto=open("lista de comentarios uspy.txt","a")

            print("escriba su comentario en comillas y despues marque su nombre completo")

            archivo_texto.write(input("escriba aqui su comentario"))

            archivo_texto.close()
            print("muchas gracias, esperamos volvernos a ver")
            quit()
        if grado == 2:
            time.sleep(2)
            print("que ha aprendido en ese grado")
            from io import open
            
            archivo_texto=open("lista de comentarios uspy.txt","a")

            print("escriba su comentario en comillas y despues marque su nombre completo")

            archivo_texto.write(input("escriba aqui su comentario"))

            archivo_texto.close()
            print("muchas gracias, esperamos volvernos a ver")
            quit()
        if grado == 3:
            time.sleep(2)
            print("que ha aprendido en ese grado")
            from io import open
            archivo_texto=open("lista de comentarios uspy.txt","a")

            print("escriba su comentario en comillas y despues marque su nombre completo")

            coment = input("escriba aqui su comentario")

            archivo_texto.write(coment)

            archivo_texto.close()
            
            print(f"es bueno saber sobre usted señor {nombre} ", "esperamos que termine los estudios en su colegio,{colegio} sabiendo esto esperamos que le fuese de agrado este cuestionario")
            print("muchas gracias, esperamos volvernos a ver")
            quit()
    if y == 2:
        time.sleep(2)
        print("anlizando su respuesta...\n respuesta verificada")
        print("3.) donde estudia usted ")
        colegio = input("nombre del colegio: ")
        print(f"especifiquenos el grado segun como se organiza en su pais de recidencia en este caso {ciudad}")
        time.sleep(2)
        print("segun la ista entre que grados se encuentra usted")
        print("1. entre primer a segundo grado de secundaria")
        print("2. entre segundo a cuarto grado de secundaria")
        print("3. entre quinto  a sexto grado de secundaria")
        grado = int(input("responda: "))
        if grado == 1:
            time.sleep(2)
            print("que ha aprendido en ese grado")
            input("escriba aqui su comentario")
            print("gracias por participar en nuestro cuestionario {nombre} esperamos que sea el mejor y aprenda nuevas cosas.\n que buen comentario pero se denota tu interes por el español jajajjajaj ")
            print("muchas gracias, esperamos volvernos a ver")
            quit()
        if grado == 2:
            time.sleep(2)
            print("que ha aprendido en ese grado")
            input("escriba aqui su comentario")
            print("gracias por participar en nuestro cuestionario {nombre} esperamos que sea el mejor y aprenda nuevas cosas.\n que buen comentario pero se denota tu interes por el español jajajjajaj ")
            print("muchas gracias, esperamos volvernos a ver")
            quit()
        if grado == 3:
            time.sleep(2)
            print("que ha aprendido en ese grado")
            input("escriba aqui su comentario")
            print("gracias por participar en nuestro cuestionario {nombre} esperamos que sea el mejor y aprenda nuevas cosas.\n que buen comentario pero se denota tu interes por el español jajajjajaj ")
            print("muchas gracias, esperamos volvernos a ver")
            quit()
    if y == 3:
        time.sleep(2)
        print("donde estudia usted o quisiera estudiar")
        colegio = input("nombre de la institución: ")
        print("especifique que estudia y si todavia no entra a la univercidad, diga que quisiera estudiar usted")
        carrera = input("escriba su respuesta: ")
        print(f"tu {nombre} seras el mejor estudiando {carrera}, siendo asi si quieres estudiar en la univercidad {colegio},o que ya estes estudiando en esa univercidad.\n de nuestra parte le deseamos lo mejor y le damos gracias por hacer este cuestionario.")
        print("muchas gracias, esperamos volvernos a ver")
        quit()
    else :
        time.sleep(2)
        print("es usted empleado \n Marque 1 si la respuesta es si y si larespuesta es no marque 0")
        work = int(input("respuesta: "))
        if work == 1:
            time.sleep(2)
            print("trabaja usted con alguna especialidad o carrera \n Marque si o no de la misma manera que lo hizo anteriormente")
            si = int(input("respuesta: "))
            if si == 1:
                time.sleep(2)
                print("especifique su carrera o especialidad y en donde trabaja o que hace")
                carrera = input("carrera: ")
                campo = input("que hace o en que trabaja: ")
                print(f"siendo asi doctor {nombre} por lo que esta maquina y programa a analizado usted es el mejor en su trabajo")
                print("muchas gracias, esperamos volvernos a ver")
                quit()
        if work == 0:
            time.sleep(2)
            print("especifiquenos que hace usted, probablemente le ayudemos con algo")
            input("comentario: ")
            print("vamos a ver que podemos hacer para ayudarlo")
            print("muchas gracias, esperamos volvernos a ver")
            quit()
if respuesta == 'no':
    time.sleep(4)
    print("esperamos su comodidad con nuestro cuestionario..")
    print("sabremos su negacion al proyecto")
    print("muchas gracias, esperamos volvernos a ver")
    quit()
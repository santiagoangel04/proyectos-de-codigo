 # programcuestionarie
print("el cuestionario empezara en pocos segundos")
i= 5
while i > 0:
    print(i,"seg")
    i=i-1
print("bienvenido a este cuestionario, esperamos su conmodidad previo a este cuestionario")
print("esta listo o lista para este cuestionario")
x = int(input("marque 1 si usted esta listo, marque por el contrario 0 si todavia no esta listo o no quiere comenzar:"))
if x == 1:
    print("gracias, continuemos")
    print("1.) como es su nombre")
    nombre = input("nombre: ")
    print("2.) donde vive especifique,ejemplo \n ciudad bogota, pais")
    ciudad = input("donde  vive usted: ")
    print("4.) en que año nacio")
    año = int(input("año de nacimiento: "))
    edad = int(2020) - int(año)
    print(f"su edad es de {edad} años")
    print("especifiquenos su tipo de educación siendo esto de la siguiente manera.\n Marque el tipo de educación que cursa usted, segun la siguiente lista.\n ejemplo educación media, escogeria entonces la segunda opcion 2 ")
    print("1. educaión basica ")
    print("2. educación media ")
    print("3. educación superior ")
    print("4. empleabilidad")
    y = int(input("marque su respuesta segun la lista anterior:"))
    if y == 1:
        print("anlizando su respuesta...\n respuesta verificada")
        print("donde estudia usted ")
        colegio = input("nombre del colegio: ")
        print(f"especifiquenos el grado segun como se organiza en su pais de recidencia en este caso {ciudad}")
        print("segun la ista entre que grados se encuentra usted")
        print("1. entre quinder a primer grado")
        print("2. primer a tercer grado ")
        print("3. tercer a quinto grado")
        grado = int(input("responda: "))
        if grado == 1:
            print("que ha aprendido en ese grado")
            input("escriba aqui su comentario")
            print("muchas gracias, esperamos volvernos a ver")
            quit()
        if grado == 2:
            print("que ha aprendido en ese grado")
            input("escriba aqui su comentario")
            print("muchas gracias, esperamos volvernos a ver")
            quit()
        if grado == 3:
            print("que ha aprendido en ese grado")
            coment = input("escriba aqui su comentario")
            print(f"es bueno saber sobre usted señor {nombre}, esperamos que termine los estudios en su colegio,{colegio} sabiendo esto esperamos que le fuese de agrado este cuestionario")
            print("muchas gracias, esperamos volvernos a ver")
            quit()
    if y == 2:
        print("anlizando su respuesta...\n respuesta verificada")
        print("3.) donde estudia usted ")
        colegio = input("nombre del colegio: ")
        print(f"especifiquenos el grado segun como se organiza en su pais de recidencia en este caso {ciudad}")
        print("segun la ista entre que grados se encuentra usted")
        print("1. entre primer a segundo grado de secundaria")
        print("2. entre segundo a cuarto grado de secundaria")
        print("3. entre quinto  a sexto grado de secundaria")
        grado = int(input("responda: "))
        if grado == 1:
            print("que ha aprendido en ese grado")
            input("escriba aqui su comentario")
            print("gracias por participar en nuestro cuestionario {nombre} esperamos que sea el mejor y aprenda nuevas cosas.\n que buen comentario pero se denota tu interes por el español jajajjajaj ")
            print("muchas gracias, esperamos volvernos a ver")
            quit()
        if grado == 2:
            print("que ha aprendido en ese grado")
            input("escriba aqui su comentario")
            print("gracias por participar en nuestro cuestionario {nombre} esperamos que sea el mejor y aprenda nuevas cosas.\n que buen comentario pero se denota tu interes por el español jajajjajaj ")
            print("muchas gracias, esperamos volvernos a ver")
            quit()
        if grado == 3:
            print("que ha aprendido en ese grado")
            input("escriba aqui su comentario")
            print("gracias por participar en nuestro cuestionario {nombre} esperamos que sea el mejor y aprenda nuevas cosas.\n que buen comentario pero se denota tu interes por el español jajajjajaj ")
            print("muchas gracias, esperamos volvernos a ver")
            quit()
    if y == 3:
        print("donde estudia usted o quisiera estudiar")
        colegio = input("nombre de la institución: ")
        print("especifique que estudia y si todavia no entra a la univercidad, diga que quisiera estudiar usted")
        carrera = input("escriba su respuesta: ")
        print(f"tu {nombre} seras el mejor estudiando {carrera}, siendo asi si quieres estudiar en la univercidad {colegio},o que ya estes estudiando en esa univercidad.\n de nuestra parte le deseamos lo mejor y le damos gracias por hacer este cuestionario.")
        print("muchas gracias, esperamos volvernos a ver")
        quit()
    else :
        print("es usted empleado \n Marque 1 si la respuesta es si y si larespuesta es no marque 0")
        work = int(input("respuesta: "))
        if work == 1:
            print("trabaja usted con alguna especialidad o carrera \n Marque si o no de la misma manera que lo hizo anteriormente")
            si = int(input("respuesta: "))
            if si == 1:
                print("especifique su carrera o especialidad y en donde trabaja o que hace")
                carrera = input("carrera: ")
                campo = input("que hace o en que trabaja: ")
                print(f"siendo asi doctor {name} por lo que esta maquina y programa a analizado usted es el mejor en su trabajo")
                print("muchas gracias, esperamos volvernos a ver")
                quit()
        if work == 0:
            print("especifiquenos que hace usted, probablemente le ayudemos con algo")
            input("comentario: ")
            print("vamos a ver que podemos hacer para ayudarlo")
            print("muchas gracias, esperamos volvernos a ver")
            quit()
elif x == 0:
    print("muchas gracias, esperamos volvernos a ver")
    quit()
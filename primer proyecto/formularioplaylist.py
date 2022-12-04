#formulario de selecionador de playlist de juegos
from cProfile import label
from re import T
from tkinter import *
from PIL import Image,ImageTk
#creamos todos los componentes del formulario
#pantalla secundaria "aqui apareceran los titulos del tema escogido"#
#creamos
def pantalla_accion():
    ventana=Tk()
    ventana.iconbitmap("primer proyecto\\icono.ico")
    ventana.title("sountracks games (accion)")
    ventana.config(bg="black",cursor="mouse")
    #el primer elemento es el del eje x y y el segundo sera del eje y
    ventana.geometry("800x900")
    anuncios_pagina_acc(ventana)

    # hacemos los botones de cada juego
    photo_halo=ImageTk.PhotoImage(file="primer proyecto\\halo.png")
    boton_halo=Button(ventana,bg="white", fg="purple", bd=5)
    boton_halo.place(x=100,y=100)

    ventana.mainloop()

def pantalla_aventura():
    ventana=Tk()
    ventana.iconbitmap("primer proyecto\icono.ico")
    ventana.title("sountracks games (aventura)")
    ventana.config(bg="black",cursor="mouse")
    #el primer elemento es el del eje x y y el segundo sera del eje y
    ventana.geometry("800x900")
    anuncios_pagina_aven(ventana)
    ventana.mainloop()

def pantalla_simulacion():
    ventana=Tk()
    ventana.iconbitmap("primer proyecto\icono.ico")
    ventana.title("sountracks games (simulacion)")
    ventana.config(bg="black",cursor="mouse")
    #el primer elemento es el del eje x y y el segundo sera del eje y
    ventana.geometry("800x900")
    anuncios_pagina_simul(ventana)
    ventana.mainloop()

def pantalla_deportes():
    ventana=Tk()
    ventana.iconbitmap("primer proyecto\icono.ico")
    ventana.title("sountracks games (deportes)")
    ventana.config(bg="black",cursor="mouse")
    #el primer elemento es el del eje x y y el segundo sera del eje y
    ventana.geometry("800x900")
    anuncios_pagina_depor(ventana)
    ventana.mainloop()

def pantalla_rol():
    ventana=Tk()
    ventana.iconbitmap("primer proyecto\icono.ico")
    ventana.title("sountracks games (rol)")
    ventana.config(bg="black",cursor="mouse")
    #el primer elemento es el del eje x y y el segundo sera del eje y
    ventana.geometry("800x900")
    anuncios_pagina_rol(ventana)
    ventana.mainloop()

def pantalla_arcade():
    ventana=Tk()
    ventana.iconbitmap("primer proyecto\icono.ico")
    ventana.title("sountracks games (arcade)")
    ventana.config(bg="black",cursor="mouse")
    #el primer elemento es el del eje x y y el segundo sera del eje y
    ventana.geometry("800x900")
    anuncios_pagina_arca(ventana)
    ventana.mainloop()

def pantalla_estrategia():
    ventana=Tk()
    ventana.iconbitmap("primer proyecto\icono.ico")
    ventana.title("sountracks games (estrategia)")
    ventana.config(bg="black",cursor="mouse")
    #el primer elemento es el del eje x y y el segundo sera del eje y
    ventana.geometry("800x900")
    anuncios_pagina_estrate(ventana)
    ventana.mainloop()


#creamos los labels para los anunicos en pantalla accion
def anuncios_pagina_acc(root):
    titulo_pag=Label(root,text="usted escogio el tema de 'acción '", bg="black", fg="white", font="gotic 19")
    titulo_pag.pack(side="top")
    sub_titulo=Label(root,text="Escoja la playlist del juego que mas te guste", fg="brown", bg="black", font="gotic 15")
    sub_titulo.place(y=80,x=10)
   
    
#creamos los labels para los anunicos en pantalla aventura
def anuncios_pagina_aven(root):
    titulo_pag=Label(root,text="usted escogio el tema de 'aventura '", bg="black", fg="white", font="gotic 19")
    titulo_pag.pack(side="top")
    sub_titulo=Label(root,text="Escoja la playlist del juego que mas te guste", fg="brown", bg="black", font="gotic 15")
    sub_titulo.place(y=80,x=10)

#creamos los demas anuncios de ventana
#labels simulacion
def anuncios_pagina_simul(root):
    titulo_pag=Label(root,text="usted escogio el tema de 'simulacion '", bg="black", fg="white", font="gotic 19")
    titulo_pag.pack(side="top")
    sub_titulo=Label(root,text="Escoja la playlist del juego que mas te guste", fg="brown", bg="black", font="gotic 15")
    sub_titulo.place(y=80,x=10)

#labels deportes
def anuncios_pagina_depor(root):
    titulo_pag=Label(root,text="usted escogio el tema de 'deportes '", bg="black", fg="white", font="gotic 19")
    titulo_pag.pack(side="top")
    sub_titulo=Label(root,text="Escoja la playlist del juego que mas te guste", fg="brown", bg="black", font="gotic 15")
    sub_titulo.place(y=80,x=10)

#arcade
def anuncios_pagina_arca(root):
    titulo_pag=Label(root,text="usted escogio el tema de 'arcade' ", bg="black", fg="white", font="gotic 19")
    titulo_pag.pack(side="top")
    sub_titulo=Label(root,text="Escoja la playlist del juego que mas te guste", fg="brown", bg="black", font="gotic 15")
    sub_titulo.place(y=80,x=10)


#labels rol
def anuncios_pagina_rol(root):
    titulo_pag=Label(root,text="usted escogio el tema de 'rol '", bg="black", fg="white", font="gotic 19")
    titulo_pag.pack(side="top")
    sub_titulo=Label(root,text="Escoja la playlist del juego que mas te guste", fg="brown", bg="black", font="gotic 15")
    sub_titulo.place(y=80,x=10)

#estrategia
def anuncios_pagina_estrate(root):
    titulo_pag=Label(root,text="usted escogio el tema de 'rol '", bg="black", fg="white", font="gotic 19")
    titulo_pag.pack(side="top")
    sub_titulo=Label(root,text="Escoja la playlist del juego que mas te guste", fg="brown", bg="black", font="gotic 15")
    sub_titulo.place(y=80,x=10)


#creamos los generos que tendra nuestra playlist
def generos(root):
    '''
    codigo para añadir imagen, solo que al añadirla esta permace de color blanco
    '''
    #se crea el genero de accion
    photo_accion=ImageTk.PhotoImage(file="primer proyecto\\accion.png")
    boton_genero_accion=Button(root,text="ACCION", font="arial 20",fg="white",bg="green",bd=5,command=pantalla_accion)
    boton_genero_accion.place(x=29,y=140)
    imagen_genero_accion=Label(root,image=photo_accion,bg="red",fg="white",font="arial 20",bd=5)
    imagen_genero_accion.place(x=55,y=220)

    #creamos el genero aventura
    photo_aventura=ImageTk.PhotoImage(file="primer proyecto\\aventura.png")
    boton_genero_aventura=Button(root,text="AVENTURA",font="arial 20",fg="white",bg="green",bd=5,command=pantalla_aventura)
    boton_genero_aventura.place(x=200,y=140)
    #label elaborar
    imagen_genero_aventura=Label(root,image=photo_aventura ,bg="orange",fg="white", font="arial 20",bd=5)
    imagen_genero_aventura.place(x=220,y=220)

    #elaboramos los botones para cada uno de los tipos de juegos 
    #rol
    photo_rol=ImageTk.PhotoImage(file="primer proyecto\\rol.png")
    boton_genero_rol=Button(root,text="ROL", font="arial 20",fg="white",bg="green",bd=5,command=pantalla_rol)
    boton_genero_rol.place(x=350,y=420)
    #label de rol
    imagen_genero_rol=Label(root,image=photo_rol,bg="white",fg="white", font="arial 20",bd=5)
    imagen_genero_rol.place(x=325,y=499)

    #deportes
    photo_deportes=ImageTk.PhotoImage(file="primer proyecto\\deportes.png")
    boton_genero_deportes=Button(root,text="DEPORTES", font="arial 20",fg="white",bg="green",bd=5,command=pantalla_deportes)
    boton_genero_deportes.place(x=645,y=140)
    #label de deportes
    imagen_genero_deportes=Label(root,image=photo_deportes,bg="darkgreen",fg="white", font="arial 20",bd=5)
    imagen_genero_deportes.place(x=650,y=220)

    #simulacion
    photo_simulacion=ImageTk.PhotoImage(file="primer proyecto\\simulacion.png")
    boton_genero_simulacion=Button(root,text="SIMULACION", font="arial 20",fg="white",bg="green",bd=5,command=pantalla_simulacion)
    boton_genero_simulacion.place(x=410,y=140)
    #label de simulacion
    imagen_genero_simulacion=Label(root,image=photo_simulacion,bg="darkblue",fg="white", font="arial 20",bd=5)
    imagen_genero_simulacion.place(x=435,y=220)

    #arcade
    photo_arcade=ImageTk.PhotoImage(file="primer proyecto\\arcade.png")
    boton_genero_arcade=Button(root,text="ARCADE", font="arial 20",fg="white",bg="green",bd=5,command=pantalla_arcade)
    boton_genero_arcade.place(x=29,y=420)
    #label de arcade
    imagen_genero_arcade=Label(root,image=photo_arcade,bg="black",fg="white", font="arial 20",bd=5)
    imagen_genero_arcade.place(x=25,y=499)

    #estrategia
    photo_estrategia=ImageTk.PhotoImage(file="primer proyecto\\estrategia.png")
    boton_genero_estrategia=Button(root,text="ESTRATEGIA", font="arial 20",fg="white",bg="green",bd=5,command=pantalla_estrategia)
    boton_genero_estrategia.place(x=615,y=420)
    #label de estrategia
    imagen_genero_estrategia=Label(root,image=photo_estrategia,bg="gold",fg="white", font="arial 20",bd=5)
    imagen_genero_estrategia.place(x=645,y=499)

    #para que la imagen aparesca siempre debe haber un mainloop 
    root.mainloop()
    

#iniciador del programa
if __name__ == "__main__":
    #pantalla principal aqui apareceran los temas de la pagina principal
    ventana_principal=Tk()
    #agregamos el icono de la pantalla con el iconbit
    #path of icon ==C:\Users\Santiago Angel\OneDrive\Documentos\codigo\proyectos de codigo\projects-group-\primer proyecto\icono.ico
    ventana_principal.iconbitmap("primer proyecto\icono.ico")
    ventana_principal.title("soundtracks games pag_1_")
    ventana_principal.resizable(0,0)
    ventana_principal.config(bg="black",cursor="mouse")
    ventana_principal.geometry("850x700")
    #creamos los anuncios de la pagina principal
    titulo_pag=Label(ventana_principal,text="Bienvenido a soundtracks games", bg="black", fg="white", font="gotic 25")
    titulo_pag.pack(side="top")
    sub_titulo=Label(ventana_principal,text="Escoja el genero del juego que mas te guste", fg="white", bg="black", font="gotic 15")
    sub_titulo.place(y=80,x=10)
    generos(ventana_principal)
    ventana_principal.mainloop()
    
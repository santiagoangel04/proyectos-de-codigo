#serpiente snake
import turtle
import time
import random

reelentizar = 0.1

ventana= turtle.Screen()
ventana.setup(width=1000, height= 600)
ventana.title("culebrita fina")
ventana.bgcolor("blue")
ventana.tracer()

# head de la snake
cabeza=turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.penup()
cabeza.goto(0, 1)
cabeza.color("black")
cabeza.direction = "stop"
# food de la snake
comida=turtle.Turtle()
comida.shape("circle")
comida.speed(0)
comida.penup()
comida.goto(25, 50)
comida.color("green")

# alargamiento de cuerpo
segmento =[]

# funciones 

def arriba():
    cabeza.direction = "up"
def abajo():
    cabeza.direction = "down"
def derecha():
    cabeza.direction = "right"
def izquierda():
    cabeza.direction = "left"

def move():
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 10)

    if cabeza.direction == "down":
        y =cabeza.ycor()
        cabeza.sety(y - 10)

    if cabeza.direction == "left":
        x= cabeza.xcor()
        cabeza.setx(x - 10)
    
    if cabeza.direction == "right":
        x= cabeza.xcor()
        cabeza.setx(x + 10)

# teclado
ventana.listen()
ventana.onkey(arriba, "Up")
ventana.onkey(abajo, "Down")
ventana.onkey(izquierda, "Left")
ventana.onkey(derecha, "Right")

while True:
    ventana.update()

    #colision bordes 
    if cabeza.xcor() > 470 or cabeza.xcor() < -480 or cabeza.ycor() > 290 or cabeza.ycor() < -270 : 
        time.sleep(1)
        cabeza.goto(0,0)
        cabeza.direction= "stop"

        #ocultar los segmentos 
        for segmento in segmento:
            segmento.goto(8000,8000)

        # limpiando segmentos
        segmento.clear()

    # colision comida 
    if cabeza.distance(comida) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        comida.goto(x,y)
         
        nuevo_segmento= turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape("square")
        nuevo_segmento.penup()
        nuevo_segmento.color("red")
        segmento.append(nuevo_segmento)

    # movimiento del cuerpo
    segmento_total = len(segmento)
    for index in range (segmento_total -1, 0 ,-1):
       x=segmento[index - 1].xcor()
       y= segmento[index - 1].ycor()
       segmento[index].goto(x,y)
    if segmento_total > 0:
        x= cabeza.xcor()
        y= cabeza.ycor()
        segmento[0].goto(x,y)

    
        



    move()

    #colision del cuerpo
    for segmento in segmento:
        if segmento.distance(cabeza) < 20:
            time.sleep(1)
            cabeza.goto(0,0)
            cabeza.direction="stop"
            
            #esconder segmentos
            for segmento in segmento:
                segmento.goto(1000, 1000)

    time.sleep(reelentizar)



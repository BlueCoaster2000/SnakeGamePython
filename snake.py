import turtle
import time
import random

delay = 0.1
cuerpo_serpiente = []
puntos = 0
record_puntos = 0

wn = turtle.Screen() #ventana

#Titulo ventana
wn.title('Juego Snake')
#Dimensiones ventana
wn.setup(width=600, height=600)
#background color
wn.bgcolor('#423e3e')

#Comida Config
comida = turtle.Turtle()
comida.speed(0)
comida.shape('circle')
comida.color('red')
comida.penup()
comida.goto(0,100)
comida.direction = 'stop'

#Poder Config
poder = turtle.Turtle()
poder.speed(0)
poder.shape('turtle')
poder.color('blue')
poder.penup()
poder.goto(10,40)
poder.direction = 'stop'

#Puntuacion
text = turtle.Turtle()
text.speed(0)
text.color('white')
text.penup()
text.hideturtle()
text.goto(0,260)
text.write(f'Puntos: 0          Record: 0', align="center", font=("arial",24))

#cabeza serpiente
head = turtle.Turtle()
#Opciones por defecto:

head.speed(0) #velocidad por defecto
head.shape('square')#forma de la cabeza
head.color('green')#Color
head.goto(0,0) #Posicion inicial
head.direction = 'stop' #Direccion de salida(empieza saliendo hacia arriba)
head.penup() #para que no deje rastro al moverse


def mov():
    if head.direction == 'up':
        #almacenamos el valor actual de la coordenada y
        y = head.ycor()
        #le damos el valor nuevo a la dirección en la que lo movemos
        head.sety(y+10)
       
    if head.direction == 'down':
         #almacenamos el valor actual de la coordenada y
        y = head.ycor()
        #le damos el valor nuevo a la dirección en la que lo movemos
        head.sety(y-10)

    if head.direction == 'right':
        #almacenamos el valor actual de la coordenada y
        x = head.xcor()
        #le damos el valor nuevo a la dirección en la que lo movemos
        head.setx(x+10)

    if head.direction == 'left':
        #almacenamos el valor actual de la coordenada y
        x = head.xcor()
        #le damos el valor nuevo a la dirección en la que lo movemos
        head.setx(x-10)



#Escuchar las teclas que presiona el usuario
def dirUp():
    head.direction = 'up'
def dirDown():
    head.direction = 'down'
def dirLeft():
    head.direction = 'left'
def dirRight():
    head.direction = 'right'

wn.listen()

wn.onkeypress(dirUp,'Up')
wn.onkeypress(dirDown,'Down')
wn.onkeypress(dirLeft,'Left')
wn.onkeypress(dirRight,'Right')

#Restablecer serpiente
def restart():
    time.sleep(1)
    head.goto(0,0)
    #Ponemos los puntos a 0
    text.clear()
    puntos =  0
    text.write(f'Puntos: {puntos}          Record: {record_puntos}', align="center", font=("arial",24))
    head.direction = 'stop'


    #Esconder segmentos
    for segmento in cuerpo_serpiente:
        segmento.goto(10000,10000)
    #Limpiar los segmentos del cuerpo despues de reiniciar el juego
    cuerpo_serpiente.clear()
while True:
    wn.update()
    #Colision con la ventana
    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
        restart()
        
    #Colision con la comida
    if head.distance(comida) < 20: 
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        comida.goto(x,y)
        
        #puntuaciones 
        puntos += 10
        if puntos > record_puntos:
            record_puntos = puntos

        text.clear()
        text.write(f'Puntos: {puntos}          Record: {record_puntos}', align="center", font=("arial",24))
        #nuevo segmento
        nuevo_segmento =  turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape('square')
        nuevo_segmento.color('#67fcbb')
        nuevo_segmento.penup()
        cuerpo_serpiente.append(nuevo_segmento)

    totalSegm = len(cuerpo_serpiente)
    for i in range(totalSegm-1,0,-1):
            x = cuerpo_serpiente[i-1].xcor()
            y = cuerpo_serpiente[i-1].ycor()
            cuerpo_serpiente[i].goto(x,y)
    
    if totalSegm > 0:
        x = head.xcor()
        y = head.ycor()#Coordenada x/y de la cabeza de la serpiente
        cuerpo_serpiente[0].goto(x,y)
    #colisiones con el powerUp
    if head.distance(poder) < 20:
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        velocidad_anterior =  head.speed()
        head.speed(velocidad_anterior+1)
        poder.goto(x,y)
        print('TURBOOO')
       
#Colisiones con su cuerpo
    mov()
    for segmento in cuerpo_serpiente:
        if segmento.distance(head) < 10:
             puntos = 0
             restart()
    time.sleep(delay)
turtle.done()
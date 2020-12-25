# Pong Game
# by @kerim
# Add Sound - https://youtu.be/XGf2GcyHPhc?t=2383

# Yapilacaklar
# oncelikle wn ile ekran buyukluk renk gibi ayarlamalari yap
# Sonrasinda alt paddle
# Ball
# Paddle hareket ettirme
# Ball hareket ettirme -> ball icin dx ve dy degeri ata -> While dongusu icinde yaz -> Ball auto movement
# Ball sinirlamalar verme -> While -> Border Check
# Topun asagiya dusmesi durumunda yeniden baslamasi

import turtle



# Screen settings
wn = turtle.Screen()
wn.title("Racket game")
wn.bgcolor("white")
wn.setup(width=1100, height=800) # ekran buyuklugu
wn.tracer(0) # Bu komut ile hareket eden seyler ilk ayarlanan konumda basliyor. (Dene)



# Paddle
paddle=turtle.Turtle()
paddle.shape("square")
paddle.color("black")
paddle.shapesize(stretch_wid=1, stretch_len=7)
paddle.penup() # Bu komut hareket ettiginde olusan cizgilerin olmamasini saglar
paddle.goto(0, -350)



#Ball
ball = turtle.Turtle()
ball.shape("square")
ball.color("black")
ball.penup()
ball.goto(0, 0)
ball.speed(1)

# Ball onjesine dx ve dy degeri veriyoruz NEDEN???
ball.dx = 0.2
ball.dy = 0.2


# Game
pen = turtle.Turtle()
pen.speed(0)
pen.color("darkblue")
pen.penup()





# Moving effects - hareket ettirme islemleri

# Oncelikle bir fonksiyon yardimi ile paddle in x kordinatini her defasinda saga kaydiracak bir fonksiyon yaziyoruz - Sonra listenera ekleyecegiz
def paddle_right():
    x = paddle.xcor()
    x += 30
    paddle.setx(x)

def paddle_left():
    x = paddle.xcor()
    x -= 30
    paddle.setx(x)


# Listener ekleme ve tus tanimlama
wn.listen() # wn = turtle.Screem() -> Ekranda tuslara yonelik dinleme yapiyor 
wn.onkeypress(paddle_right, "Right") # Klavyede sag ok tusa basildiginda paddle_right fonksiyonunu calistiriyor
wn.onkeypress(paddle_left, "Left") # Klavyede sol ok tusuna basildiginda paddle_left fonksiyonunu calistiriyor



#Main game loop
while True:
    wn.update()

    #Topun kendiliginden hareket etmesi -> Ball auto movement -> Capraz hareket etmesi
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border check
    if ball.ycor() > 375: # ust sinirin belirlenmesi
        ball.sety(375)
        ball.dy *= -1

    # Topun ekranin Sag tarafindaki sinirlarin belirlenmesi
    if ball.xcor() > 525:
        ball.setx(525)
        ball.dx *= -1

    # Topun ekranin Sol taraftindaki sinirlarin belirlenmesi
    if ball.xcor() < -525:
        ball.setx(-525)
        ball.dx *= -1

    # Top -390 i gecerse yani Paddle'in altina inerse ortadan basla
    if ball.ycor() < -400:
        ball.goto(0, 0)
        ball.dy *= -1

    # Top ile Paddle etikilesime girmesi
    if (ball.ycor() < -340 and ball.ycor() > -350) and (ball.xcor() < paddle.xcor() + 60 + 5  and ball.xcor() > paddle.xcor() - 60 -5 ):
        ball.sety(-340)
        ball.dy *= -1




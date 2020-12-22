import turtle

wn = turtle.Screen()
wn.title("Pong by @Kerim")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)


# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square") # seklinin kare olmasini saglar
paddle_a.color("white") # renk ayarlama
paddle_a.shapesize(stretch_wid=5, stretch_len=1) # paddle a icin yukseklik ve genislik degerlerini veriyoruz
paddle_a.penup()
paddle_a.goto(-350, 0) # Konumunu belirlemek icin kullaniyoruz - Normalde tam ortadan basliyor


# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square") # seklinin kare olmasini saglar
paddle_b.color("white") # renk ayarlama
paddle_b.shapesize(stretch_wid=5, stretch_len=1) # paddle a icin yukseklik ve genislik degerlerini veriyoruz
paddle_b.penup()
paddle_b.goto(350, 0) # Konumunu belirlemek icin kullaniyoruz - Normalde tam ortadan basliyor


# Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square") # seklinin kare olmasini saglar
ball.color("blue") # renk ayarlama
ball.penup()
ball.goto(0, 0) # Konumunu belirlemek icin kullaniyoruz - Normalde tam ortadan basliyor

ball.dx = 0.2 # bu topun her hareketinde 2 birimlik yer degistirecegini gosteriyor
ball.dy = 0.2 # burada ayni zamanda y ekseninde 2 birim hareket etmesi gerektigini tanimladik yani capraz gider


# Simdiyaptigimiz seyleri hareket ettirmenin zamani geldi
# Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)



#Tuslara listener ekleme ve fonksiyon cagirma - Keyboard Binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")



#Main game loop
while True:
    wn.update()

    # Move tha Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border check
    if ball.ycor() > 290: # Eger ball in konumu 290 dan buyuk ise
        ball.sety(290) # Ball in y kordinatini 290 a esitle ve *= -1 ile -> ters yonde devam etmesini sagla
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390: # bu sinirlarin disina cikarsa ortadan basla ve ters yonde devam et
        ball.goto(0, 0)
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1

    #Paddle en Ball collisions - Top ile raket in etkilesime girmesi
    if (ball.xcor() > 340 and ball.xcor() < 350 ) and (ball.ycor() < paddle_b.ycor() +40 and ball.ycor() > paddle_b.ycor() -50):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350 ) and (ball.ycor() < paddle_a.ycor() +40 and ball.ycor() > paddle_a.ycor() -50):
        ball.setx(-340)
        ball.dx *= -1



# Pong Game
# by @kerim
# Add Sound - https://youtu.be/XGf2GcyHPhc?t=2383

import turtle

wn = turtle.Screen()
wn.title("Pong by @Kerim")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0
 
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
ball.color("white") # renk ayarlama
ball.penup()
ball.goto(0, 0) # Konumunu belirlemek icin kullaniyoruz - Normalde tam ortadan basliyor

ball.dx = 0.1 # bu topun her hareketinde 2 birimlik yer degistirecegini gosteriyor
ball.dy = 0.1 # burada ayni zamanda y ekseninde 2 birim hareket etmesi gerektigini tanimladik yani capraz gider

# Scoreboard ekrana yazdirma
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0   Player B: 0", font=("Courier", 20, "normal"), align="center")


# Simdiyaptigimiz seyleri hareket ettirmenin zamani geldi
# Function - Paddlerin hareket etmelerini saglayan fonksiyonlar
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

    # Topun Yukari ve asagi tarafa yonelik hareketerline sinirlar ve kurallarin belirlenmesi
    if ball.ycor() > 290: # Eger ball in y koordinati 290 dan buyuk ise
        ball.sety(290) # Ball in y kordinatini 290 a esitle ve *= -1 ile -> ters yonde devam etmesini sagla
        ball.dy *= -1 # burada ters yonde hareket etmesini sagliyoruz

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # Topun Sag ve sol tarafa yonelik hareketlerine sinirlar ve kurallarin belirlenmesi
    if ball.xcor() > 390: # bu sinirlarin disina cikarsa ortadan basla ve ters yonde devam et
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(score_a, score_b), font=("Courier", 20, "normal"), align="center")

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(score_a, score_b), font=("Courier", 20, "normal"), align="center")

    #Paddle en Ball collisions - Top ile raket in etkilesime girmesi
    if (ball.xcor() > 340 and ball.xcor() < 350 ) and (ball.ycor() < paddle_b.ycor() +40 and ball.ycor() > paddle_b.ycor() -50):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350 ) and (ball.ycor() < paddle_a.ycor() +40 and ball.ycor() > paddle_a.ycor() -50):
        ball.setx(-340)
        ball.dx *= -1
    

    # Scoreboard a yonelik islemler
    if score_a == 5:
        pen.clear()
        pen.write("Player A won!", font=("Courier", 20, "normal"), align="center")
        score_a = 0
        score_b = 0
        
    elif score_b == 5:
        pen.clear()
        pen.write("Player B won!", font=("Courier", 20, "normal"), align="center")
        score_a = 0
        score_b = 0
        



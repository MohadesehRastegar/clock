from turtle import Turtle, Screen
import datetime
import turtle
import time

WinScreen = Screen()
WinScreen.tracer(0)
WinScreen.title("Analog clock by python")
WinScreen.bgcolor("black")
WinScreen.setup(width=1000, height=700)
def fxnnn():
    WinScreen.bgpic("pic4.gif")
    WinScreen.onkey(fxn,"f")
    WinScreen.listen()
def fxnn():
    WinScreen.bgpic("pic2.gif")
    WinScreen.onkey(fxnnn,"f")
    WinScreen.listen()
def fxn():
    WinScreen.bgpic("pic3.gif")
    WinScreen.onkey(fxnn,"f")
    WinScreen.listen()
    #بک گراند مشکی
def cx():
    WinScreen.bgpic("pic1.gif")

WinScreen.onkey(fxn,'f') 
WinScreen.listen()
WinScreen.onkey(cx,"c")
WinScreen.listen()

     
circle = Turtle()
circle.penup()
circle.pensize(30)
circle.pencolor("pink")
circle.speed(0)
circle.hideturtle()
circle.goto(0, -290)
circle.pendown()
circle.circle(290)

t=turtle.Turtle()
t.pen(pencolor="pink")
t.ht()
t.speed(0)
   
hourHand = Turtle()
hourHand.shape("arrow")
hourHand.color("blue")
hourHand.speed(0)
hourHand.shapesize(stretch_wid=0.4, stretch_len=16)
    # عقربه دقیقه شمار
minuteHand = Turtle()
minuteHand.shape("arrow")
minuteHand.color("gold")
minuteHand.speed(0)
minuteHand.shapesize(stretch_wid=0.4, stretch_len=24)
    # عقربه ثانیه شمار
secondHand = Turtle()
secondHand.shape("arrow")
secondHand.color("dark red")
secondHand.speed(0)
secondHand.shapesize(stretch_wid=0.4, stretch_len=26)
    # دایره درونی
insideCircle = Turtle()
insideCircle.shape("circle")
insideCircle.color("gray")
insideCircle.shapesize(stretch_wid=1.5, stretch_len=1.5)

    #one
t.penup()
t.goto(0,0)
t.setheading(60)
t.forward(210)
t.setheading(0)
t.forward(10)
t.write(str( 1 ),align="center",font=("Tahama", 35, "normal"))

    #two
t.penup()
t.goto(0,0)
t.setheading(30)
t.forward(210)
t.setheading(0)
t.forward(30)
t.write(str( 2 ),align="center",font=("Tahama", 35, "normal"))
        

    #three
t.penup()
t.goto(0,0)
t.setheading(353)
t.forward(215)
t.setheading(0)
t.forward(25)
t.write(str( 3 ),align="center",font=("Tahama", 35, "bold"))

    #four
t.penup()
t.goto(0,0)
t.setheading(318)
t.forward(215)
t.setheading(0)
t.forward(45)
t.write(str( 4 ),align="center",font=("Tahama", 35, "normal"))

    #five
t.penup()
t.goto(0,0)
t.setheading(288)
t.forward(242)
t.setheading(0)
t.forward(45)
t.write(str( 5 ),align="center",font=("Tahama", 35, "normal"))

    #six
t.penup()
t.goto(0,0)
t.setheading(270)
t.forward(263)
t.setheading(0)
t.write(str( 6 ),align="center",font=("Tahama", 35, "bold"))

    #seven
t.penup()
t.goto(0,0)
t.setheading(258)
t.forward(242)
t.setheading(180)
t.forward(55)
t.write(str( 7 ),align="center",font=("Tahama", 35, "normal"))

    #eight
t.penup()
t.goto(0,0)
t.setheading(220)
t.forward(240)
t.setheading(180)
t.forward(30)
t.write(str(8),align="center",font=("Tahama",35,"normal"))

    #nine
t.penup()
t.goto(0,0)
t.setheading(186)
t.forward(250)
t.setheading(0)
t.forward(5)
t.write(str(9),align="center",font=("Tahama",35,"bold"))

    #ten
t.penup()
t.goto(0,0)
t.setheading(156)
t.forward(230)
t.setheading(0)
t.forward(5)
t.write(str(10),align="center",font=("Tahama",35,"normal"))

    #eleven
t.goto(0,0)
t.setheading(124)
t.forward(205)
t.setheading(120)
t.forward(14)
t.write(str(11),align="center",font=("Tahama",35,"normal"))

    #twoelve
t.goto(0,0)
t.setheading(90)
t.forward(220)
t.write(str(12),align="center",font=("Tahama",35,"bold"))

t.goto(0,0)
t.pensize(6)
t.speed(0)
for _ in range(12):
    t.fd(180)
    t.pendown()
    t.fd(20)   
    t.penup()
    t.goto(0,0)
    t.rt(30)
t.setheading(90)    
for _ in range(60):
    t.forward(200)
    t.pendown()
    t.forward(10)
    t.penup()
    t.goto(0,0)
    t.right(6)


def main():

    def MovingHourHand():
        InternalHour = datetime.datetime.now().hour
        degree = (InternalHour - 15) * -30
        InternalMinute = datetime.datetime.now().minute
        degree = degree + -0.5 * InternalMinute
        hourHand.setheading(degree)
        WinScreen.ontimer(MovingHourHand, 60000)
        WinScreen.update()
    def MovingMinuteHand():
        InternalMinute = datetime.datetime.now().minute
        degree = (InternalMinute - 15) * -6
        currentSecondInternal = datetime.datetime.now().second
        degree = degree + (-currentSecondInternal * 0.1)
        minuteHand.setheading(degree)
        WinScreen.ontimer(MovingMinuteHand, 1000)
        WinScreen.update()
    def MovingSecondHand():
        currentSecondInternal = datetime.datetime.now().second
        degree = (currentSecondInternal - 15) * -6
        secondHand.setheading(degree)
        WinScreen.ontimer(MovingSecondHand, 1000)
        WinScreen.update()

    WinScreen.ontimer(MovingHourHand, 1)
    WinScreen.ontimer(MovingMinuteHand, 1)
    WinScreen.ontimer(MovingSecondHand, 1)
    WinScreen.update()

pen=Turtle()
def drawgap():
    pen.penup()
    pen.fd(5)

def drawline(draw):
    drawgap()
    pen.pendown() if draw else pen.penup()
    pen.fd(10)
    drawgap()
    pen.right(90)

def drawdigit(digit):
    drawline(True) if digit in [2,3,4,5,6,8,9] else drawline(False)
    drawline(True) if digit in [0,1,3,4,5,6,7,8,9] else drawline(False)
    drawline(True) if digit in [0,2,3,5,6,8,9] else drawline(False)
    drawline(True) if digit in [0,2,6,8] else drawline(False)
    pen.left(90)
    drawline(True) if digit in [0,4,5,6,8,9] else drawline(False)
    drawline(True) if digit in [0,2,3,5,6,7,8,9] else drawline(False)
    drawline(True) if digit in [0,1,2,3,4,7,8,9] else drawline(False)
    pen.left(180)
    pen.penup()
    pen.fd(20)

def drawdate(date):
    
    for i in date:
 
        if i == '*':
   
            pen.pencolor('blue')
            pen.fd(20)
        elif i == '#':

            pen.pencolor('blue')
            pen.fd(20)
        elif i == '&':

            pen.pencolor('blue')
            pen.fd(20)
        
        else:
            drawdigit(eval(i))
            
def digmain():
    pen.up()
    pen.goto(-250,300)
    pen.down()
    pen.pencolor('blue')
    pen.width(5)
    pen.speed(0)
    pen.hideturtle()
    pen.penup()
    pen.fd(-250)

    drawdate(time.strftime('%H*%M#%S&',time.localtime()))

digmain()  

main()
WinScreen.mainloop()
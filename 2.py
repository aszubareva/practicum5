import turtle
xc = int(input())
yc = int(input())
r = int(input())
x = int(input())
y = int(input())

t = turtle.Turtle()
t.speed(3)

#Рисование окружности
t.penup()
t.goto(xc, yc - r)
t.pendown()
t.circle(r)

#Рисование точки
t.penup()
t.goto(x, y)
t.pendown()
t.dot(10, 'red')

d = ((x - xc)**2 + (y - yc)**2)**0.5

if d < r:
    print("Точка внутри окружности")
elif d == r:
    print("Точка на окружности")
else:
    print("Точка вне окружности")

turtle.done()

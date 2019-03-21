import turtle
m=turtle.Turtle()
m.speed(0)
color=['red','green','yellow','blue']
for i in range(200):
    m.color(color[i%4])
    m.forward(i)
    m.right(90)

turtle.done()
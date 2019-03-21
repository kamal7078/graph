import turtle
r=turtle.Turtle()
r.speed(20)
r.getscreen().bgcolor("red")
def draw_petal():
    for i in range(14):
        r.left(360/10)
        r.circle(100,60)
        r.left(120)
        r.circle(100,60)


draw_petal()
turtle.done()



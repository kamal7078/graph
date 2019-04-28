#-------------------------------------------------
# garden_2.py
# Dowloaded from www.bagofcows.com on 26-04-2019
#-------------------------------------------------

from turtle  import *
import random
hideturtle()

#===================================
# draws a rectangle
#===================================
def draw_rectangle(x,y,w,h,colour):
    up()
    goto(x,y)
    down()
    color(colour)
    begin_fill()
    for i in range(2):
        forward(w)
        left(90)
        forward(h)
        left(90)
    end_fill()
#===================================
# draws a triangle
#===================================    
def draw_triangle(x,y,b,h,colour):
    up()
    goto(x,y)
    down()
    color(colour)
    begin_fill()
    goto(x + b/2, y - h)
    goto(x - b/2,y - h)
    goto(x,y)
    end_fill()
   

#===================================
# draws a regular polygon
#===================================
def draw_polygon(x,y,sides,size,colour):
    up()
    goto(x,y)
    down()
    color(colour)
    begin_fill()
    angle = 360 / sides
    for i in range(sides):
        forward(size)
        left(angle)
    end_fill()
#===================================
# draws a circle
#===================================
def draw_circle(x,y,radius,colour):
    up()
    goto(x,y)
    down()
    color(colour)
    begin_fill()
    circle(radius)
    end_fill()



#===================================
# This makes the first type of flower
#===================================
def flower(x,y):
    down()
    draw_rectangle(x,y,5,30,"brown")    # a brown stem
    draw_circle(x-5,y + 10,5,"green")   # two green leaves
    draw_circle(x+10,y + 10,5,"green")
    draw_circle(x+2,y+20,10,"pink")       # pink petals
    draw_circle(x+2,y+25,5,"red")         # red middle
    up()
    goto(x,y)



#===================================
# YOU CHANGE THIS
# to make the second type of flower
#===================================
def flower2(x,y):
    up()
    goto(x,y)
    down()
    # set a thick green line
    color("green")
    width(4)
    left(60)
    # draw some stems
    for i in range(3):
        forward(30)
        backward(30)
        left(30)
    # then the petals on top
    width(1)
    draw_circle(x+5, y+50,10,"red")
    draw_circle(x+2, y+45,5,"blue")
    up()
    # point back the way we started
    setheading(0)
    
    

#===================================
# YOU CHANGE THIS
# to make the third type of flower
#===================================
def flower3(x,y):
    up()
    goto(x,y)
    down()
    draw_circle(x,y,8,"blue")
    # set a thin green line
    color("green")
    width(2)
    setheading(30)
    # choose a random angle 
    angle = random.randint(10,15)
    # draw some stems
    while heading() < 150:
        forward(40)
        fillcolor(random.choice(["red","yellow","orange"]))
        begin_fill()
        circle(5)
        end_fill()
  #      color("green")
        backward(40)
        left(angle)
    setheading(0)

#===================================
# YOU CHANGE THIS
# This makes a shed that needs improvement
#===================================
def shed(x,y,w,h,):
    draw_triangle(x,y,w,h/2,"grey")
    draw_rectangle(x - w/2 +10,y-h,w -20,h/2,"brown")
    # draw a set of windows
    for i in range(30,180,30):
        draw_rectangle(x - w/2 + i,y-h + 30,26,50,"#FFCCFF")
    # draw the door
    draw_rectangle(x +w/2 - 60 ,y-h,40,h/2 - 10,"#CC0066")
    

#===================================
# YOU ADD YOUR TREE HERE
#===================================
def tree(x,y):
    draw_rectangle(x-5,y,10,100, "brown")
    draw_triangle(x,y+100,100,50,"green")
    draw_triangle(x,y+120,100,50,"green")
    draw_triangle(x,y+140,100,50,"green")


choice = numinput("Choose", "Enter 1,2 or 3 to test your flower functions, 4 for the shed, 5 for the tree, or 0 draw the garden")
if choice == 1:
    flower(0,0)
elif choice == 2:
    flower2(0,0)
elif choice == 3:
    flower3(0,0)
elif choice == 4:
    shed(0,0,300,200)
elif choice == 5:
    tree(-30,0)
else:
    # speed as fast as possible
    speed(0)
    
    # set the whole screen colour
    bgcolor("orange")
    # draw the lawn
    draw_rectangle(-300,-200,600,400,"#336633")
    # draw the shed
    shed(-30,350,300,200)
    # some trees
    tree(200,190)
    tree(300,190)
    tree(320,190)
    tree(260,180)
    tree(230,170)
    
    # a pond
    draw_circle(100,-200,50,"#66CCFF")
    draw_circle(150,-180,50,"#66CCFF")
    draw_circle(180,-170,50,"#66CCFF")
    draw_circle(200,-180,50,"#66CCFF")
    draw_circle(175,-160,30,"#336633")

    numflowers = int(numinput("Choose","How many flowers would you like?"))
    # this makes it do 10 flowers
    for i in range(numflowers):
        # choose a random place to put it
        pos_x = random.randint(-300,300)
        pos_y = random.randint(-200,100)
        
        # check to see if it would be in the pond. If so
        # put it in the island
        if pos_x > 75 and pos_y < -130:
            pos_x = 175 + random.randint(-10,10)
            pos_y = -130 + random.randint(-10,10)

        
        # choose what type it should be
        flower_type = random.randint(1,3)
        # chose a different function for each type
        if flower_type == 1:
            flower(pos_x,pos_y)
        elif flower_type == 2:
            flower2(pos_x,pos_y)
        elif flower_type == 3:
            flower3(pos_x,pos_y)

    

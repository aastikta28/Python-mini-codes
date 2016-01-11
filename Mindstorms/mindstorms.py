import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_triangle(some_turtle):
    for i in range(1,4):
        some_turtle.forward(100)
        some_turtle.left(120)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()

    for i in range(1,37):
        draw_triangle(brad)
        brad.right(10)
    
##    brad = turtle.Turtle()
##    for i in range(1,37):
##        draw_square(brad)
##        brad.right(10)
##    
    #angie = turtle.Turtle()
    #angie.circle(100)
    
    window.exitonclick()

draw_art()

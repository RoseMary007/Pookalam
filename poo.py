import turtle
import math

# setup screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Pookalam Design")

t = turtle.Turtle()
t.speed(0)
turtle.colormode(255)

# function to draw a centered circle
def draw_circle(color, radius, x, y):
    t.penup()
    t.goto(x, y - radius)   # move to the correct position so circle is centered
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

#darkgreen
draw_circle((15, 54, 12), 320, 0, 0)

#yellow
draw_circle((241, 209, 23), 300, 0, 0)

#magenta
draw_circle((150, 37, 93), 250, 0, 0)

# outer dark green circle
draw_circle((15, 54, 12), 200, 0, 0)

# white dots on border
for angle in range(0, 360, 24):
    x = 180 * math.cos(math.radians(angle))
    y = 180 * math.sin(math.radians(angle))
    draw_circle((241, 209, 23), 20, x, y)

# orange ring
draw_circle((238, 106, 30), 160, 0, 0)

# yellow base circle
draw_circle((241, 209, 23), 120, 0, 0)

t.color((95, 26, 95))  # purple from #5F1A5F
for angle in range(0, 360, 30):   # repeat around the circle
    t.penup()
    t.goto(0, 0)
    t.setheading(angle)
    t.forward(120)   # radius just inside orange
    t.pendown()
    t.begin_fill()
    t.circle(40, 180)  # semicircle (radius=40, half circle)
    t.end_fill()



# flower petals (purple)
t.color((157, 12, 43))
for angle in range(0, 360, 30):
    t.penup()
    t.goto(0, 0)
    t.setheading(angle)
    t.forward(60)
    t.pendown()
    t.begin_fill()
    t.circle(60, 60)
    t.left(120)
    t.circle(40, 60)
    t.end_fill()

# inner green circle (inside yellow)
draw_circle((57, 89, 31), 50, -20, 90)

# inner yellow circle (inside green)
draw_circle((241, 209, 23), 35, -12, 60)

t.color("white")  # semicircle color
for angle in range(0, 360, 30):   # repeat around
    t.penup()
    t.goto(0, 0)
    t.setheading(angle)
    t.forward(200)   # distance from center (adjust to fit inside circle)
    t.right(90)      # rotate so semicircle faces center
    t.pendown()
    t.begin_fill()
    t.circle(50, 180)   # semicircle facing inward
    t.end_fill()


t.hideturtle()
turtle.done()

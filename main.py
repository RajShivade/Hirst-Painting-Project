#import colorgram

#rgb_colors = []
#colors = colorgram.extract('spotdot.jpg', 30)
#for color in colors:
#    r = color.rgb.r
#    g = color.rgb.g
 #   b = color.rgb.b
  #  new_color = (r, g, b)
   # rgb_colors.append(new_color)

#print(rgb_colors)


import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(230, 222, 218), (231, 224, 228), (223, 221, 228), (218, 173, 125), (159, 181, 190), (134, 73, 53), (50, 103, 154), (118, 81, 92), (179, 142, 152), (162, 104, 151), (42, 47, 66), (128, 174, 115), (83, 96, 183), (67, 9, 27), (82, 133, 107), (52, 63, 78), (228, 189, 141), (194, 91, 72), (220, 226, 221), (62, 49, 38), (115, 41, 56), (91, 143, 118), (70, 67, 52), (209, 181, 189), (181, 185, 210), (209, 183, 178), (89, 55, 47), (183, 201, 179), (172, 199, 204), (41, 73, 83)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)




screen = turtle_module.Screen()
screen.exitonclick()
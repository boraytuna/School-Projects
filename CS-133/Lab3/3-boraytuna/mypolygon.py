import turtle
import math
bob = turtle.Turtle()

############
# EXERCISE 1
# Write a function called square_one that takes a parameter named t, which is a turtle. It should use the turtle to draw a square.
# Write a function call that passes bob as an argument to square_one, and then run the program again.
############

def square_one(t):
    # Drawing the four sides using a for loop
    for i in range(4):
        t.forward(100)
        t.left(90)

#square_one(bob)


############
# EXERCISE 2
# Write a function called square_two (based on square_one) but add another parameter, named length.
# Modify the body so length of the sides is length, and then modify the function call to provide a second argument.
# Run the program again. Test your program with a range of values for length.
############

def square_two(t, length):
    # Drawing the four sides using a for loop
    for i in range(4):
        t.forward(length) # Using the second argument
        t.left(90)

# square_two(bob,100)
# square_two(bob,20)
# square_two(bob,175)


############
# EXERCISE 3
# Copy your code from square_two into polygon below.
# Modify the code to add another parameter named n so it draws an n-sided regular polygon.
# Hint: The exterior angles of an n-sided regular polygon are 360/n degrees.
############

def polygon(t, n, length):
    #Find the angle of rotation that is needed to complete the polygon
    angle = 360 / n
    # Using for loop for n sided polygons
    for i in range(n): 
        t.forward(length)
        t.left(angle)

#polygon(bob, 9, 70)


############
# EXERCISE 4
# Write a function called circle that takes a turtle (t) and radius (r) as parameters
# The function should draw an approximate circle by calling polygon with an appropriate length and number of sides.
# Test your function with a range of values of r.
# Hint: figure out the circumference of the circle and make sure that length * n = circumference.
############

def circle(t, r):
    circumference = 2 * math.pi * r #Set circumference
    n = 50 # number of sides
    length = circumference / n # length of each side
    polygon(t, n, length)


# circle(bob,30)
# circle(bob,140)


############
# EXERCISE 5
# Make a more general version of circle called arc that takes an additional parameter angle.
# Angle determines what fraction of a circle to draw.
# Angle is in units of degrees, so when angle=360, arc should draw a complete circle.
############

def polyline(t, n, length, angle):
    # Using for loop to draw 
    for i in range(n):
        t.forward(length)
        t.left(angle)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1 # Calculate the number of sides
    step_length = arc_length / n # Calculate the length
    step_angle = float(angle) / n # Calculate the angle for rotating
    polyline(t, n, step_length, step_angle) # Call the polyline function

#arc(bob, 100, 360)

############
# Rewrite polygon (from Exercise 3) to use polyline, name it polygon_refactored.
############

def polygon_refactored(t, n, length):
    angle = 360 / n # Find the angle needed
    polyline(t, n, length, angle) # Call the polyline function

#polygon_refactored(bob, 7, 70)

############
#  Rewrite circle to use arc, name it circle_refactored.
############

def circle_refactored(t, r):
    arc(t, r, 360) # Call the arc function

#circle_refactored(bob,200)


turtle.mainloop()

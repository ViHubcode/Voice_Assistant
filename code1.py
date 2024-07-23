import turtle

# Create a turtle object
t = turtle.Turtle()

# Draw a square
for _ in range(400):
    t.forward(100)  # Move forward by 100 units
    t.right(70)     # Turn right by 90 degrees

# Close the turtle graphics window when clicked
turtle.done()

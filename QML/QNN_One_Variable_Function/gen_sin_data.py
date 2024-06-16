import math

# Define the range and step size
start = 0
end = 2 * math.pi
step = 0.002

# Open a text file for writing
with open("sin.csv", "w") as file:
    # Write the header
    file.write("x,sin(x)\n")

    # Loop through the range and write values to the file
    x = start
    while x <= end:
        file.write("{:.9f},{:.9f}\n".format(x, math.sin(x)))
        x += step

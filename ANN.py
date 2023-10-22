

x_values = []
y_values = []
bias = []

while True:
    x_input = input("Enter a value for x (or 'f' to finish): ")
    if x_input == "f":
        break
    y_input = input("Enter a value for y: ")

    x_values.append(x_input)
    y_values.append(y_input)
    bias.append(1)

def iw(x,y,b):
    output= (x * wx) + (y * wy) + (b * wb)
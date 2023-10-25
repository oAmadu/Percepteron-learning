Err_values = []
target = []
x_values = []
y_values = []
bias = []
S_values = []
ic = 0 # counting number of iterations

while True:
    x_input = input("Enter a value for x (or 'f' to finish): ") # enters X1 values
    if x_input == "f":
        break
    y_input = input("Enter a value for y: ") # Enters X2 values
    target_input = input("Enter a value for the target: ")

    x_values.append(float(x_input))
    y_values.append(float(y_input))
    bias.append(float(1))  # convert bias to float (all is 1's)
    target.append(float(target_input))

Thresh = float(input("Enter the value of the threshold: ")) # Threshold input
LR = float(input("Enter learning rate's value (if there isn't just enter 1): ")) #Learning rate input
wx = float(input("Enter value of the initial weight for x: "))
wy = float(input("Enter value of the initial weight for y: "))
wb = float(input("Enter value of the initial weight for bias: "))

num_items = len(x_values)  # Number of items in x, y, bias
all_errors_zero = False  # All erors aren't zero (So we have to start the algo)

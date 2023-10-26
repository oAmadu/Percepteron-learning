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
    bias.append(float(1))  # add 1 for each input
    target.append(float(target_input))

Thresh = float(input("Enter the value of the threshold: ")) # Threshold input
LR = float(input("Enter learning rate's value (if there isn't just enter 1): ")) # Learning rate input
wx = float(input("Enter value of the initial weight for x: "))
wy = float(input("Enter value of the initial weight for y: "))
wb = float(input("Enter value of the initial weight for bias: "))

num_items = len(x_values)  # Number of items in x, y, bias
all_errors_zero = False  # All errors aren't zero (So we have to start the algo)

while not all_errors_zero:
    all_errors_zero = True  # Assume all errors are zero

    Err_values = []  # Reset the list for each iteration

    for i in range(num_items):
        S = x_values[i] * wx + y_values[i] * wy + bias[i] * wb
        S_values.append(S)

        if S > Thresh:
            O = 1
        else:
            O = 0

        Err = target[i] - O
        wx = wx + LR * Err * x_values[i]
        wy = wy + LR * Err * y_values[i]
        wb = wb + LR * Err * bias[i]

        Err_values.append(Err)  # Add the error to Err_values list
        ic += 1  # add 1 for each iteration

        if Err != 0:
            all_errors_zero = False

    if all(err == 0 for err in Err_values):
        break

    # Reset the S list for the next iteration
    S_values = []


print("\nThe appropriate weights are ", wx, wy, wb)
print(" Number of iterations:", ic/4)

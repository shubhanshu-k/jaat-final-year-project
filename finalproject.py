

def print_JAAT_in_line():
    for row in range(7):
        # Print J
        for col in range(5):
            if (col == 3) or (row == 6 and 0 < col < 4) or (row > 3 and col == 0):
                print("**", end="")
            else:
                print("  ", end="")

        # Space between J and A
        print("  ", end="")

        # Print A
        for col in range(5):
            if (col == 0 or col == 4) or (row == 0 or row == 3):
                if (row == 0 and (col == 0 or col == 4)):
                    print("  ", end="")
                else:
                    print("**", end="")
            else:
                print("  ", end="")

        # Space between A and A
        print("  ", end="")

        # Print A again
        for col in range(5):
            if (col == 0 or col == 4) or (row == 0 or row == 3):
                if (row == 0 and (col == 0 or col == 4)):
                    print("  ", end="")
                else:
                    print("**", end="")
            else:
                print("  ", end="")

        # Space between A and T
        print("  ", end="")

        # Print T
        for col in range(5):
            if row == 0 or col == 2:
                print("**", end="")
            else:
                print("  ", end="")

        # Move to the next line after finishing a row for all letters
        print()

    # Adding empty lines after printing the letters
    print()  # Adds one empty line
    print()  # Adds another empty line

num1 = float(input("Enter the first number:\n"))

# Taking second number input from the user
num2 = float(input("Enter the second number:\n"))
print()
# Calculating the sum of the two numbers
sum_result = num1 + num2
print_JAAT_in_line() 

input("\nPress any key to continue...")

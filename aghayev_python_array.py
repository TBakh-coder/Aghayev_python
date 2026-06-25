# I define a function named 'main'. This groups our code together and makes code tidy. It also allows us to call the function later in the code.
def main():
# 'try:' starts a protected section of code. If anything inside fails, it jumps to line 15.

    try:
# 1. Get the numbers from the user
        array_input = input("Enter a list of numbers " + "\033[1m" + "(SPACE " + "\033[0m" + "seperated):")

# 2. Turn the text into a list of numbers
        numeric_array = [int(x) for x in array_input.split()]
        print("Multiplies of" + "\033[1m" + " 3 " + "\033[0m")

# 3. Check each number
        for element in numeric_array:
            mult = int(element/3)
            if element %3 == 0:
                print(element, " (multiplier: " + str(mult) + ")")
    except ValueError as e:

        print ("An error occurred: ", e);
main()

#Made by Bakhtiyar Aghayev
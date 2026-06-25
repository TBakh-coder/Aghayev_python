# I define a function named 'main'. This groups our code together and makes code tidy. It also allows us to call the function later in the code.
def main():
    # protected section of code with try-except.
    try:
        # 1. Get user input and immediately convert it to a float decimal
        number = float(input("Enter a number: "))

        # 2. Check the condition directly using the float
        if int(number) > 7:
            print ("Hello");
        else:
            print ("Number is not greater than 7");
    
    # 3. Catch instances where text was entered instead of a number
    except ValueError as e:
        print ("an error occurred: ", e);

# 4. Trigger the function
main()

#Made by Bakhtiyar Aghayev
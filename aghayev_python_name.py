# I define a function named 'main'. This groups our code together and makes code tidy. It also allows us to call the function later in the code.
def main():
        # 1. Get the name (input is already a string by default)
        name = str(input("Enter the Name:"))

        # 2. Check the condition
        if name == "John":
            print ("Hello", name);
        elif name != "John":
            print ("There is no such name");

# 3. Call the function to run it
main()

#Made by Bakhtiyar Aghayev
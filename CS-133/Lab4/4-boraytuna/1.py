"""
Write a program that asks the user for their name and says hello to them.

Remember to document your code!

The output should look like this:

Enter your name: Chris
Hello Chris!
"""

def your_name():
    """
    This function reads the input of the user and prints out the input with another string
    """
    user_input = str(input("Enter your name: ")) # Read the input
    while user_input == "" or user_input is None: # Make sure the user inputs their name
        user_input = str(input("Please enter your name: "))
    if user_input is not None: # When there is an input printout the statement
        print ("Hello", user_input + "!")


# Run the function
your_name()


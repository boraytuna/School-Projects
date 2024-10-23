"""
Write a program that prompts the user to enter two integers and display the total on the screen.

Remember to document your code!

The output should look like this:

Enter integer one: 3
Enter integer two: 1
Total: 4
"""

def get_integer(prompt):
    """
    Helper function to get a valid integer from the user.
    """
    while True:
        try:
            return int(input(prompt))  # Try to convert the input to an integer
        except ValueError:
            print("Invalid input. Please enter a valid integer.")  # Error message for invalid input

def two_integers():
    """
    This function returns the sum of two integers entered by the user.
    """
    first_integer = get_integer("Enter the first integer: ")  # Get the first integer
    second_integer = get_integer("Enter the second integer: ")  # Get the second integer

    total = first_integer + second_integer  # Add the integers together
    print(f"Total: {total}")

# Run the function
two_integers()
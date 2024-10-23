"""
Write a program that accepts a non-zero positive integer. The program should then sum all numbers from 1 through that provided number (inclusively). That means an entry of 4 should add 1+2+3+4.

If the user provides a zero or a negative number, the program should output an error message "Try again!" and quit.

Remember to document your code!

Your output should like this:

Enter a non-zero positive integer: 3
The sum of all numbers from 1 through 3 is: 6

Enter a non-zero positive integer: -5
Try again!
"""

def get_integer(prompt):
    """
    Helper function to get a valid non-zero positive integer from the user.
    """
    while True:
        try:
            value = int(input(prompt))  # Try to convert the input to an integer
            if value <= 0:
                print("Try again!")  # If value is zero or negative, print error message
                return None  # Exit the loop and return None to indicate invalid input
            else:
                return value  # Return the valid non-zero positive integer
        except ValueError:
            print("Invalid input. Please enter a valid integer.")  # Error message for invalid input


def non_zero_integer():
    """
    This function to accepts a non-zero positive integer and sum all numbers from 1 to the given number.
    """
    user_input = get_integer("Enter a non-zero positive integer: ") # Read user input

    if user_input is not None:  # If a valid number is provided
        total_sum = sum(range(1, user_input + 1))  # Sum from 1 to user input (inclusive)
        print(f"The sum of all numbers from 1 through {user_input} is: {total_sum}")


# Run the function
non_zero_integer()

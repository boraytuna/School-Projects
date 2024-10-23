"""
Write a program that accepts an integer from input. Your program should convert the entered integer (which is a number of seconds) into hours, minutes and seconds.

Remember to document your code!

Your output should like this:

Enter seconds: 3809
Hours: 1
Minutes: 3
Seconds: 29
"""


def get_integer(prompt):
    """
    Helper function to get a valid non-negative integer from the user.
    """
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Invalid input. Please enter a non-negative integer.")  # Error message for negative numbers
                continue
            return value  # Return valid non-negative integer
        except ValueError:
            print("Invalid input. Please enter a valid integer.")  # Error message for invalid input


def seconds_to_hours():
    """
    This function reads user input (seconds) and converts it to hours, minutes, and seconds.
    """
    total_seconds = get_integer("Enter seconds: ")  # Read user input
    hours = total_seconds // 3600  # Calculate hours
    minutes = (total_seconds % 3600) // 60  # Calculate minutes
    seconds = total_seconds % 60  # Calculate remaining seconds

    # Ensure output matches expected format
    print(f"Hours: {hours}")
    print(f"Minutes: {minutes}")
    print(f"Seconds: {seconds}")


# Run the function
seconds_to_hours()

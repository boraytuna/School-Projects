"""
Write a program that prompts the user to input a Celsius temperature and outputs the equivalent temperature in Fahrenheit.

The formula to convert the temperature is:
F = (C * 9/5) + 32 where
F is the Fahrenheit temperature and
C is the Celsius temperature

Remember to document your code!

The output should look like this:

Enter Celsius temp: 33.2
Fahrenheit temp: 91.76
"""

def get_float(prompt):
    """
    Helper function to get a valid float from the user.
    """
    while True:
        try:
            return float(input(prompt))  # Try to convert the input to a float
        except ValueError:
            print("Invalid input. Please enter a valid float.")  # Error message for invalid input

def celsius_to_fahrenheit():
    """
    This function takes in float as Celsius degree and returns the degree in Fahrenheit.
    """
    celsius = get_float('Enter Celsius temp: ')
    fahrenheit = (celsius * 1.8) + 32
    print("Fahrenheit temp:" , fahrenheit)

# Run the function
celsius_to_fahrenheit()
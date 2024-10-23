def form():
  """ The form function that collects info from users

  Returns:
  - A string that says whether the form succeeded or not
  """
  # Collect the user's street number
  street_num = input("Enter the street number of your address: ")
  street_num = test_street_num(street_num)
  if street_num == False:
    return "Form failed: Restart the form!"

  # Collect the user's age
  age = input("Enter your age: ")
  age = test_age(age) # Finish this function below!
  if age == False:
    return "Form failed: Restart the form!"

  # Collect the user's reason of visit
  reason = input("Enter your reason of visit: ")
  reason = test_reason_for_visit(reason)
  if reason == False:
    return "Form failed: Restart the form!"

  # Collect the user's phone number
  phone_num = input("Enter your phone number as the following example 1234567890: ")
  phone_num = test_phone_number(phone_num)
  if phone_num == False:
    return "Form failed: Restart the form!"

  # Collect how the user's email
  email = input("Enter your email: ")
  email = test_email(email)
  if email == False:
    return "Form failed: Restart the form!"


  # Then, print out all our collected info in a form
  print("=====================")
  print("We've collected the following information:")
  print("- Street Number:", street_num)
  print("- Age:", age)
  print("- Reason of Visit:", reason)
  print("- Phone Number:", phone_num)
  print("- Email:", email)
  print("=====================")

  return "Form complete!"

def test_street_num(street_num):
  """ EXAMPLE: Gets the user's street number.

  Arguments:
  - street_num - the street number of the user
  Returns:
  - False if the input is incorrect
  - the integer street number if it is correct
  """
  # Check to see if it's empty!
  if street_num.strip() == "":
    print("SORRY! You forgot to enter your number!\n")
    return False
  # Check to see if it's a positive number!
  elif street_num.isdigit() == False:
    print("SORRY! Your number should be a positive number\n")
    return False
  else:
    return street_num

def test_age(age):
  """ Gets the user's age.

  Arguments:
  - age - the age of the user
  Returns:
  - False if the input is incorrect
  - the integer age if it is correct
  """
  # Check to see if it's empty!
  if age.strip() == "":
    print("SORRY! You forgot to enter your age!\n")
    return False
  # Check to see if it's a positive number!
  elif age.isdigit() == False:
    print("SORRY! Your number should be a positive number\n")
    return False
  else:
    return age

def test_reason_for_visit(reason):
    """ Gets the user's reason of visit.

    Arguments:
    - reason: the reason of the visit
    Returns:
    - False if the input is incorrect
    - the string reason of visit if it is correct
    """
    # Check if the input is a string
    if not isinstance(reason, str):
      print("SORRY! Your input should be a string.\n")
      return False
    # Check to see if it's empty!
    elif reason.strip() == "":
      print("SORRY! You forgot to enter your reason!\n")
      return False
    # Check to see if the input consist of only alphabetic characters and spaces
    elif not all(char.isalpha() or char.isspace() for char in reason):
      print("SORRY! Your reason should consist of words and spaces only (no numbers or symbols).\n")
      return False
    else:
      return reason


def test_phone_number(phone_num):
  """Gets the user's phone number.

  Arguments:
  - phone_num: the phone number of the user.

  Returns:
  - False if the input is incorrect.
  - False if the input length is not 10 (normal phone number length).
  - the integer phone number if it is correct.
  """
  input_len = len(phone_num)  # Store the length of the argument

  # Check if the input is empty
  if phone_num.strip() == "":
    print("SORRY! You forgot to enter your phone number!\n")
    return False
  # Check to see if it's a positive number!
  elif not phone_num.isdigit():
    print("SORRY! Your number should be a positive number (digits only).\n")
    return False
  # Check if the phone number has exactly 10 digits
  elif input_len != 10:
    print("SORRY! Your phone number should have exactly 10 digits.\n")
    return False
  else:
    return int(phone_num)  # Return the phone number as an integer

def test_email(email):
    """Gets the user's email.

    Arguments:
    - email: the email address of the user.

    Returns:
    - False if the input is incorrect.
    - the string email if it is correct.
    """
    # Check if the input is empty
    if email.strip() == "":
      print("SORRY! You forgot to enter your email!\n")
      return False
    # Check for a basic valid email pattern
    # Check if "@" is in the string and "." is after the "@"
    elif "@" not in email or "." not in email.split("@")[-1]:
      print("SORRY! Your email should be valid (e.g., example@mail.com).\n")
      return False
    else:
      return email

# Runs the main program
print( form() )


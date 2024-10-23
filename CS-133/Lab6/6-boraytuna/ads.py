"""
Problem 1 - Dog Food Ad
"""

def owns_dog():
    """
    This function asks the user if they own a dog or not.
    It returns true if they own a dog and prompts according ad,
    otherwise it returns false and prompts according ad.
    """
    answer = input("Do you own a dog? ") # Ask the user the question
    if answer.lower() == "yes":
        # Prompt dog ad
        dog_ad(True)
    else:
        # Prompt another ad
        dog_ad(False)

def dog_ad(x):
    if x:
        # If the user owns a dog, show a dog food ad
        print("Dog Food Ad: Meat’s the need of dogs like yours! The ALL-MEAT dinner for dogs, WOOF.")
    else:
        # If the user doesn't own a dog, show an ad for something else
        print("Ad: Dirty mouth? Clean it up with new Orbit Raspberry Mint. For a good clean feeling, no matter what!")

"""
Problem 2 - Dog/Cat Ads
"""

def int_question(x):
    """
    This function asks the user to enter a number,
    if the number is not an integer greater than or equal to 0
    this function prints an informative message.
    """
    answer = input(x) # Ask the user the question

    # Check if the user's answer is a non-negative integer
    if answer.isdecimal():
        # Convert the valid answer to an integer and return it
        return int(answer)
    else:
        # If the answer is not valid, print an error message and return 0
        print("Not a number! Converting answer to 0.")
        return 0

def friends_ad(number):
    if number >= 500:
        # If the user has 500 or more friends prompt the dog ad
        print("Ad with Dog: Get your cat food today!")
    else:
        # If the user has less than 500 friends prompt the cat ad
        print("Ad with Cat: Get your cat food today!")

"""
Problem 3 - Location/Age Ads
"""

def zip_age_ad(zipcode, age):
    """
    This checks if the inputted zipcode and age match the specific ones.
    Based on the match it prints out different types of adds
    :param zipcode: is an integer
    :param age: is an integer
    """
    if (zipcode == 14706 or zipcode == 14778) and age >= 25: # If the zipcode matches and age is over the limit
        print("Expensive Product Ad: Get your new phone today!")
    elif (zipcode == 14706 or zipcode == 14778) and age < 25: # If the zipcode matches and age is under the limit
        print("Cheap Product Ad: Buy a watermelon")
    else:   # If the zipcode doesn't match
        print("Tourist Ad: Come visit SBU!")

"""
Problem 4 - Custom Ads
"""

def custom_ads(gender, age, relationship, number_of_friends):
    """
    This function takes four parameters (gender, age, relationship, and number_of_friends)
    and prints a personalized ad based on these inputs:
    - If the user is a man, single, and has fewer than 500 friends, they receive an ad for men's grooming products.
    - If the user is a woman, single, and has fewer than 500 friends, they receive an ad for women's beauty products.
    - If the user is either man or woman and in a relationship, they receive an ad for gifts for their partner.
    - If the user's age is less than 25, they receive a default ad indicating they are too young for the site.
    """
    while age >= 25: # While the age is equal or more than 25, print these ads
        if gender.lower() == "man" and (relationship.lower() == "single" or number_of_friends < 500):
            print("Custom Ad [1]: Men's grooming essentials! Get the best care for yourself today.")
            break
        elif gender.lower() == "woman" and (relationship.lower() == "single" or number_of_friends < 500):
            print("Custom Ad [2]: Women's beauty products are found here!")
            break
        elif (gender.lower() == "woman" or gender.lower() == "man") and relationship == "taken":
            print("Custom Ad [3]: Get your loved one a gift!")
            break
    else:   # If age is less than 25, print this ad
        print("Custom Ad [4]: Too young to shop on this website!")

"""
Problem 5 - Completing Your Program
"""
def ads_prompter():
    """
    This function prompts the user to choose how personalized the ad should be.
    Based on the user's choice, it calls the appropriate function to display a targeted ad.
    1 - Asks if the user owns a dog and displays a dog-related ad or a general ad.
    2 - Asks for the number of friends and displays a dog/cat ad based on that number.
    3 - Asks for the user's zipcode and age, and displays a product ad based on the location and age.
    4 - Asks for personal details like gender, age, relationship status, and number of friends, and displays a custom ad based on these inputs.
    """
    answer = int(input("How personalized should the ad be? (1 - 4): "))  # Ask the user how personalized the ad should be
    if answer == 1:
        owns_dog()
    elif answer == 2:
        num_friends = int_question("How many friends do you have? ")
        friends_ad(num_friends)
    elif answer == 3:
        zipcode = int_question("What zip code do you live in? ")
        age = int_question("How old are you? ")
        zip_age_ad(zipcode, age)
    elif answer == 4:
        gender = input("What is your gender? (man/woman) ")
        age = int_question("How old are you? ")
        relationship = input("What is your relationship status? (single/taken) ")
        number_of_friends = int_question("How many friends do you have? ")
        custom_ads(gender, age, relationship, number_of_friends)

# Call the function
ads_prompter()
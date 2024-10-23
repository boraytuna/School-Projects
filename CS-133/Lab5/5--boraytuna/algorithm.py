# Keeps track of the point total during questions
current_score = 0

# A header to start the program
print("-------------------------------")
print("   HOUSING SCORE CALCULATOR")
print("-------------------------------")
print()

# Question 1
def how_many_credits_total():
    """
    This function asks the user the number of credits they have and adds 1 point for 0-29 credits,
    2 points for 30-59, 3 points for 60-89, 4 points for 90-120 and 5 points for 120+.
    """
    print("QUESTION 1")
    global current_score  # Access the global var for the current score

    # Read user input
    credit = int(input("How many credits do you have: "))

    if 0 <= credit <= 29:
        current_score += 1
    elif 30 <= credit <= 59:
        current_score += 2
    elif 60 <= credit <= 89:
        current_score += 3
    elif 90 <= credit <= 120:
        current_score += 4
    elif credit > 120:
        current_score += 5

    return current_score

# Question 2
def how_many_semester():
    """
    This function asks the reader how many semesters they have studied in the school.
    It takes in an int and returns that int times 0.5 and adds it to the current score.
    """
    print("QUESTION 2")
    global current_score  # Access the global var for the current score

    # Read user input
    semester = int(input("How many semesters have you studied in this school: "))

    # Calculate the points and add them to current score
    current_score += semester * 0.5
    return current_score

# Question 3
def do_you_have_disability():
    """
    This function asks the user if they have any disability. If they do, they get 1 point.
    If they say yes, a new question is prompted. The new question asks if they need to live on the first floor.
    If they say yes, they get 5 additional points.
    """
    print("QUESTION 3")
    global current_score  # Access the global var for the current score

    while True:
        has_disability = input("Do you have any disability? (y/n): ").strip().lower()

        if has_disability == 'y':
            current_score += 1
            while True:
                do_you_need_to_live_on_first_floor = input("Do you need to live on the first floor? (y/n): ").strip().lower()
                if do_you_need_to_live_on_first_floor == 'y':
                    current_score += 5
                    break
                elif do_you_need_to_live_on_first_floor == 'n':
                    break
                else:
                    print("Invalid input. Please enter 'y' or 'n'.")
            break
        elif has_disability == 'n':
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

    return current_score

# Question 4
def are_you_student_athlete():
    """
    This function asks the user if they are a student athlete.
    If yes, add 2 points to current score.
    If no, do not add points to current score.
    """
    print("QUESTION 4")
    global current_score  # Access the global var for the current score

    while True:
        is_student_athlete = input("Are you a student athlete? (y/n): ").strip().lower()

        if is_student_athlete == 'y':
            current_score += 2
            break
        elif is_student_athlete == 'n':
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

    return current_score

# Question 5
def are_you_resident_assistant():
    """
    This function asks the user if they are a resident assistant.
    If yes, add 1 point to current score.
    If no, do not add points to current score.
    """
    print("QUESTION 5")
    global current_score  # Access the global var for the current score

    while True:
        is_ra = input("Are you a resident assistant? (y/n): ").strip().lower()

        if is_ra == 'y':
            current_score += 1
            break
        elif is_ra == 'n':
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

    return current_score

# Question 6
def academic_probation():
    """
    This function asks the user if they have been on academic probation last year.
    If yes, remove 1 point from current score.
    If no, do not add points to current score.
    """
    print("QUESTION 6")
    global current_score  # Access the global var for the current score

    while True:
        ap = input("Have you been on academic probation last year? (y/n): ").strip().lower()

        if ap == 'y':
            current_score -= 1
            break
        elif ap == 'n':
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

    return current_score

# Question 7
def disciplinary_probation():
    """
    This function asks the user if they have been on disciplinary probation last year.
    If yes, remove 3 points from current score.
    If no, do not add points to current score.
    """
    print("QUESTION 7")
    global current_score  # Access the global var for the current score

    while True:
        dp = input("Have you been on disciplinary probation last year? (y/n): ").strip().lower()

        if dp == 'y':
            current_score -= 3
            break
        elif dp == 'n':
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

    return current_score

# Question 8
def are_you_transfer_student():
    """
    This function asks the user if they are a transfer student.
    If yes, add 1 point to current score.
    If no, do not add points to current score.
    """
    print("QUESTION 8")
    global current_score  # Access the global var for the current score

    while True:
        is_transfer = input("Are you a transfer student? (y/n): ").strip().lower()

        if is_transfer == 'y':
            current_score += 1
            break
        elif is_transfer == 'n':
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

    return current_score

# Question 9
def are_you_employed_over_twenty_hours():
    """
    This function asks the user if they are employed over twenty hours.
    If yes, add 1 point to current score.
    If no, do not add points to current score.
    """
    print("QUESTION 9")
    global current_score  # Access the global var for the current score

    while True:
        employed = input("Are you employed over 20 hours in a week? (y/n): ").strip().lower()

        if employed == 'y':
            current_score += 1
            break
        elif employed == 'n':
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

    return current_score

# Question 10
def are_you_first_gen_college_student():
    """
    This function asks the user if they are a first generation college student.
    If yes, add 1 point to current score.
    If no, do not add points to current score.
    """
    print("QUESTION 10")
    global current_score  # Access the global var for the current score

    while True:
        first_gen = input("Are you a first generation college student? (y/n): ").strip().lower()

        if first_gen == 'y':
            current_score += 1
            break
        elif first_gen == 'n':
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

    return current_score

# Question 11
def how_many_credits_next_semester():
    """
    This function asks the user how many credits they are going to take next semester.
    If less than 12, remove 1 point from current score.
    If equal to 12, return current score.
    If between 12-15 (inclusive), add 1 point to current score.
    If between 15-18 (inclusive), add 2 points to current score.
    If over 18, add 3 points to current score.
    """
    print("QUESTION 11")
    global current_score  # Access the global var for the current score

    # Read user input
    credit = int(input("How many credits are you taking next semester: "))

    if credit < 12:
        current_score -= 1
    elif credit == 12:
        pass  # No change to score
    elif 12 < credit <= 15:
        current_score += 1
    elif 16 <= credit <= 18:
        current_score += 2
    elif credit > 18:
        current_score += 3

    return current_score

# Question 12
def are_you_international_student():
    """
    This function asks the user if they are an international student.
    If yes, add 1 point to current score.
    If no, do not add points to current score.
    """
    print("QUESTION 12")
    global current_score  # Access the global var for the current score

    while True:
        international_student = input("Are you an international student? (y/n): ").strip().lower()

        if international_student == 'y':
            current_score += 1
            break
        elif international_student == 'n':
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

    return current_score

# Call the functions
def call_functions():
    how_many_credits_total()
    how_many_semester()
    do_you_have_disability()
    are_you_student_athlete()
    are_you_resident_assistant()
    academic_probation()
    disciplinary_probation()
    are_you_transfer_student()
    are_you_employed_over_twenty_hours()
    are_you_first_gen_college_student()
    how_many_credits_next_semester()
    are_you_international_student()

call_functions()

# At the end of the program, tell the user their score
print()
print("--------YOUR HOUSING SCORE--------")
print("Your housing points score is", current_score)
print("----------------------------------")

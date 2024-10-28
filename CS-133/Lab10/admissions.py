#################################
## PROVIDED CODE, DON'T MODIFY ##
#################################

def check_row(row):
    """Checks to ensure that a list is of length 8 and that each element is type float.

    Parameters:
    row (list): The list to be checked.

    Returns:
    boolean: True if the length is 8 & all elements are floats. False otherwise.
    """
    if len(row) != 8:
        print("Length incorrect! (should be 8): " + str(row))
        return False
    ind = 0
    while ind < len(row):
        if type(row[ind]) != float:
            print("Type of element incorrect: " + str(row[ind]) + " which is " + str(type(row[ind])))
            return False
        ind += 1
    return True

###########################
## WRITE YOUR CODE BELOW ##
###########################

def convert_row_type(row):
    """
    Converts each element in the list to a float if possible.
    If an element is empty or cannot be converted, substitutes it with a default value (e.g., 0.0).

    Parameters:
    row (list): The list of elements (as strings) representing one student's data.

    Returns:
    list: A list with all elements converted to floats, with defaults for any problematic values.
    """
    converted_row = []
    for element in row:
        try:
            # Try to convert the element to a float
            converted_row.append(float(element))
        except ValueError:
            # If conversion fails, append a default value
            converted_row.append(0.0)
    return converted_row


def calculate_score(student_info):
    """
    Calculates the prospective student score based on weighted criteria.

    Parameters:
    student_info (list): A list containing GPA, SAT, Interest, and High School Quality scores.

    Returns:
    float: The calculated score for the student, rounded to 2 decimal places.
    """
    # Unpack student information
    sat_score, gpa, interest, high_school_quality = student_info

    # Normalize GPA and SAT
    normalized_gpa = gpa * 2
    normalized_sat = sat_score / 160

    # Calculate weighted score
    score = (
            0.4 * normalized_gpa +  # 40% GPA
            0.3 * normalized_sat +  # 30% SAT
            0.2 * high_school_quality +  # 20% curriculum strength
            0.1 * interest  # 10% demonstrated interest
    )

    # Round to 2 decimal places and return
    return round(score, 2)


def is_outlier(student_info):
    """
    Checks if a student is an outlier based on specific conditions:
    - Demonstrated interest score of 0.
    - Normalized GPA more than 2 points higher than the normalized SAT score.

    Parameters:
    student_info (list): A list containing GPA, SAT, Interest, and High School Quality scores.

    Returns:
    bool: True if the student is an outlier, False otherwise.
    """
    # Unpack student information
    sat_score, gpa, interest, high_school_quality = student_info

    # Normalize GPA and SAT
    normalized_gpa = gpa * 2
    normalized_sat = sat_score / 160

    # Check if the student meets the outlier conditions
    if interest == 0 or (normalized_gpa - normalized_sat > 2):
        return True
    return False


def is_grade_outlier(grades):
    """
    Checks if there is a single grade that is more than 20 points lower than all other grades.

    Parameters:
    grades (list): A list of grades (float or int).

    Returns:
    bool: True if an outlier grade exists, False otherwise.
    """
    # Sort grades from lowest to highest
    sorted_grades = sorted(grades)

    # Check if the difference between the two lowest grades is greater than 20
    if len(sorted_grades) > 1 and (sorted_grades[1] - sorted_grades[0] > 20):
        return True
    return False


def is_grade_improved(grades):
    """
    Checks if the average score of each semester is higher than each previous semester.

    Parameters:
    grades (list): A list of grades (float or int) for each semester.

    Returns:
    bool: True if grades are strictly increasing, False otherwise.
    """
    # Check if grades are in ascending order
    in_order = grades == sorted(grades)

    # Check if all grades are unique
    no_duplicates = len(grades) == len(set(grades))

    # Return True if both conditions are met
    return in_order and no_duplicates

########################################
## PROVIDED STARTER CODE, MODIFY THIS ##
########################################

def main():
    # File setup
    filename = "dataset.csv"
    input_file = open(filename, "r")
    output_file = open("all_student_scores.csv", "w")  # New .csv file for all the student names and scores
    chosen_file = open("chosen.txt", "w")  # New file for students with a score of 6 or higher
    outliers_file = open("outliers.txt", "w")  # New file for students identified as outliers
    improved_chosen_file = open("improved_chosen.txt", "w")  # New file for improved list
    extra_improved_chosen_file = open("extra_chosen.txt", "w")  # New file for extra improved list
    print("Processing " + filename + "...")

    # Grab the line with the headers
    headers = input_file.readline()

    # Loop through file content line-by-line
    for line in input_file:
        # Split each line by commas to get a list of elements
        row = line.strip().split(",")

        # Save the student's name in a variable and remove it from the list
        student_name = row[0]
        row = row[1:]

        # Convert each element in row to a float, handling any invalid entries
        row_floats = convert_row_type(row)

        # Check if the row is valid
        if not check_row(row_floats):
            print(f"Error in data for student: {student_name}")
            continue  # Skip this student if the row is invalid

        # Separate the data into two lists
        student_info = row_floats[:4]  # SAT, GPA, Interest, High School Quality
        semester_grades = row_floats[4:]  # Semester 1, Semester 2, Semester 3, Semester 4

        # Calculate the student's score
        score = calculate_score(student_info)

        # Write the student's name and score to the output file
        line = f"{student_name},{score}\n"
        output_file.write(line)

        # If the score is 6 or higher, write the student name to chosen.txt
        if score >= 6:
            chosen_file.write(f"{student_name}\n")

        # Call is_outlier and, if True, write to outliers.txt
        if is_outlier(student_info):
            outliers_file.write(f"{student_name}\n")

        # If meets the conditions, write the student name to improved_chosen_file.txt
        if score >= 6 or (is_outlier(student_info) and score >= 5):
            improved_chosen_file.write(f"{student_name}\n")

        # If meets the conditions, write the student name to extra_chosen_file.txt
        if score >= 6 or (score >= 5 and (is_outlier(student_info) or is_grade_outlier(semester_grades) or is_grade_improved(semester_grades))):
            extra_improved_chosen_file.write(f"{student_name}\n")

    # Close all files
    input_file.close()
    output_file.close()
    chosen_file.close()
    outliers_file.close()
    improved_chosen_file.close()
    extra_improved_chosen_file.close()
    print("Done!")

# Call the main function
main()
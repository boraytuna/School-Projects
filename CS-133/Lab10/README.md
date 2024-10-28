[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/A-k_1xT3)
# Admissions Lab

## Overview

### Code
Develop code (admissions.py) to process student data to decide which students should be admitted.

### Document
Remember to comment your code.

### Submit
* Stage your code (admissions.py) as well as all of your output files, which should include:
  * all_student_scores.csv
  * chosen.txt
  * outliers.txt
  * improved_chosen.txt
  * extra_improved_chosen.txt
* Commit to the GitHub repository for grading.
* *Note!* Your program will be tested using a file with the same format but different data! Make sure that you haven't "hard coded" anything specific to your data.

### Credits
This lab was originally developed by Natalie Garrett and Casey Fiesler and is available in its original form here: [https://www.internetruleslab.com/ethicsbased-computer-science-assignments](https://www.internetruleslab.com/ethicsbased-computer-science-assignments).

## Detailed Instructions
In this lab you will...
* Understand how to iterate through a list
* Practice implementing functions that return values
* Explore algorithmic decision-making and representations of people in data
* Understanding outliers, missing information in data, and human judgements in algorithmic decisions

### Introduction
As you know, the college admissions process involves a lot of types of data from prospective students to make decisions. With the number of applicants increasing, colleges may begin relying on algorithms to select which applications should receive more intensive human review. An algorithm could use quantitative data–such as GPA and SAT score–to provide initial recommendations. In fact, there is more data available than ever. [Many colleges](https://www.wsj.com/articles/the-data-colleges-collect-on-applicants-11548507602) even track data about prospective student engagement (e.g., whether they open emails, visit the college website, engage on social media, etc.) This creates a “demonstrated interest” value.

Based on a [recent survey](https://www.insidehighered.com/admissions/article/2018/11/12/new-data-admissions-including-application-trends-early-decision-and) of college admissions officers, we know some of the weights that humans tend to give to these different types of data.  Your task will be to create a program that iterates through a list of data points and provides a recommendation for which prospective students are likely to be the best candidates for admission.

### Data
Prospective student data is organized in the **dataset.csv** file such that the data for each student is on one line, with the values separated by commas. Examples of student data might be:

```
Student,SAT,GPA,Interest,High School Quality,Sem1,Sem2,Sem3,Sem4
Abbess Horror ,1300,3.61,10,7,95,86,91,94
Adele Hawthorne ,1400,3.67,0,9,97,83,85,86
Adelicia von Krupp ,900,4,5,2,88,92,83,72
```

The data includes (in order):
* Student: a unique identifier for each student (their string name)
* SAT score: value between 0 and 1600
* GPA: value between 0 and 5
* Interest: value between 0 and 10 (from very low interest to very high interest)
* High School Quality: value between 0 and 10 (from very low-quality to very high-quality high school)
* Semester 1: average grade for semester 1
* Semester 2: average grade for semester 2
* Semester 3: average grade for semester 3
* Semester 4: average grade for semester 4

### Getting Set Up
First, we need to make sure that we can appropriately read in the data line by line, parsing each line into a list and converting each element to the appropriate type.

#### Task 1.1
Read in your data set in main(), looping through its contents line by line. This code is already provided for you.
* Make use of the str.split(delimiter) function to break individual lines into a list of elements.
* Make sure that you've done this by printing the value of your list after using the split function. You'll delete this print statement later but make sure to double check this before moving on!
* Once you have each line in a list, save the student's name in a variable, then delete this element from your list.

#### Task 1.2
Once you have a list of strings for each line, you will write a function **convert_row_type** that takes one list of elements (representing the data for one student) as a parameter and converts it so that all numbers are converted to floats. Make sure not to lose any information when you do this conversion!

Example:
```
Input: ["1300","3.61","10","7","95","86","91","94"]
Return value: [1300.0,3.61,10.0,7.0,95.0,86.0,91.0,94.0]
```

#### Task 1.3
In main, once you've called convert_row_type on the list representing one row, call the provided check_row. If this function returns False, print out an error message. Ensure that none of the rows in your data return False when passed to this function.

#### Task 1.4
Separate your data. Use list slicing to separate your list (which should contain 8 numbers at this point) into two lists:
* One that contains: the student's SAT, GPA, Interest, and High School Quality scores, and
* Another one that contains their 4 semester grades.

You'll use the first list of 4 numbers for Problems 2 and 3, and Problem 4 with the second list of grades.

### Problem 2: Prospective Student Score

#### Task 2.1
Write a function **calculate_score** that takes a list as a parameter and calculates an overall score for each student based on the following weights:  
* 40% GPA,
* 30% SAT,
* 20% strength of curriculum, and
* 10% demonstrated interest.

The list parameter will contain all of the relevant information about the student. The return value is the student’s calculated score.

Two important notes on output:
* To make this work, you will also need to normalize both GPA and SAT so that they are also on a 0 to 10 scale. To do this, multiply the GPA by 2, and divide the SAT score by 160.
* Round each output score to 2 decimal points.

Example:
```
Input: [1300.0,3.61,10.0,7.0]
Output: 7.73
```
The above example represents a student with a 1300 SAT score, a 3.61 GPA, 10 out of 10 for interest and 7 out of 10 for high school quality. The output is calculated as follows:

```
((3.61 * 2) * 0.4) + ((1300 / 160) * 0.3) + (10 * 0.1) + (7 * 0.2)
```

#### Task 2.2
In your main() function, modify your loop that reads in and converts your data to call the calculate_score function for each line (row) of data (after you've converted it).

Then, write the student's id and their calculated score to a new file called **all_student_scores.csv** (using the example code below) such that each row contains a student’s name and their score, separated by a comma.

```
output_file = open('all_student_scores.csv', 'w')
line = "Abbess Horror ,7.73,\n"
output_file.write(line)
```

Example lines written to file:
```
Abbess Horror ,7.73
Adele Hawthorne ,7.36
Adelicia von Krupp ,5.79
```
#### Task 2.3
Write the student names for all students who have a score of 6 or higher to a file called **chosen.txt**. You should do this in your main() function, where you have access to the returned calculated score for each student and their name.

Example lines written to file:
```
Abbess Horror
Adele Hawthorne
```

### Problem 3: Looking for Outliers

Consider ways that this algorithm might systematically miss certain kinds of edge cases. For example, what if a student has a 0 for demonstrated interest because they don’t use social media or have access to a home computer? What if a student has a very high GPA but their SAT score is low enough to bring their score down; could this mean that they had a single bad test taking day?

#### Task 3.1
Write a function **is_outlier** that can check for certain kinds of outliers. It should check for:
1. demonstrated interest scores of 0 and,
2. a normalized GPA that is more than 2 points higher than the normalized SAT score.

If either of these conditions is true, it should return True (because this student is an outlier); otherwise, the function returns False.

#### Task 3.2
Call is_outlier for each student from your main() function and write the students' names to a file called **outliers.txt**, one name per line if they are an outlier.

#### Task 3.3
Combine the work that you've done now to create an improved list of students to admit to your school. Write students names, one per line to the file **improved_chosen.txt** if they either have a score of 6 or greater or if they are an outlier and their score is 5 or greater. Make sure to take advantage of the work that you’ve already done by calling your functions from previous problems to help you out!

### Problem 4: GPA Checker

A single GPA score is not a full picture of a student’s academic performance, as it may have improved over time or included outlier courses or semesters. A more context-sensitive algorithm could consider a student’s entire transcript and checks for, for example, a single class score that is more than two letter grades (20 points) lower than all other scores. For this task, you will use the second half of the data for each student in the provided file.

#### Task 4.1
Write a function **is_grade_outlier** that takes in a list of grades (of *any* length) and returns True if one single number is more than 20 points lower than all other numbers; otherwise, False.

Example:
```
Input: [99, 94, 87, 89, 56, 78, 89]
Output: True
```

Hint: Sort the list from lowest to highest, and check for the difference between the two lowest grades. In the example above, 78 - 56 = 22 and 22 is > 20. Therefore, the function returns True.

Next, consider the data that we have: a list of grades for each student, one grade per semester for four semesters. Make sure that your is_grade_outlier function works by calling it for every row in the second dataset. Print out an informative message about which students have a single grade outlier. You'll delete this later but it's a great way of testing your function!

Finally, consider the importance of an algorithm being able to flag students who might have a lower overall GPA but have shown improvement over time.

#### Task 4.2
Create a function **is_grade_improved** that returns True if the average score of each semester is higher than each previous semester and False otherwise. Hint: investigate how the == operator works between two lists and think about using the sorted() function.

#### Task 4.3
Using the grade information that you've just learned, create your own conditions based on the information from the previous problems, is_grade_outlier, and is_grade_improved to chose all students if:
* they either have a score of 6 or greater or,
* if they have a score of 5 or more and at least one of the following is true:
  * is_outlier returns True,
  * is_grade_outlier returns True, or
  * is_grade_improved returns True.

Write the students who fit this description to **extra_improved_chosen.txt**, one name per line.

## Specifications to Pass
* Your code (admissions.py) outputs all of the correct students to the correct output files using a test comma seperated value file that is formatted the same as dataset.csv, but contains different student scores. The correct output should appear in the following files:
  * all_student_scores.csv
  * chosen.txt
  * outliers.txt
  * improved_chosen.txt
  * extra_improved_chosen.txt
* Your code  (admissions.py) implements all of the above specified functions, with each one operating as instructed. These include:
  * check_row (provided)
  * main (partially provided)
  * convert_row_type
  * calculate_score
  * is_outlier
  * is_grade_outlier
  * is_grade_improved
* Your code (admissions.py) is appropriately documented.

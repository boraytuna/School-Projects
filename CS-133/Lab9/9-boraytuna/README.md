[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/o_oNPePI)
# Visitor Form Lab

## Overview

### Code
Develop code (form.py) to write a standard form that a university can give visitors to collect their information.

### Document
Remember to comment your code.

### Report
Your lab report (labreport.md) should include tests cases, and an ethical reflection.

### Submit
* Stage your code (form.py) and labreport.md.
* Commit to the GitHub repository for grading.

### Credits
This lab was originally developed by [Evan M. Peck](http://www.eg.bucknell.edu/~emp017/) and is available in its original form here: [https://ethicalcs.github.io/#gatekeepers](https://ethicalcs.github.io/#gatekeepers).

## Detailed Instructions
In this lab, you’ll ...
* use functions within the flow of a program,
* reinforce our understanding of data types,
* reinforce our understanding of conditionals, and
* practice usability and security via input validation.

### The Scenario
You are working for the prestigious Harwall University to meet the joint needs of Admissions, Alumni Relations, and Communications. People are constantly visiting campus - to see someone they know, to check out the school as a prospective student, to give a talk, to interview, to come back to the school (alumni!), or for a variety of other reasons.

It would be valuable to know who is on campus throughout the year, so you are asked to write a standard form that Harwall can give visitors to collect their information. Harwall intends to use the information from this form later to communicate with potential donors or reach out to prospective students. This seems like a small task, but in the competitive world of college admissions and development, your work has the potential to significantly impact the future of Harwall University.

The more highly-structured data Harwall collects, the more they feel they can effectively build relationships and communicate with their visitors. It helps with automated mailing lists to follow up, it helps with detecting patterns in prospective students and visitors, and it helps the university reflect on the demographics of people that they might be missing.

Since Harwall wants to make sure that this data is useful, they have also asked you to validate whatever information is entered into the form. *That is your job. Choose the data and validate it.*

### Starter Code
Rather than a typical online form, we’ll be designing our form via the console in Python (just like previous labs). You’ve been provided with a template (form.py) which the university wishes you to follow. It also includes an example.

At a high level, form() acts as the main function that controls the logic of the program. It’s where we assign each of the fields that we would like to collect, and also where we report the collected information afterwards.

We’ll use if/elif/else statements to decide whether users input the correct information. For each field that we want to collect, you create a corresponding validation ***function***. We already have one 100% completed in the example: test_street_num()

Take some time to understand the starter code now.

### Write test_age Function
You might have noticed that the function test_age is not completed yet. Before you start writing code, always write test-cases in English. For example, here are the English test-cases for the function test_street_num:

1. (Bad) The user enters nothing, or just spaces.
    * Test: Should catch nothing, a space, and multiple spaces
    * Expected output: returns False
2. (Bad) The user enters something other than a positive number.
    * Test: Should catch ten, a, !, -10
    * Expected output: returns False
3. (Good) The user enters a positive number.
    * Test: 10, 5, 223
    * Expected output: returns the number

When you think you understand the above test cases for the function test_street_num(), write a similar set of test cases for test_age in your lab report. Record numbers that you are using to test that your code is working. Provide suitable checks that someone has entered a reasonable age. (For example, no one should be 800 years old. Let’s assume that our visitors are not older than 122 years.)

After your test cases are written, complete the code for the partially finished test_age function. Before moving on, use your test cases to ensure that your code is working.

### Designing Your Form
Now it is time to decide for yourself which other information you will capture. Here are a couple of examples of people who may be visiting campus:

> Beverly (52, F) and Robert (55, M) Deason are bringing their daughter Mary (17, F) for a college visit. Mary is a junior in high school, and is thinking about Harwall because of the Engineering College. Coming from Cambridge, MA, the family is traveling across a number of colleges in Pennsylvania. Mary says that you can email her at mlp231@mac.com or text her at (617) 431-5817.

> Terrell Hughes (M) is on campus to interview for the tenure-track Computer Science faculty position. He is currently a visiting scholar at Cornell University in Ithaca, NY, having been there since he got his Ph.D. from NYU a year ago. You have his business card, which lists his contact information as thughes14211@cornell.edu and 607 151 4561. Terrel laughed when you asked for his age, and just said to put down 30.

> Rolf Feierabend (M) has lived in Mifflinburg, PA since 1961, when his parents immigrated to the US, bringing then-seventeen Rolf in tow. He has been retired for a couple of years now, and takes his husky lab Winston on walks through campus on occasion. Although he has an email account feierabend411@aol.com he doesn’t really check it anymore. He says to just call him at 570-511-5161

Decide which information is absolutely necessary to capture from each visitor.
Each piece of information will be its own field. Note that...
* The university would like you to capture as much information as possible. The more individual pieces of data they have, the more successfully they can communicate with their visitors.
* More fields are usually better than fewer. For example, a single address field might make it hard later on for a computer to decipher the different pieces. Breaking it into pieces (street number, state, country) is advantageous for all the ways the university might want to use it.

Complete the following tasks:
* Choose 3 fields of the *most important* information to capture. List the 3 fields in your lab report (replace ???) and include test cases for each field.
* Once finished with test cases, write the code to capture and validate the user's input for each of these 3 fields. Be creative and use some of the concepts discussed in class. This will require you to add code in the form() function, and to create a new test function.

During this process, you will probably have several moments in which you need to ask how can I do this in Python? Before asking your instructor, try playing with the code and see what happens. We also encourage you to see if you can find the answer using a search engine (like Google). The more you can empower yourself to use the web’s resources to overcome your programming problems, the more effective you’ll be in this course as our projects get larger.

### Part Two
There is an additional portion of this lab, but you can only access it once you have completed the lab up until this point.  If you are here, ask the instructor for the final part. Read the text before completing the following questions in the Ethical Reflection section of your lab report.
* Without changing your code, try to enter the information from the visitors described in the part two text using your program. What happens? Does your program work? Where does it fail?
* After reading the articles referenced in the the part two text, reflect on the following question: How could you change your program to address some misconceptions we might have about “normal” answers to different fields of information? As you make your input validation more permissive, what is the tradeoff for the university’s data collection?
* What would happen if a form built with bad assumptions was used in college applications? How might the design of the form change the composition of a recruiting class. Who would be most likely to have trouble filling out the form?

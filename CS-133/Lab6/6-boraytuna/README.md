[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/-Mf--0iT)
# Targeted Ads Lab

## Overview

### Code
Develop code (ads.py) to deliver targeted ads for a social media platform.

### Document
Remember to comment your code.

### Report
Your lab report (labreport.md) should include tests cases for problem 4, and an ethical reflection.

### Submit
* Stage your code (ads.py) and labreport.md.
* Commit to the GitHub repository for grading.
* Make sure all tests pass.
  * You may resubmit if your tests fail, but please perform extensive testing locally first
  * Note: Our course has a finite number of provisioned tests

### Credits
This lab was originally developed by Natalie Garrett and Casey Fiesler and is available in its original form here: [https://www.internetruleslab.com/ethicsbased-computer-science-assignments](https://www.internetruleslab.com/ethicsbased-computer-science-assignments).

## Detailed Instructions

For this lab, you will be creating functions that will:
1. ask questions to collect data, and
2. create functions that will use that data to output personalized ads using conditionals.

Each problem will present a short scenario and task describing what type of personalized ad should be served. There will be a few guidelines for the first few questions and ads you’ll be implementing, and then you will have the freedom to ask your own questions and develop your own ads.

Your job is to write a program that decides on an ad to serve to a person on a social media platform. The personalized ad program will prompt the user for information and then return text that describes ads based on their inputs. Feel free to use as much (or as little) creativity as you want for the descriptions of ads for your program!

Final output should look something like this (it will vary based on the problem):
```
How personalized should the ad be? (1 - 4): 1
Do you own a dog? yES
Dog Food Ad: [Your text here]
```

### Initial Reflection
Before you begin, think about the ads you see online.
* Are those ads accurate?
* How do you think advertisers profile you?
* What information do you think advertisers use?
* How do you feel about these kinds of inferences being used to influence your behavior online and offline?
* Is this just par for the course of how we are influenced every day by things like advertising, or does it feel different?
* Are there ethical or unethical ways to use this kind of technology?

### Objectives

In this lab, you’ll...
* Understand how to implement a simple decision using an if statement.
* Understand how to implement a two-way decision using an if/else statement.
* Understand how to implement a multi-way decision using an if/elif/else statement.
* Understand the concept of boolean expressions and the boolean data type.
* Be able to read, write, and implement algorithms that employ decision structures, including those that employ sequences of decisions and nested decision structures.

#### Constraints
You should not use any global variables in this code. ***All your variables must be local within functions***.

### Problem 1

Next, work on asking questions and creating functions to deliver ads based on the following scenario:

***Scenario:*** For advertisers using the lowest tier of personalization on this social media platform, there is limited data about users available — we only know whether a user self-reported that they own dog.

***Task 1.1:*** Find out whether a user has a dog! Using the built-in input function, ask the user if they have a dog. Our user will more than likely type a “yes” or “no”, which isn’t very easy for our program to use (strings are not the most appropriate data type for representing values that we want to have two options)! So let’s create a function to turn that answer into something that is easy to parse: a Boolean.

Write the following function:

* _owns_dog_: this function should take no parameters. It should return the user’s answer as a boolean. This function should be case insensitive. If the user answers "yes", "YES", "yES", "yes", or any other variations of "yes", your function should return True. If they answer anything that is not "yes" (case insensitive), your function should return False. Make use of [string functions](https://docs.python.org/3/library/stdtypes.html#string-methods), rather than listing all possibilities, to accomplish this!

***Task 1.2:*** Given a boolean returned by owns_dog, write a function dog_ad that:
* If the value of this boolean is True, print text advertising dog food. Your text must start with “Dog Food Ad:“
* Otherwise, print text advertising anything else. Your text must start with "Ad:".

For example, given that the user owns a dog, your function might something like:
```
Dog Food Ad: Meat’s the need of dogs like yours! The ALL-MEAT dinner for dogs, WOOF.
```

Otherwise, your function might something like:
```
Ad: Dirty mouth? Clean it up with new Orbit Raspberry Mint. For a good clean feeling, no matter what!
```

Write the following function:

* _dog_ad_: this function should take one argument as a parameter (the answer to a yes-or-no question: Do you own a dog?) If the user has a dog, they will be served an ad for dog food. If they do not have a dog, they will be served an ad for anything else you choose.

***Task 1.3:*** Go implement the part of problem 5 that corresponds to delivering ad 1.

### Problem 2

Next, work on asking questions and creating functions to deliver ads based on the following scenario:

***Scenario:*** By combining data from a marketing platform with the results from personality tests that users have completed, we know that people with at least 500 Facebook friends are likely to be extroverts, and people with less than 500 friends are likely to be introverts. Based on analysis of user-uploaded photos using computer-vision algorithms, we also know that people who are extroverts are more likely to have many photos of dogs, and introverts are more likely to have many photos of cats. Market research has shown that dog people are highly likely to be positively influenced by advertisements for any product that includes dogs, and similar for cat people and cats.

***Task 2.1:*** Find out how many friends a user has, and write a function that implements the following logic:
* If the user has at least (more than or equal to) 500 friends, print ad text that includes a dog. Your text must start with "Ad with Dog:".
* If the user has less than 500 friends, print ad text that includes a cat. Your text must start with "Ad with Cat:".

Write the following functions:

* _int_question_: this function should take one parameter, the string question to pose to the user. It should return the user's answer as an int. If the user provides an answer that is not an integer greater than or equal to 0 (hint: see the str.isdecimal() function), this function should print an informative message, then return the number 0. (The user should not be able to make this function throw an error). Make sure to call this function whenever you ask the user a question with an integer response. (Even in problems 3 and 4!)
* _friends_ad_: this function should take one parameter, the integer number of friends that the user has. If this number is greater than or equal to 500, they will be served an ad for any product that includes a dog as part of the ad; if less than 500, a cat should be part of the ad. The text must contain the specific strings indicated above.

***Task 2.2:*** Go implement the part of problem 5 that corresponds to delivering ad 2.

### Problem 3

Next, work on asking questions and creating functions to deliver ads based on the following scenario:

***Scenario:*** Based on ad clicks and third-party data shared through purchases on a “marketplace” platform, we have data about likely income averages for every zipcode in the country. We also know based on self-reported age how incomes vary based on life stage (e.g., college students have less disposable income no matter where they live). Advertisers strategically advertise to people who are more likely to be able to afford their product.

***Task 3.1:*** Given a user’s zipcode and age as integers, write a function that implements the following logic:
* If the zipcode is in Allegany or St. Bonaventure's zip code (14706 or 14778) and the user is at least 25, print ad text for an expensive product. Your text must start with "Expensive Product Ad:".
* If the zipcode is in Allegany or St. Bonaventure and the user is younger than 25, print ad text for an inexpensive product. Your text must start with "Cheap Product Ad:".
* Otherwise, print ad text encouraging the user to visit SBU. Your text must start with "Tourist Ad:".

Write the following function:

* _zip_age_ad_: this function should take two arguments, the user’s zipcode and their age. If their zipcode is either 14706 or 14778 they should be shown an advertisement for an expensive product - unless their age is under 25, in which case they should be shown an ad for a cheap product. If they do not live in 14706 or 14778, they should be shown an ad encouraging them to come visit SBU. The text must contain the specific strings indicated above.

***Task 3.2:*** Go implement the part of problem 5 that corresponds to delivering ad 3.

### Problem 4

Next, work on asking questions and creating functions to deliver ads based on the following scenario:

***Scenario:*** Imagine that you have access to even more of a user’s personal information based on their profile. In order to help advertisers get the most money out of their advertising packages, you tailor the ads a user will see based on personal details each user provides.

***Task 4.1:*** Write a function that uses personal details from a social media profile to display at least 3 different custom ads depending on what the user has input. You are free to use all, some, or none of the information given to print text advertising. The only guideline is that your advertisements must start with "Custom Ad [number] :"". Descriptions of the variables are below. Your function must take at least 4 of the following values as parameters.

* name – a string containing a user’s name (e.g. Avatar Aang)
* gender – a string containing a user’s gender (e.g. man)
* age – an integer containing a user’s age (e.g. 98)
* hometown – a string containing a user’s hometown (e.g. Southern Air Temple)
* relationship – a string containing a user’s relationship status (e.g. Crushing on Someone)
* birthday – a string containing a user’s birthday (e.g. August 21)
* number_of_friends – an integer containing the number of friends a user has on social media (e.g. 243)
* political_affiliation – a string containing a user’s political affiliation (e.g. Independent)

When you prompt the user for their choices, make sure that it is clear what format they should answer using (an integer, yes/no, a string of their choice, etc).

Using the examples above (i.e. Avatar Aang, man, 98, etc.), your function might print:
```
Custom Ad [1] : Looking for cabbages? Cabbage Corp - Cabbages so good, they’re smashing.
```

***Task 4.2:*** Write *at least* 3 test cases for this problem. Document these in your lab report and test your program.

***Task 4.3:*** Go implement the part of problem 5 that corresponds to delivering ad 4.

### Problem 5

As you have been working through the above problems, you should have been adding function calls to each one under problem 5. See sample output below:

```
How personalized should the ad be? (1 - 4): 1
Do you own a dog? YeS
Dog Food Ad: [Your text here]
```
```
How personalized should the ad be? (1 - 4): 1
Do you own a dog? no
Ad: [Your text here]
```
```
How personalized should the ad be? (1 - 4): 2
How many friends do you have? 500000
Ad with Dog: [Your text here]
```
```
How personalized should the ad be? (1 - 4): 2
How many friends do you have? so many
Not a number! Converting answer to 0.
Ad with Cat: [Your text here]
```
```
How personalized should the ad be? (1 - 4): 3
What zip code do you live in? 14706
How old are you? 52
Expensive Product Ad: [Your text here]
```
```
How personalized should the ad be? (1 - 4): 3
What zip code do you live in? 14706
How old are you? 18
Cheap Product Ad: [Your text here]
```
```
How personalized should the ad be? (1 - 4): 3
What zip code do you live in? 90210
How old are you? 21
Tourist Ad: [Your text here]
```

### Testing Notes
* The automated tests will pass the first number in a way that may cause Python to interpret it as an integer. Therefore, your code should assume and enforce the use of integers instead of strings.
* The automated test input will include trailing new line characters. Therefore, your code should sanitize input to remove any trailing characters using [rstrip()](https://docs.python.org/3/library/stdtypes.html#str.rstrip).

### Reflect
Your code works...but is it fair? You should never deploy real code without checking your assumptions. Test cases only test your technical assumptions, but not your social assumptions. Reflect on these questions ***in conjunction*** with those above in the Initial Reflection section:

* How might data be used for advertising purposes?
* How can inferences about someone be drawn from data? These inferences allow information to be known about someone beyond what they explicitly state.
* How can what is known about someone influence not only what is advertised to them, but how it is advertised?

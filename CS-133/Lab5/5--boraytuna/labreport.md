# Housing Priority Lab Report

## User Needs Assessment
***Provide your bullet-point list of factors and their numeric priority here.***
* How many credits do you have? 0-29 credits is 1 point. 30-59 is 2 points. 60-89 is 3 points. 90-120 is 4 points. 120+ is 5 points.
* How many semesters have you lived in on-campus housing? 1 semester is 0.5 point.
* Do you have any disability that limits your movement? If they say yes add 1 point to current_score and prompt the new question "Do you need to live in first floor?" Yes is 5 points. No is 0 point.
* Are you a student athlete? Yes is 2 points. No is 0 point.
* Are you a resident assistant (RA)? Yes is 1 point. No is 0 point.
* Have you been on academic probation during the last academic year? Yes is -1 points. No is 0 point.
* Have you been on disciplinary probation during the last academic year? Yes is -3 points. No is 0 point.
* Are you a transfer student? Yes is 1 point. No is 0 point.
* Are you currently employed more than 20 hours per week? Yes is 1 point. No is 0 point.
* Are you a first-generation college student? Yes is 1 point. No is 0 point.
* How many credits are you taking next semester? If is less than 12 remove 1 point. If equal to 12 is 0 point. If between 12-15 (15 included) is 1 point. If between 15-18 (18 included) is 2 points. If over 18 is 3 points.
* Are you an international student? Yes is 1 point. No is 0 point.


## Test Cases
***Provide a bullet-point list of your tests cases here. Include both input & expected output.***
* Boray with 77 credits, 4 semesters, no disability, student athlete, not a resident assistant, no academic probation, no disciplinary probation, not a transfer, not working over 20 hours, not a first generation, 17 credits and is an international student should output 10.
* Mark with 44 credits, 2 semesters, yes disability, no need to live on first floor, not a student athlete, a resident assistant, no academic probation, no disciplinary probation, not a transfer, works over 20 hours, not a first generation, 15 credits and is not an international student should output 7.
* Miko with 92 credits, 7 semesters, no disability, not a student athlete, not a resident assistant, no academic probation, disciplinary probation, a transfer, not working over 20 hours, not a first generation, 12 credits and is an international athlete should output 6.5.
* Sarah with 112 credits, 5 semesters, yes disability, needs to live on first floor, not a student athlete, not a resident assistant, no academic probation, no disciplinary probation, not a transfer, working over 20 hours, first generation, 14 credits, not an international student should output 15.5.
* John with 22 credits, 1 semester, no disability, not a students athlete, not a resident assistant, academic probation, no disciplinary probation, transfer student, not working over 20 hours, not a first generation, 19 credits, international student should output 5.5.

## Ethical Reflection
***Reflect on the ways in which different scoring algorithms can advantage or harm different groups of people.***
* The scoring algorithm tends to benefit students who are involved in more activities or face certain challenges, like student athletes, those with disabilities, resident assistants, or international students. These groups gain extra points, which gives them an advantage in housing priority. However, students who do not belong to these categories, especially those with fewer credits or who don’t have special circumstances like disabilities or high credit loads, might be overlooked. This could result in less priority for students who still have important housing needs but don't fit the specific criteria used in the algorithm.

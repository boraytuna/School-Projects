[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/U1lHWjNT)
# Housing Priority Lab

## Overview

### Code
Develop a scoring algorithm (algorithm.py) to determine which classmates are prioritized for housing on campus.

### Document
Remember to comment your code.

### Report
Your lab report (labreport.md) should include needs, tests cases, and an ethical reflection.

### Submit
* Stage your code (algorithm.py) and labreport.md.
* Commit to the GitHub repository for grading.
* There are no automated tests (you must use your own test cases).

### Optional Reading
* [New Algorithms to Score Candidates for Lifesaving Organ Donations](http://algorithmtips.org/2021/04/29/new-algorithms-to-score-candidates-for-lifesaving-organ-donations/)
* [We Created Poverty - Algorithms Won’t Make That Go Away.](https://www.theguardian.com/commentisfree/2018/may/13/we-created-poverty-algorithms-wont-make-that-go-away)
* [What Happens When an Algorithm Cuts Your Health Care](https://www.theverge.com/2018/3/21/17144260/healthcare-medicaid-algorithm-arkansas-cerebral-palsy)

### Credits
This lab was originally developed by [Evan M. Peck](http://www.eg.bucknell.edu/~emp017/) and is available in its original form here: [https://ethicalcs.github.io/#decision-makers](https://ethicalcs.github.io/#decision-makers).

## Detailed Instructions

Read this README in its entirety ***before*** starting anything. Like all lab assignments, attention to detail in this lab is essential. Most of the questions you'll have while working on this lab area already answered here.

When we say the word ‘algorithm’, we tend to ascribe agency to the computer. It is *deciding* things for us. But the reality is that there is no magic. There are software developers like you and me who design and create sets of rules that the computer carries out for us.

These algorithms are all around us, and they are *constantly* making decisions.

The decisions we make in code impact the lives of real people. For example, the [Silicon Valley Triage Tool](https://economicrt.org/publication/silicon-valley-triage-tool/) is an *algorithm* that identifies people experiencing homeless for whom giving them housing would cost the public less than keeping them homeless. So even as we learn the simple structures of code, we need to think about **how we can make *good* decisions?**

We are going to explore this idea in a more familiar context to you - **university housing lotteries**. Universities like St. Bonaventure select methods that determine the order in which students can choose their housing. You might not think of it as one, but this method is an *algorithm*. St. Bonaventure's algorithm has not been popular, as described in [this news report](https://fb.watch/uJHhdBfMTA/). In this lab, you will have the opportunity to design your own algorithm.

In this lab, you’ll practice...
* translating English rule-sets into code,
* soliciting text input from people,
* applying conditionals (if/elif/else) to make decisions with a program,
* using an accumulation variable to keep track of information in a program, and
* integrating basic human-centered design processes into your programs.

### Algorithm Specifics

Your job is to build an algorithm that helps determine the order in which students will get to select their housing. To simplify things, we’re going to use a point system.
* Students are awarded a number of points based on a variety of factors.
* Students with the most amount of points get first choice at housing.

This real approach is used by many universities. For example, consider the following real point system used by another liberal arts college in the United States:
* Current Freshman: 1 point
* Current Sophomore: 2 points
* Current Junior: 3 points
* Current Senior: 4 points
* 23+ Years of Age: 1 point
* Full-Time, Off-Campus Program Credit (e.g. student teaching): 1 point
* Academic Probation: -1 point
* Possible Academic Suspension: -2 points
* On Disciplinary Probation at Any Point during the Academic Year: -3 points

So a junior (+3 points) who is 23 years old (+1 point) would have priority over a senior (+4 points) who is on academic probation (-1 point).

***Your goal is to create a program that assigns points to students in order to prioritize them in housing selection. But wait! Don’t start yet. First...***

### User Needs Assessment

Before you code, you must assess the needs of your users. While the list above was one college’s take, there are many more potential aspects to consider if you want to create a fair algorithm that takes into account the diverse needs of students.

You should not create a program that serves people without talking to people. Complete the following steps:

1. Watch [this news report](https://fb.watch/uJHhdBfMTA/).
2. Talk to other students in lab. Ask them about their needs.
3. Develop a list of unique factors that may be important in deciding who should choose housing first based on the steps above. Give each one a numeric priority. Include this list in your lab report.

### Algorithm Planning

Now it is time to translate student needs into a concrete algorithm. Be careful and limit yourself to the most important factors. You have a limited amount of time in lab!

Our algorithm will:
* Ask students questions (like "What class year are you?").
* Assign points based on their answers (like "4 points for senior").
* Accumulate their total points across all answers (like "You have 23 housing points").

#### Constraints
Since we are exercising our ability to write code in addition to solving problems, we are going to put a couple of constraints to make sure you get practice with the different ways in which conditionals can be used.

1. You must have at least 1 question that only appears if the previous question is answered a specific way.
- For example: if someone says they are a 4th year student, you may ask the question “Are you about to graduate?” If they say yes, they receive no points. *ONLY* a 4th year student would receive this question.

2. You must have at least 1 question that makes use of a simple equation to determine the number of points awarded.
- For example: Rather than ask people to enter their status as a 1st, 2nd, 3rd, 4th year, you ask them for the number of credits they have received so far at St. Bonaventure. Then they might receive credits/8 points.

***Your goal is to create a bullet-point list that describes the questions you will ask, the possible answers, and how you are mapping those factors to point values (positive or negative).***

#### Test Cases

Write *at least* 3-5 hypothetical test cases for your program. Document these in your lab report and return to these cases during testing of your program.

For example, tests cases might look like:

* A 25 year old senior who is on academic probation should output 4 points
* A 22 year old junior who is student teaching should output 4 points
* A 20 year old sophomore on disciplinary probation should output -1 points

### Write Code
Example starter code is provided in algorithm.py.

Your goal: Modify the program in algorithm.py to match the algorithm you designed. During your creation, keep a couple of things in mind:
* Start with just 2 fields that you would like to ask and test.
* Use comments to describe what was happening in the program.
* Choose variable names that clearly describe that data that they hold.
* Use spacing to group similar code.  

### Test
Test your code using your test cases developed above.

### Reflect
Your code works...but is it fair? You should never deploy real code without checking your assumptions. Your test cases tested your technical assumptions, but not your social assumptions.

1. Find classmates either inside or outside of the lab.
2. Run your code with them.
3. Get feedback on what worked and what didn’t?

In particular, you should reflect on...
* Which students are most likely to benefit from your algorithm?
* Which students are most likely to be forgotten by your algorithm?

## Specifications to Pass

* Lab report contains all of the following:
  * A numbered list of housing factors from your user needs assessment
  * At least 3 test cases that specify both the input and expected output
  * Ethical reflections on your code based on the testing of your code
* Code in algorithy.py does all of the following:
  * Produces the expected output from your test cases
  * Asks at least one question only if the answer to a previous question is answered in a specific way
  * Asks at least one question that makes use of a simple equation

# Week 8 Lab Report
***Boray Tuna Goren***

## Test Cases

### Test Cases for test_age

1. (Bad) The user enters nothing or just spaces
    * Test: Should catch nothing, a space, and multiple spaces
    * Expected output: returns False
2. (Bad) The user enters something other than a positive number.
    * Test: Should catch invalid inputs such as “ten”, “a”, “!”, “-10”.
    * Expected output: returns False
3. (Good) The user enters a positive number.
    * Test: Should accept valid inputs such as “10”, “5”, “223”.
    * Expected output: returns the number as an integer

### Test Cases for test_reason_for_visit

1. (Bad) The user enters nothing or just spaces
    * Test: Should catch nothing, a space, and multiple spaces
    * Expected output: returns False
2. (Bad) The user enters something other than string.
    * Test: Should catch invalid inputs such as "-10", "123".
    * Expected output: returns False
3. (Good) The user enters a valid string.
    * Test: Should accept valid strings such as “school search”, “dog walk”, “job application”.
    * Expected output: returns the string

### Test Cases for test_phone_number

1. (Bad) The user enters nothing or just spaces
    * Test: Should catch nothing, a space, and multiple spaces
    * Expected output: returns False
2. (Bad) The user enters something other than a positive number of exactly 10 digits
    * Test: Should catch inputs such as “-10”, “123456789”, "12345678901".
    * Expected output: returns False
3. (Good) The user enters a valid 10-digit number
    * Test: Should accept valid phone numbers such as “1234567890”, “7152361234”.
    * Expected output: returns the number as an integer.

### Test Cases for test_email

1. (Bad) The user enters nothing or just spaces
    * Test: Should catch nothing, a space, and multiple spaces
    * Expected output: returns False
2. (Bad) The user enters an invalid email without an “@” symbol or domain name
    * Test: Should catch invalid emails like “examplemail.com”, “user@com”.
    * Expected output: returns False
3. (Good) The user enters a valid email
    * Test: Should accept valid email formats such as “example@mail.com”, “user123@domain.org”.
    * Expected output: returns the email as a string

## Ethical Reflection

### Question 1
Without changing your code, try to enter the information from the visitors described in the part two text using your program. What happens? Does your program work? Where does it fail?

* Both visitors failed the street number of the address since they didn't include any information about the street they live in. When I tried to enter the information of first visitor(Chung Ying Tsang) the form failed. It failed because the student is from England and have a different calling code for the phone number. It requires more length to fit all the phone number information. When I tried to enter the information of the second visitor(Ash O'Connell-Chapman Jr.) the program failed. Because the second visitor didn't have a phone number or email. 

### Question 2
After reading the articles referenced in the part two text, reflect on the following question: How could you change your program to address some misconceptions we might have about “normal” answers to different fields of information? As you make your input validation more permissive, what is the tradeoff for the university’s data collection?

* After reading the articles on misconceptions about names, addresses, and phone numbers, I realized that my program makes several assumptions about what constitutes “normal” input. For example, in the test_reason_for_visit function, I restricted the input to only alphabetic characters and spaces. This means that if someone includes numbers or special characters in their reason (like “Visiting for CS101 workshop” or “Attending the 3D-printing seminar”), the program would reject their input.

* Similarly, the test_phone_number function assumes that all phone numbers are 10-digit positive integers, which is only true for U.S. phone numbers. This excludes international visitors who might have longer or differently formatted phone numbers, such as “+44 20 7946 0958” for a UK number.

* To address these misconceptions, I could modify my program to accept a wider range of characters in text fields like reason_for_visit, allowing numbers, punctuation, and special characters, remove strict length requirements for phone numbers and instead validate them using patterns that account for international formats, possibly by accepting strings and using regular expressions, allow optional fields or provide alternatives for users who might not have certain information, such as a phone number or email address.

* By making the input validation more permissive, we make the form more inclusive and accessible to a diverse range of users. However, the tradeoff is that the collected data may be less standardized, making it more challenging to process and analyze automatically. The university might receive data in various formats, which could require additional effort to clean and integrate into their systems.

### Question 3
What would happen if a form built with bad assumptions was used in college applications? How might the design of the form change the composition of a recruiting class. Who would be most likely to have trouble filling out the form?

* If a form built with bad assumptions is used in college applications, it could exclude or disadvantage certain groups of applicants. For example, international students might struggle with fields that don’t accept their phone numbers or addresses. Applicants with names that include special characters, hyphens, or suffixes like “Jr.” or “O’Connell” might not be able to enter their names correctly.

* This flawed design could lead to a less diverse recruiting class, as students who face difficulties with the form might abandon their applications or feel unwelcome. Those most likely to have trouble filling out the form include international applicants with non-U.S. phone numbers and addresses, individuals with names that don’t fit conventional Western formats.

* By not accommodating these variations, the university risks missing out on talented individuals who could contribute significantly to the campus community. It’s crucial to design forms that are inclusive and considerate of all potential users to promote diversity and equal opportunity.
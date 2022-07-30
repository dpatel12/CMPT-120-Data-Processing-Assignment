# CMPT 120: Data Processing Assignment
### Introduction
The Data Processing Assignment was the final assignment of CMPT 120 in the Fall 2019 semester at SFU. Approximately 2 weeks were given to complete the assignment. The option to complete the assignment as a team existed however this assignment was completed individually. Provided code was given by Professor Diana Cukierman to read and write to .csv files, found as in **codeProvided.py** and copied to the final assignment file, but the rest of the program is my work. The assignment was written in Python 3.7 and is included as **dataProcessing.py**.

In addition to the programming assignment, we were tasked with creating a flowchart to better visualize and explain the top (global) level of the file, which has been included as **Flowchart.jpg**.

The original assignment requirement document has been included as **Description.pdf**.

### Requirements
For this assignment, we were tasked with:
* Processing the data from a .csv file that would follow a specific format.
* Display some statistics obtained by running some tests with the data.
* Create a .csv file from the processed data.

It was required that the program must include:
* 4 fruitful functions
* 2 void functions
* 5 functions receiving parameters
* A reasonable main level
* Trace printing

Note that the comments have been left in the .py file to make understanding the code easier for the marker.

### Explanation of what the program does
The data file that will be provided will be of the format:
> NameA   4 2 1 2 4 2 4 4 5 2 2 1 5 2 4 3 1 1 3 3 5\
> NameB   5 2 1 2 4 5 4 4 1 2 2 2 4 4 4 3 1 2 3 3 2\
> NameC   4 1 2 1 2 1 2 5 1 1 1 1 4 2 2 1 5 1 3 4 1

Where the first line represents the student that is responding to a survey, and the numbers that follow the student's name in the line represent their response to a question.

The input file can contain any number of names, and any number of responses. However, the number of responses per name must be the same for all names. For example, if NameA had responded to 10 questions then any consecutive responder must have responded to 10 questions as well.

From the input file, we were tasked with analyzing the similarity of responses between any pairs of students, with us having to print:
| Percentage/number of similar responses between a pair of students | Message to output to the user |
| --- | ---|
| If 90% of the responses were the same between the students (the same number in the same column) | Output "really have a lot in common (>90%)!" |
| If 50% or more of the responses were the same | Output "have about half opinions in common!" |
| 2 or more responses to questions were the same | Output "have just a few opinions in common (<50%)" |
| Less than 2 responses the same | Output "have nothing in common!" |

After printing the designated text to the user, the mean response value was calculated per student and was outputted to a different .csv file in the following format:
> NameA 2.85714285714285\
> NameB 2.85714285714285\
> NameC 2.142857143

With the student's name beside their corresponding mean response value.
An example input file can be found as **IN_all_data.txt** and the corresponding output file as **OUT_perstudent.csv**.


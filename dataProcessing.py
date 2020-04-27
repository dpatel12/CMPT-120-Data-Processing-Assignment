###  Data Processing Assignment
###
###
###  Brendan Saw
###  301393286 bsaw@sfu.ca


#provided function
def read_string_list_from_file(the_file):
    '''
    Author: Diana Cukierman
    If you revise, indicate so here and how:

    
    READING OF TEXT FILE
    String ---> List of Strings

    the_file is a string representing several 'lines',
    each line is a string, possibly including spaces , and ending with \n

    THIS FUNCTION GENERATES AND RETURNS  A LIST OF STRINGS

    Assumptions:
    1) the_file is in the same directory (folder) as this program 
    2) lines have a "\n" at the end, that is, after each 'line' (student)
       in the file , there is a new line character ("\n"), including the last
       line  in the_file
    3) for this problem each line has alphabetic and numeric values
       separated with spaces, but this does not affect this function. 
    '''
    
    fileRef = open(the_file,"r")      # opening file to be read
    localList_ofstrings=[]            # new list being constructed 
    
    for line in fileRef:
        string = line[0:len(line)-1]  # -1 to eliminate trailing '\n'
                                      # of each line 
                                    
        localList_ofstrings.append(string)      # adds string (line) to list
        
    fileRef.close()  
        
    #........
    print ("\n JUST TO TRACE, the list OF STRINGS is:\n")
    print(localList_ofstrings)
    
    #print("\n TRACE printing input file one STRING per line\n")
    #for element in localList_ofstrings:
    #    print (element)  # element is a string for one student
    #........
    
    return localList_ofstrings 

#provided function
def write_perstudent_to_file(lout_Strings,the_file):

    '''
    Author: Diana Cukierman
    If you revise, indicate so here and how:

    list od Strings --> ()  (A file is saved it the current folder)

    You need to ensure that lout_Strings has the appropriate contents
    according to the assumptions (and needed to write a text file)

    Assumptions:
    1) the_file will be saved in the same directory (folder) as this program 
    2) lout_Strings is  formatted so that it
       2.0) is a list of strings
       2.1) each string contains one student's  data  
       2.2) each  string for one student includes the name
       2.3) each  string includes a comma after the students' name,then the avg
       2.4) each string includes a new line ('\n') at the end
    '''
    
    fileRef = open(the_file,"w") # opening file to be written
    for line in lout_Strings:
        fileRef.write(line)
                                    
    fileRef.close()
    
    return




######################################### END OF PROVIDED FUNCTIONS

##########VOID FUNCTION #1: PRINT FUNCTION
def printFunction1():
    print('''WELCOME to the CMPT 120 Preferences and Similarities system! 
 ============================================================ 

This system will process data from the file: IN_all_data.txt
  (the file with that exact name needs to be in this folder!!!) 

The file has answers of students opinions
  from 1 - strongly disagree  to 5- strongly agree

The system will produce:
  - an output file with avgs per student: OUT_perstudent.csv
  - several statistics

You will also be able to check if pairs of students are similar\n''')
#call print function
printFunction1()

#Ask how what is the maximum number of pairs that is allowed
maxPairsInt = False
while maxPairsInt == False:
    maxPairs = input("Maximum number of pairs ==> ")
    if maxPairs.isdigit():
        #if the input is an integer, then exit out of while loop by setting flag to true
        maxPairsInt = True
    else:
        print(" What you provided is not an integer  number, please re-type")

print("\nInitial processing ...")

#DIana's function called
readString = read_string_list_from_file("IN_all_data.txt")



agrees = 0
count1 = 0
newStringNoText = []
newIntNoText = []
nameList = []
#for all items in the list created by Diana's function
for i in readString:
    #counter for how many 4s or 5s
    agreesCounter = 0

    tempList = []
    tempListInt = []
    tempListName = ""

    #for all spaces in each string in the list created by Diana's function
    for j in readString[count1]:

        # if the space is a digit
        if j.isdigit():
            #tempList used to group information and then put into newStringNoText
            tempList = tempList + [j]
            #tempListInt used to group information and then put into newIntNoText
            tempListInt = tempListInt + [int(j)]
        if j == "4" or j == "5":
            #if 4 or 5 then agrees counter goes up
            agreesCounter = agreesCounter + 1
        if j.isalpha():
            #if j is alpha, put into tempListName. This is for the list of names
            tempListName = tempListName + j

    #this is used later to calculate the averages        
    newStringNoText = newStringNoText + [tempList]

    #this is used exclusively for the print one student
    newIntNoText = newIntNoText + [tempListInt]

    #this is used to get only the names of the students into a list
    nameList = nameList + [tempListName]

    #check the max amount of agrees of all the students... we use the agrees int later
    if agrees < agreesCounter:
        agrees = agreesCounter
    count1 = count1 + 1




#create a new list averages
averages = []
for j in newStringNoText[0]:
    #just to make the averages list sufficiently long to the number of responses per student
    averages = averages + [[int(j)]]

#since we let the averages list be based on the first person's responses, then add the other people's
#responses into their positions. This is so we are able to take the averages of all the
#first spot... second spot, etc..
if len(newStringNoText)>1:
    for i in range(len(newStringNoText)-1):
        count2 = 0
        for j in newStringNoText[i+1]:
            averages[count2] = averages[count2] + [int(j)]
            count2 = count2 + 1

#print("\n now printing one STRING per line\n")

list1 = []
for i in readString:
    
    #print(i)
    list1 = list1 + [[i]]
'''
print("\n JUST TO TRACE, the list OF LISTS is:\n")

print(list1)


print("\n now printing one LIST per line\n")
'''
print("\n TRACE printing one STUDENT (name and LIST responses) per line\n")

########## FRUITFUL FUNCTION 1
#calculating the studs
def calculateStuds(x):
    countA = 0
    for i in list1:
        #this is the print, here we use the nameList and newIntNoText
        print(nameList[countA], "--", newIntNoText[countA])
        x = x + 1
        countA = countA + 1
    return x

studs = calculateStuds(0)

#############FRUITFUL FUNCTION 2
#calculate the nqns
def calculateNqns(x):

    counter = 0
    #get only the digits and count how many there are. This generates the number of nqns
    for i in list1[0][0]:
        if i.isdigit():
            x = x + 1
        counter = counter + 1
    return x
nqns = calculateNqns(0)

###########VOID FUNCTION 2: ANOTHER PRINT FUNCTION
def printFunction2():
    print("\n studs, nqns: {} {}\n".format(studs, nqns))

    print('''Processing all students' responses  ...


All students' responses have been processed ...


SOME STATS!! 
============= \n''')

        
    print('''The input file had responses from: {} students
Each student responded to: {} questions
The maximum agrees (response 4 or 5) in a student was: {}

The averages per question were: \n'''.format(studs, nqns, agrees))

    print("question num - average")
printFunction2()

count3 = 0
#here is when we use the averages
for i in averages:
    averages[count3] = sum(averages[count3])
    #this is the actual calculation of the mean value
    averages[count3] = averages[count3]/studs
    #rounding it up to two decimals so it doesn't look as ugly
    averages[count3] = round(averages[count3], 2)
    count3 = count3 + 1

count4 = 1
#printing it out nicely
for i in averages:
    print(str(count4) + " - " + str(i))
    count4 = count4 + 1

###################LARGEST NUMBER CALCULATION: FRUITFUL FUNCTION 3
#calculating question which has the most agreed values
def largestNumCalc(x):
    for i in averages:
        if i>x:
            x = i
    return x
largestNum = largestNumCalc(0)

mostAgreed = []
count5 = 1
for i in averages:
    if largestNum == i:
        #creating a list of the most agreed values
        mostAgreed = mostAgreed + [str(count5)]
    count5 = count5 + 1

print("\nThe most agreed questions were:\n")
print(', '.join(mostAgreed))

print('''\n NOW... LET'S SEE SIMILARITIES BETWEEN PAIRS OF STUDENTS!!... 
 ============================================================ 

You can check up to {} pairs\n'''.format(maxPairs))



#while loop flag
responseEnd = False
whileCounter = 0
#see if it is the first run of the while loop since they have different dialogue
firstRun = True

#conditions of either inputs having END, or the whileCounter being exceeded
while ((responseEnd == False) and whileCounter < int(maxPairs)):
    #if it is the first run
    if firstRun:
        firstInput = input("Pleace provide the first name in the pair (or END to finish) ==> ")
        firstRun = False
    # if it isnt the first run, alter the dialogue slightly
    else:
        firstInput = input("Another pair? provide the first name (or END to finish) ==> ")

    #make sure to check it firstInput == END before anything else, so it can be terminated immediately
    if firstInput == "END":
        print("\n***** Ok, I see that you do not want to consult any pairs...\n")
        responseEnd = True
    #by putting everything in this else, we make sure that it isnt called after firstInput == END
    else: 
        secondInput = input("Please provide the second name in the pair ==> ")
        #same thing if second input == END
        if secondInput == "END":
            print("\n***** Ok, I see that you do not want to consult any pairs...\n")
            responseEnd = True
        else:
            count6 = 0
            #reset firstInputTrue and secondInputTrue to be false to prepare for next while loop iteration
            firstInputTrue = False
            secondInputTrue = False
            for i in nameList:
                #this checks whether the inputted value is in the nameList
                if firstInput == nameList[count6]:
                    num1Index = count6
                    firstInputTrue = True
                #this check whether the second inputted value is in the namelist
                if secondInput == nameList[count6]:
                    num2Index = count6
                    secondInputTrue = True
                count6 = count6 + 1
            #if both input values are in the list of names, then continue on
            if firstInputTrue and secondInputTrue:
                countSimilar = 0
                count7 = 0
                #this is checking whether the number of num1 is the same as the number of num2 with the same indices
                for i in newStringNoText[num1Index]:
                    if newStringNoText[num1Index][count7] == newStringNoText[num2Index][count7]:
                        countSimilar = countSimilar + 1
                    count7 = count7 + 1
                print("TRACE similars {}".format(countSimilar))

                #turn results of count similar into a percentage for easy calculations
                percentageSimilar = countSimilar / nqns
                if percentageSimilar >= 0.9:
                    print("** {} and {} really have a lot in common (>90%)!\n".format(firstInput, secondInput))
                elif percentageSimilar >= 0.5:
                    print("** {} and {} have about half opinions in common!\n".format(firstInput, secondInput))
                elif countSimilar >= 2:
                    print("** {} and {} have just a few opinions in common (<50%)!\n".format(firstInput, secondInput))
                else:
                    print("** {} and {} have nothing in common!\n".format(firstInput, secondInput))
                
            #if there is an input value that isnt in the list of names, then we can't continue on 
            else:
                print("** Sorry! at least one name is not in the data\n")
                
            #always increase the while loop counter otherwise will go on forever
            whileCounter = whileCounter + 1
            #if the while counter ends up equaling the max number, say some dialogue
            if whileCounter == int(maxPairs):
                print("***** Sorry you cannot check more pairs.. you reached the maximum: {}".format(maxPairs))

#this creates an average list that is meant to later be put into the .csv file

###############FRUITFUL FUNCTION 4
def avgCalculations(x):
    count8 = 0
    for i in newStringNoText:
        tempAvgList = 0
        for j in newStringNoText[count8]:
            tempAvgList = tempAvgList + int(j)
        #calculating the average
        tempAvgList = tempAvgList/nqns
        count8 = count8 + 1
        x = x + [tempAvgList]
    return x
avgList = avgCalculations([])




print("\nOutput file being saved ...\n")
print("\nTRACE list of strings ready to save to output file, one per line")

############## FRUITFUL FUNCTION 5
def nameListWriteFunc(x):
    count9 = 0
    for i in nameList:
        #combining the nameList and the avgList
        x = x + ["{},{}\n".format(i, avgList[count9])]
        #printing everything out nicely
        print("{},{}\n".format(i, avgList[count9]))
        count9 = count9 + 1
    return x

nameListWrite = nameListWriteFunc([])

#diana's file to write to the .csv file
write_perstudent_to_file(nameListWrite, "OUT_perstudent.csv")
    
print("\nAll done! Bye!")













        

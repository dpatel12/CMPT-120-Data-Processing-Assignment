### CMPT 120 
### author Diana Cukierman
###
###  Data Processing: preferences and similarities
###  
###  CODE PROVIDED      

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
        

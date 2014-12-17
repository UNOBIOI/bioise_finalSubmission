from Bio.Seq import Seq

#Function checks to make user's file is correct and then sequence in the file
def file_check():

    #Boolean variable used throughout the function, changes to false if there is a fail
    checker = True
    #Variable used to store the user notifications when a check fails.
    response = ''

    #Opening the users inputed file
    f = open('user_alignInput.txt', 'r')
    fline = f.readline()
    secline = f.readline()
    f.close()
    seq = Seq(secline)

    #Counting the valid base pairs in sequence
    Gcount = seq.count('G')
    Ccount = seq.count('C')
    Acount = seq.count('A')
    Tcount = seq.count('T')
    sum = Gcount + Ccount + Acount + Tcount

    #If the sum of the present base pairs does not equal the length of the sequence then it fails
    if '\n' in seq:
        if sum != len(seq) - 1:
            checker = False
            response = response + 'Sequence contains improper characters\n'
    else:
        if sum != len(seq):
            checker = False
            response = response + 'Sequence contains improper characters\n'

    #checks to makes sure the sequence is atleast 30 nucleotides in length
    if len(secline) < 30:
        checker = False
        response = response + 'Minimum of 30 characters required\n'

    #checks to make sure there are no more than 2 new lines  
    #lines = 0
    #with open('user_seqInput.fa', 'r') as in_file:
    #    for line in in_file:
    #        lines += 1
    #if lines > 2:
    #    checker = False
    #    response = response + 'Too many new lines' 
   
    #checks the first line of the fasta file.
    if fline[0] != '>':
        checker = False
        response = response + 'The first line is invalid\n'


    #Returning the boolean variable and the user notifications
    return checker, response

#Checks the user's input in the text box
def textbox_check(s):
    checker = True
    response = ''
    s = s.upper()
    seq = Seq(s)
    Gcount = seq.count('G')
    Ccount = seq.count('C')
    Acount = seq.count('A')
    Tcount = seq.count('T')
    sum = Gcount + Ccount + Acount + Tcount

    if sum != len(seq):
        checker = False
        response = 'Characters are not valid\n'
 
    if len(seq) < 30:
        checker = False
        response = response + 'Minimum of 30 characters required'
    
    return (checker, response)

#def main():
#
#    checker, response = file_check()
#    print checker
#    print response

#main() 

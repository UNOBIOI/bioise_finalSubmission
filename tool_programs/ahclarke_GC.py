#!/usr/bin/python3.2
#
# Name: Alex Clarke
# Class: BIOI 3500-001
# Program #: 1, part 1
# Due Date: 23 January 2014
#
# Honor Pledge: On my honor as a student of the University of Nebraska at 
#               Omaha, I have neither given nor received unauthorized help 
#               on this homework assignment.
#
# NAME: Alex Clarke
# EMAIL: ahclarke@unomaha.edu
# NUID: 078
#
# Colleagues: None
#
# This program calculates the GC content of a fragment of DNA, given its 
# sequence from the user.

def main():
    # Get the DNA sequence from the user.
    print("Enter a sequence:  ", end="")
    seq = str(input()).upper()

    a = 0 # The number of A's in the sequence
    c = 0 # The number of C's in the sequence
    g = 0 # The number of G's in the sequence
    t = 0 # The number of T's in the sequence
    
    # Count the number of A's, C's, G's, and T's.
    for char in seq:
        if char == "A":
            a += 1
        elif char == "C":
            c += 1
        elif char == "G":
            g += 1
        elif char == "T":
            t += 1

    # Calculate and print the GC content.
    gc = ((c + g) / (a + c + g + t)) * 100
    print("%%GC content:  %.2f%%" % gc)

if __name__ == '__main__':
    main()

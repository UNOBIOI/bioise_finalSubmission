def get_gcCont(seq):
    # Get the DNA sequence from the user.
    seq = str(seq).upper()

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
    gc = ((c + g) / float((a + c + g + t)) * 100)
    gc = str(round(gc, 3)) + str(" %")
    #print("%%GC content:  %.2f%%" % gc)
    return gc

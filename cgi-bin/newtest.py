#!/usr/bin/python

#Import functions of other programs
#import getseq
#from .. import seq_apps

#Import modules for CGI handling
import cgi, cgitb 

#Import Biopython modules
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
seq = form.getvalue('seq')
option = form.getvalue('dropdown')
length = str(len(seq))
messenger_rna = Seq(seq, IUPAC.unambiguous_dna)
trans = messenger_rna.translate()

# test for submitting string
#subname = form.getvalue('subname')

# send seq to new program test and output html
#getseq.showseq(seq)
#makeFASTA.writefasta(seq)

# Checkbox value test
align_OPT = form.getvalue('alignment')
comp_OPT = form.getvalue('composition')
trans_OPT = form.getvalue('translation')
geneCR_OPT = form.getvalue('gene')

numA = 0
numC = 0
numT = 0
numG = 0
for base in seq:
    if base == 'A':
        numA = numA + 1
    elif base == 'G':
        numG = numG + 1
    elif base == 'C':
        numC = numC + 1
    elif base == 'T':
        numT = numT + 1

numA = str(numA)
numG = str(numG)
numC = str(numC)
numT = str(numT)

print 'Content-type:text/html\r\n\r\n'
print "<html>"
print "<head>"
print "<title>Bioinformatics Tool Wrapper</title>"
print "<h1>DNA Sequence Input</h1>"
print "<img src='../DNA.jpg' alt='Unsequenced Regions of Chromosomes' width='400px'/>"
print "</head>"
print "<body>"
print "<h2>Your sequence was %s </h2>" % (seq)
if option == 'length':
    print "<h3>It is %s bases long </h3>" % (length)
elif option == 'nucCount':
    print "<h3>There are %s A bases in your sequence</h3>" % (numA)
    print "<h3>There are %s G bases in your sequence</h3>" % (numG)
    print "<h3>There are %s C bases in your sequence</h3>" % (numC)
    print "<h3>There are %s T bases in your sequence</h3>" % (numT)
print "<h2>The translation of your sequence is %s </h2>" % (trans)
if align_OPT == 'alignment':
    print "<h3>You selected alignment option</h3>"
if comp_OPT == 'composition':
    print "<h3>You selected composition option</h3>"
print '<a href="http://bioise2014.ist.unomaha.edu/test.html" target="_self">HOME</a>'
print '<a href="http://bioise2014.ist.unomaha.edu/cgi-bin/user_input.fa" target="_self">FASTA File Input</a>'
# test for printing string with submit button
#print "<h3>String with submit %s </h3>" % (subname)
print "</body>"
print "</html>"


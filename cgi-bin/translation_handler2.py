#!/usr/bin/python

#Import modules for CGI handling
import cgi, cgitb


#Import functions of other programs
import tools.seq_apps as sa
import tools.aa_comp as aac
#Import Biopython modules
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
#seq = form.getvalue('seq')
#fileitem = form['fastafile'].value
#radio = form.getvalue('suboption')

#if radio == 'file':
#    # read file
#    fp = open('userinput.txt', 'wb')
#    fp.write(fileitem)
#    fp.close()
#    # this next part is just so seq gets created, runBlast won't
#    # take in seq anymore, just read the created file
#    # below needs to create a fasta file from file above
#    fp = open('userinput.txt', 'r')
#    line = fp.readline()
#    seq = str(line)
#    fp.close()

# need to make calls to functions in seq_apps.py
#messenger_rna = Seq(seq, IUPAC.unambiguous_dna)
#trans = str(sa.translation(seq))
#rev = sa.reverseComp(seq)
#aaComp = aac.aa_composition(trans)

print 'Content-type:text/html\r\n\r\n'
print '<html>'
print '<head>'
print '<style>'
print '    #header {'
print '        color:black;'
print '        text-align: center;'
print '        padding:5px;'
print '        font-size: 20pt;'
print '    }'
print '    h1 a, h1 a:active, h1 a:visited{'
print '        color:black;'
print '        text-decoration: none;'
print '    }'
print '    h1 a:hover {'
print '        text-decoration: underline;'
print '    }'
print '    body {'
print '        background-image: url("../images/dna.jpg");'
print '        background-size: 100%;'
print '        background-attachment: fixed;'
print '        background-repeat: repeat-y;'
print '        font-family: \'Open Sans\', sans-serif;'
print '    }'
print '    #background_rectangle {'
print '        background-color:rgba(255, 255, 255, 0.4);'
print '        border-style: solid;'
print '        border-color: black;'
print '    }'
print '    #input {'
print '        text-align: center;'
print '        font-size: 16pt;'
print '    }'
print '    #footer {'
print '        color: black;'
print '        clear: both;'
print '        text-align:center;'
print '        padding-top: 140px;'
print '        padding-bottom: 28px;'
print '    }'
print '    h3 {'
print '        padding-bottom: 30px;'
print '    }'
print '</style>'
print '    <title>Bioinformatics Tool Wrapper</title>'
print '</head>'
print '<body>'
print '<div id="background-rectangle">'
print '<div id="header">'
print '<h1><a href="http://bioise2014.ist.unomaha.edu/home.html">CSCI 4830 Project</a></h1>'
print '<h2>Translation and Reverse Composition Tool</h2>'
print '</div>'
print '</div>'
print '<div id = "results">'
#print ' <h2>Translation of sequence: %s </h2>' % trans
#print ' <h2>Reverse complement of sequence: %s </h2>' % rev
print ' <h2>Amino Acid Composition:</h2>'
print '<h3>'
#for aa in aaComp:
#    aa = str(aa)
#    print '%s' % aa
#    print '<br>'
print '</h3>'
print '</div>'
print '<div id="footer">'
print '    @Tool Wrapper'
print '</div>'
print '</body>'
print '</html>'

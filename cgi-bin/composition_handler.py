#!/usr/bin/python 

#Import modules for CGI handling
import cgi, cgitb
 

#Import functions of other programs
import tools.seq_apps as sa
import tools.gcContent as gcCont
import tools.makeBLASTfile as mbf
import tools.validation as validate

#Import Biopython modules
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
seq = form.getvalue('seq')
fileitem = form['fastafile'].value
radio = form.getvalue('suboption')

if radio == 'file':
    # read file
    fp = open('userinput.txt', 'wb')
    fp.write(fileitem)
    fp.close()
    fp = open('user_seqInput.fa', 'wb')
    fp.write(fileitem)
    fp.close()
    checker, response = validate.file_check()
    if (checker):    
        seq = mbf.getSeq()
else:
    checker, response = validate.textbox_check(seq)

# need to make calls to functions in seq_apps.py
#messenger_rna = Seq(seq, IUPAC.unambiguous_dna)
a_comp, g_comp, c_comp, t_comp = sa.composition(seq)
gc = gcCont.get_gcCont(seq)


print 'Content-type:text/html\r\n\r\n'
print '<html>'
print '<head>'
print '<style>'
print '    #header {'
print '        background-color:black;'
print '        color:white;'
print '        text-align:center;'
print '        padding:5px;'
print '    }'
print '    #nav {'
print '        width:35%;'
print '        float:left;'
print '        padding:5px;'
print '    }'
print '    #section {'
print '        width:350px;'
print '        float:left;'
print '        padding:10px;'
print '    }'
print '    #footer {'
print '        background-color:black;'
print '        color:white;'
print '        clear:both;'
print '        text-align:center;'
print '        padding:5px;'
print '    }'
print '</style>'
print '    <title>Bioinformatics Tool Wrapper</title>'
print '</head>'
print '<body background="../images/images2.jpg" bgpropeties="fixed">'
print '<div id="header">'
print ' <h1>Composition Tool</h1>'
print '</div>'
if (checker):
    print '<div id = "results">'
    print ' <h2>A: %s</h2>' % a_comp
    print ' <h2>G: %s</h2>' % g_comp
    print ' <h2>C: %s</h2>' % c_comp
    print ' <h2>T: %s</h2>' % t_comp
    print ' <h2>GC Content: %s</h2>' % gc
    print ' <h2><a href="http://bioise2014.ist.unomaha.edu/tool_pages/composition.html">New Submission</a></h2>'
    print ' <h2><a href="http://bioise2014.ist.unomaha.edu/home.html">Home</a></h2>'
    print '</div>'
else:
    print '<div id = "error">'
    print ' <h2>Error</h2>'
    print ' <h2>%s</h2>' % response
    print ' <h2><a href="http://bioise2014.ist.unomaha.edu/tool_pages/composition.html">Back to Composition Tool</a></h2>'
    print '</div>'
print '<div id="footer">'
print '    @Tool Wrapper'
print '</div>'
print '</body>'
print '</html>'

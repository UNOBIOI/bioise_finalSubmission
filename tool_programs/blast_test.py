from Bio import SeqIO
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML

#import depends on the version of python.
try:
    from StringIO import StringIO # Python 2
except ImportError:
    from io import StringIO # Python 3

#this opens and reads the fasta file. This is where the user inputted sequence will be inputted in fasta format
f_record = next(SeqIO.parse('sequence.fasta', 'fasta'))

#run blast and save the results as result_handle
result_handle = NCBIWWW.qblast('blastn', 'nr', f_record.format('fasta'))

#create and write an xml file for the blast results
save_file = open('sequence.out', 'w')
blast_results = result_handle.read()
save_file.write(blast_results)
save_file.close()


print('Parsing the results and extracting info...')

# option 1 -- open the saved file to parse it
# option 2 -- create a handle from the string and parse it
string_result_handle = StringIO(blast_results)
b_record = NCBIXML.read(string_result_handle)

# now get the alignment info for all e values greater than some threshold
E_VALUE_THRESH = 0.1

for alignment in b_record.alignments:
    for hsp in alignment.hsps:
        if hsp.expect < E_VALUE_THRESH:
            print('****Alignment****')
            print('sequence: %s' % alignment.title)
            print('length: %i' % alignment.length)
            print('e value: %f' % hsp.expect)
            print(hsp.query[0:75] + '...')
            print(hsp.match[0:75] + '...')
            print(hsp.sbjct[0:75] + '...')


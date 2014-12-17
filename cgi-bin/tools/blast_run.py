from Bio import SeqIO
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML

def runBlast():
    try:
        from StringIO import StringIO #Python 2
    except ImportError:
    	from io import StringIO #Python 3

    #Parsing the fasta file into a BioPython format
    #The user's FASTA file is used here. 	
    f_record = next(SeqIO.parse('alignBLAST.fa', 'fasta'))

    #Accessing BLAST and saving the results to the variable
    result_handle = NCBIWWW.qblast('blastn', 'nr', f_record.format('fasta'))
   
    #File is created and the result will be imported to it.
    save_file = open('sequence.out', 'w')

    #Reading the blast reslts to the variable
    blast_results = result_handle.read()

    #saving the blast result to the file and closing the file. 
    save_file.write(blast_results)
    save_file.close()

    # option 1 -- open the saved file to parse it
    # option 2 -- create a handle from the string and parse it
    string_result_handle = StringIO(blast_results)
    b_record = NCBIXML.read(string_result_handle)

    # now get the alignment info for all e values greater than some threshold
    E_VALUE_THRESH = 0.1

    #Variable used for the return of the BLAST output
    blast_output = ''
    headings = []
    lengths = []
    e_vals = []

    #Searching for BLAST results with appropriate E value
    for alignment in b_record.alignments:
        for hsp in alignment.hsps:
            if hsp.expect < E_VALUE_THRESH:
                #blast_output += '\nSequence: %s\n' % alignment.title
                #blast_output += 'Length: %i\n' % alignment.length
                #blast_output += 'e value: %f\n' % hsp.expect
                headings.append(alignment.title)
                lengths.append(alignment.length)
                e_vals.append(hsp.expect)   

    #return str(blast_output)
    return headings, lengths, e_vals

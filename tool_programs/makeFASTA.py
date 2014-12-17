from Bio.Seq import Seq
from Bio.Blast import NCBIWWW
from Bio import SeqIO


def writefasta(seq):
#create file to write the sequence as a fasta file. 
    f = open("user_input.fasta","w")
    f.write(">user's input\n" + seq)
    f.close()



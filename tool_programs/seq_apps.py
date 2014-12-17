from Bio.Seq import Seq
from Bio.Blast import NCBIWWW
from Bio import SeqIO


# reverse compliment
def reverseComp(seq):
    seq = seq.upper()
    seq = Seq(seq)
    revComp = seq.reverse_compliment()
    
    return revComp

#counting the composition
def composition(seq):
    seq = seq.upper()
    seq = Seq(seq)
    a_comp = seq.count("A")
    g_comp = seq.count("G")
    c_comp = seq.count("C")
    t_comp = seq.count("T")

    return a_comp, g_comp, c_comp, t_comp

# protein translation
def translation(seq):
    seq = seq.upper()
    seq = Seq(seq)
    trans = seq.translate()
    
    return trans


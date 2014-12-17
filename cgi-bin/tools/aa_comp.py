from Bio.SeqUtils.ProtParam import ProteinAnalysis

def aa_composition (seq):

    protein = ProteinAnalysis(seq)

    aa =protein.count_amino_acids()

    aacomp = 'A:\t%i,' % aa['A'] 
    aacomp += 'C:\t%i,' % aa['C']
    aacomp += 'E:\t%i,' % aa['E']
    aacomp += 'D:\t%i,' % aa['D']
    aacomp += 'G:\t%i,' % aa['G']
    aacomp += 'F:\t%i,' % aa['F']
    aacomp += 'I:\t%i,' % aa['I']
    aacomp += 'H:\t%i,' % aa['H']
    aacomp += 'K:\t%i,' % aa['K']
    aacomp += 'M:\t%i,' % aa['M']
    aacomp += 'L:\t%i,' % aa['L']
    aacomp += 'N:\t%i,' % aa['N']
    aacomp += 'Q:\t%i,' % aa['Q']
    aacomp += 'P:\t%i,' % aa['P']
    aacomp += 'S:\t%i,' % aa['S']
    aacomp += 'R:\t%i,' % aa['R']
    aacomp += 'T:\t%i,' % aa['T']
    aacomp += 'W:\t%i,' % aa['W']
    aacomp += 'V:\t%i,' % aa['V']
    aacomp += 'Y:\t%i,' % aa['Y']

    aacomp = aacomp.split(",")
    return aacomp


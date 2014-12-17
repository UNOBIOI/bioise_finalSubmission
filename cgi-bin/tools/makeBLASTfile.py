from Bio import SeqIO

def copyFile():
    outFile = open("alignBLAST.fa", "w")

    for seq_record in SeqIO.parse("user_alignInput.txt", "fasta"):
        outFile.write(">")
        outFile.write(str(seq_record.description))
        outFile.write("\n")
        outFile.write(str(seq_record.seq))
   
    outFile.close()

def makeFile(seq):
     outFile = open("alignBLAST.fa", "w")
     
     outFile.write(">")
     outFile.write("User Input")
     outFile.write("\n")
     outFile.write(str(seq))

     outFile.close()

def getSeq():
    for seq_record in SeqIO.parse("user_seqInput.fa", "fasta"):
        seq = str(seq_record.seq)
        
    return seq

#def main():
#
#    seq = 'AGAGAGAGAGAGATCCAGAGF'

#    makeFile(seq)
#     seq = getSeq()
#     print seq
     
#main()

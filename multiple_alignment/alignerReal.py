from Bio import AlignIO

records = AlignIO.parse("X4_14C.fasta","fasta")

with open("X4_14C.clustalw","w+") as write_file:
    AlignIO.write(records, write_file, "clustal")

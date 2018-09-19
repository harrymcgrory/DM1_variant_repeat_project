from Bio import AlignIO
from statistics import mode

records = AlignIO.read("data/X4_14Caligned.clustalw","fasta")
consensus_seq = ""
for i in range(len(records[0])):
    bases = list(records[:, i])
    mode_base = max(set(bases), key=bases.count)
    consensus_seq += mode_base

consensus_seq = consensus_seq.replace("-","")
print(consensus_seq)

#print(len(records))
#for record in records:
#    for r in str(record):
#        print(r, end="")
#    break
#counter = 0
#for record in records:
#    s = "seq{}".format(counter)
#    record.id = ""
#    record.description = s
#    counter += 1

#with open("multiple_alignment/data/X4_14C.fasta","w") as write_file:
#    SeqIO.write(records, write_file, "fasta")

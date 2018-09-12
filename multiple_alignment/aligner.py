from Bio import SeqIO

records = list(SeqIO.parse("multiple_alignment/data/X4_14C.fastq","fastq"))

counter = 0
for record in records:
    s = "seq{}".format(counter)
    record.id = ""
    record.description = s
    counter += 1

with open("multiple_alignment/data/X4_14C.fasta","w") as write_file:
    SeqIO.write(records, write_file, "fasta")
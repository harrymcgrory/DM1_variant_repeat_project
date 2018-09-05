from library import *
import matplotlib.pyplot as plt
import random
import linecache

fastq_file = open("DNAReadData.fastq", "r")
file_content = fastq_file.read()

line = linecache.getline("DNAReadData.fastq", 16)
line = line.rstrip()

probs = quality_to_probability(line)

##for i in range(len(probs)):
##    print(line[i],probs[i])

plt.plot(range(len(probs)), probs, "b")
plt.axis([0, len(probs), 0, max(probs)])
plt.xlabel("Location in sequence")
plt.ylabel("Probability of read being incorrect")
plt.show()

##fastq_file = "DNAReadData.fastq"
##data = []
##for base in linecache.getline(fastq_file,4):
##    data.append([])
##
##
##line_no = 4
##for row in range(20):#range(sum(1 for line in open("DNAReadData.fastq"))):
##    if line_no % 4 == 0:
##        line = ""
##        line = linecache.getline(fastq_file, line_no)
##        line = line.rstrip()
##        line_probs = quality_to_probability(line)
##        for index, prob in enumerate(line_probs):           
##            data[index].append(prob)
##    line_no += 1
##
##print([i[:20] for i in data[1:10]])
##
##plt.boxplot([i[:20] for i in data[1:10]])
##plt.show()
##        


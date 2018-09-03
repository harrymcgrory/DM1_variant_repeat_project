from library import *
import matplotlib.pyplot as plt
import random
import linecache

fastq_file = open("DNAReadData.fastq", "r")
file_content = fastq_file.read()

line = linecache.getline("DNAReadData.fastq", 16)
line = line.rstrip()

probs = quality_to_probability(line)
print(line)
print(probs)
for i in range(len(probs)):
    print(line[i],probs[i])

plt.plot(range(len(probs)), probs, "b")
plt.axis([0, len(probs), 0, max(probs)])
plt.show() 


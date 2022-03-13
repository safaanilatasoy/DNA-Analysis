# DNA Toolset/Code Testing
import data as data
import labels as labels

from DNAProccessing import *
import random

# Creating random DNA sequence
seq = ''.join([random.choice(Nucleotides)
               for nuc in range(20)])

DNAStr = validateSeq(seq)
fre = countNucFre(seq)
rate_nuc = countNucRate(seq)

# for the virtualization we get value from array
data=rate_nuc.values()
labels=rate_nuc.keys()



# Printing Results
print("DNA : ", DNAStr)
print("Counting Nucleotides : ", fre)
print("Rate of Nucleotits : ", countNucRate(seq))
createPieChart(data,labels)





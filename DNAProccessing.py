# DNA Toolkit File

import random
import pandas as pd
import matplotlib.pyplot as plt


Nucleotides = ["A", "C", "G", "T"]


# Check the sequence for make sure it is a DNA String

def validateSeq(dna_seq):
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return False
    return tmpseq

# A function that will return frequency of the nucleotides

def countNucFre(seq):
    fre = {"A": 0, "C": 0, "G": 0, "T": 0}
    for nuc in seq:
        fre[nuc] += 1
    return fre


# A function will return rates of the nucleotides

def countNucRate(seq):
    A = round((seq.count('A'))/len(seq)*100)
    C = round((seq.count('C'))/len(seq)*100)
    G = round((seq.count('G'))/len(seq)*100)
    T = round((seq.count('T'))/len(seq)*100)

    rate_nuc = {"A": round((seq.count('A'))/len(seq)*100),
                "C": round((seq.count('C'))/len(seq)*100),
                "G": round((seq.count('G'))/len(seq)*100),
                "T": round((seq.count('T'))/len(seq)*100)}

    return rate_nuc

# A function will shows the rates of the nucleotides as a pie chart

def createPieChart(data,labels):

    plt.figure(figsize=(5, 5))
    plt.pie(data, labels=labels, autopct="%.1f%%")
    plt.show()
    

# A function will replace a certain nucleotide type with a other

def replaceNuc(seq,old,new):
    replaced = seq.replace(old,new)
    return replaced
    


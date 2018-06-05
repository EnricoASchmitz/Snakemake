# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 21:20:02 2018

@author: Ernst
"""

def main():
    gennaam = opengennaam()
    sequentie = opensequentie()
    insertinfo(gennaam, sequentie)

def opengennaam():
    file = open("C:\\Users\\Ernst\\Documents\\GitHub\\Snakemake\\allSequence_GCcontent.txt", "r")
    eiwitlist = ["Name"]

    for line in file:
        if ">" in line and "%" not in line:
            eiwit = line.split("[")[0].strip()
            if "," in line:
                eiwit = eiwit.split(",")[0].strip()
            eiwit = eiwit.split(" ")[1:]
            eiwitstring= " ".join(eiwit)
            eiwitlist.append(eiwitstring)
    return eiwitlist

def opensequentie():
    file = open("C:\\Users\\Ernst\\Documents\\GitHub\\Snakemake\\allSequence_GCcontent.txt", "r")
    seq = ""
    alleseq = ["Sequentie"]
    for line in file:
        if line != "\n":
            if ">" not in line:
                line = line.strip()
                seq += line
        if line == "\n":
            alleseq.append(seq)
            seq = ""
    return  alleseq
    
    

def insertinfo(gennaam, sequentie):
    infile = open("C:\\Users\\Ernst\\Documents\\GitHub\\Snakemake\\InfoFile.txt","r") 
    outfile = open("C:\\Users\\Ernst\\Documents\\GitHub\\Snakemake\\InfoOutfile.txt",'w')
    
    rows = [line.split('\t') for line in infile]
    cols = zip(*rows) # transposes 2Dlist
    cols = list(cols)

    cols.insert(2, gennaam)
    cols.insert(4, sequentie)
    rows = zip(*cols) # transpose back
    outfile.writelines(['\t'.join(row) for row in rows])
    outfile.close()
    print("done writing file")
    
    
    

    
main()
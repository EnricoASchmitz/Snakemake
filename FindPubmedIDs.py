# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 11:35:42 2018

@author: Ernst
"""

from Bio import Entrez




def main():
    eiwitIDs = openfile()
    geneIDs = opengeneids()
    search(eiwitIDs, geneIDs)


#file met de gene ID openen    
def openfile():
    file = open("C:\\Users\\Ernst\\Documents\\GitHub\\Snakemake\\allSequence_GCcontent.txt", "r")
    eiwitlist = []

    for line in file:
        if ">" in line and "%" not in line:
            eiwit = line.split("[")[0].strip()
            if "," in line:
                eiwit = eiwit.split(",")[0].strip()
            eiwit = eiwit.split(" ")[1:]
            eiwitstring= " ".join(eiwit)
            eiwitlist.append(eiwitstring)
    return eiwitlist

def opengeneids():
    bestandID = open("C:\\Users\\Ernst\\Documents\\GitHub\\Snakemake\\GeneIDList.txt", "r")
    geneIDs = ""
    for geneID in bestandID:
        geneIDs += geneID
    geneIDs = geneIDs.splitlines()
    return geneIDs

#zoeken op pubmed met de parameters van get_info(), de gevonden pubmedID's 
#worden terug gebracht naar de main() om later gebruikt te worden om de papers op te halen            
def search(eiwitlist, geneIDs): 
    count = 0
    outfile = open("C:\\Users\\Ernst\\Documents\\GitHub\\Snakemake\\PubmedIDs.txt","w")
    outfile.write("GeneID\tPubmedID\n")   
    Entrez.email = "A.N.Other@example.com"
    for geneid in eiwitlist:
        handle = Entrez.esearch(db="pubmed", term=geneid, retmax=10)
        record = Entrez.read(handle)
        idlist = record["IdList"]
        outfile.write(geneIDs[count]+"\t"+ str(idlist) + "\n")
        count += 1
    print("done writing file")
    outfile.close()

main()
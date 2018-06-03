# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 14:08:23 2018

@author: Ernst

functie: geneIDs ophalen
         sequentie vinden
         gc percentage uitrekenen
"""
from Bio import Entrez

def main():
    geneIDs = openfile()
    findsequence(geneIDs)
    
#file met de gene ID openen    
def openfile():
    file = open("C:\\Users\\Ernst\\Documents\\GitHub\\Snakemake\\GeneIDList.txt", "r")
    geneIDs = ""
    for geneID in file:
        geneIDs += geneID
    geneIDs = geneIDs.splitlines()
    
    return geneIDs

#sequentie zoeken en wegschrijven naar een nieuw bestand
def findsequence(geneIDs):
    out_handle = open('allSequence_GCcontent.fasta', 'w')  
    Entrez.email = "A.N.Other@example.com"
    for geneID in geneIDs:                          #zoeken op geneID
        handle = Entrez.efetch(db="nucleotide", id=geneID, rettype="fasta", retmode="text")
        record = handle.read()
                    #resultaten wegschrijven samen met de bijbehoorde GC content
        out_handle.write(geneID+ " >GC content: " +calculateGCpercent(record)+"\n")
        out_handle.write(record)
    print("done writing file")
    out_handle.close()
        
#GC percentage uitrekenen van de gevonden sequentie
def calculateGCpercent(sequentie):
    totalCount = len(sequentie)
    sequentie = sequentie.upper()
    GCcount = 0

    for nucleotide in sequentie:
        if nucleotide == "C" or nucleotide == "G":
            GCcount += 1
    GCcontent = GCcount / float(totalCount) * 100
    GCcontent = round(GCcontent, 2)
    GCcontent = str(GCcontent) + "%"

    return GCcontent

main()
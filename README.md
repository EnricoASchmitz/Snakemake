#Snakemake Workflow

input file: RNA-Seq-counts.txt

workflow visualisatie: dag.pdf

LET OP: Alle bestandsnamen moeten worden veranderd in de python files en de snakemakefile

Dit project geeft als output een ods file. 
Het bestand bevat: 
            geneid 
            ID 
            Name 
            Kegg 
            Sequentie 
            Pubmed 
            GCPer 
            FastaID 
            BLAST

Het aantal geblasten eiwitten kan veranderd worden door: if count < 1 ; te veranderen naar een ander getal dan 1. Nu wordt er 1 eiwit geblast

Requirements:
    biopython                 1.71
    bioservices               1.5.2
    graphviz                  2.40.1
    pandas                    0.23.0
    python                    3.5.1
    snakemake                 3.11.0
    urllib3                   1.22




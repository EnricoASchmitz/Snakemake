# Snakemake Workflow

input file: RNA-Seq-counts.txt

workflow visualisatie: dag.pdf

LET OP: Alle bestandsnamen moeten worden veranderd in de python files en de snakemakefile

Dit project geeft als output een ods file. 
Het bestand bevat: <br />
            geneid <br />
            ID <br />
            Name <br />
            Kegg <br />
            Sequentie <br />
            Pubmed <br />
            GCPer <br />
            FastaID <br />
            BLAST<br />

Het aantal geblasten eiwitten kan veranderd worden door: if count < 1 ; te veranderen naar een ander getal dan 1. Nu wordt er 1 eiwit geblast

Requirements:<br />
    biopython                 1.71<br />
    bioservices               1.5.2<br />
    graphviz                  2.40.1<br />
    pandas                    0.23.0<br />
    python                    3.5.1<br />
    snakemake                 3.11.0<br />
    urllib3                   1.22<br />




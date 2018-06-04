rule data:
     input:
         "/home/enrico/Desktop/Snakemake/GeneIDList.txt",
         "/home/enrico/Desktop/Snakemake/allSequence_GCcontent.fasta",
         "/home/enrico/Desktop/Snakemake/Kegg.txt",
         "/home/enrico/Desktop/Snakemake/Blast.txt"

rule GENEID:
    input:
        "/home/enrico/Desktop/Snakemake/RNA-Seq-counts.txt"
    output:
        "/home/enrico/Desktop/Snakemake/GeneIDList.txt"
    script:
        "/home/enrico/Desktop/GENEID.py"

rule biopython:
    input:
        "/home/enrico/Desktop/Snakemake/GeneIDList.txt"
    output:
        "/home/enrico/Desktop/Snakemake/allSequence_GCcontent.fasta"
    script:
        "/home/enrico/Desktop/functie.py"

rule KEGG:
    input:
        "/home/enrico/Desktop/Snakemake/RNA-Seq-counts.txt"
    output:
        "/home/enrico/Desktop/Snakemake/Kegg.txt"
    script:
        "/home/enrico/Desktop/KEGG.py"

rule BLAST:
    input:
        "/home/enrico/Desktop/Snakemake/allSequence_GCcontent.fasta"
    output:
        "/home/enrico/Desktop/Snakemake/Blast.txt"
    script:
        "/home/enrico/Desktop/Blast.py"

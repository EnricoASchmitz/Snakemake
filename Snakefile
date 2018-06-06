rule data:
     input:
         "/home/enrico/Desktop/Snakemake/GeneIDList.txt",
         "/home/enrico/Desktop/Snakemake/allSequence_GCcontent.fasta",
         "/home/enrico/Desktop/Snakemake/Kegg.txt",
         "/home/enrico/Desktop/Snakemake/Blast.txt",
         "/home/enrico/Desktop/Snakemake/MergedFile.txt",
         "/home/enrico/Desktop/Snakemake/InfoFile.txt",
         "/home/enrico/Desktop/Snakemake/PubmedIDs.txt",
         "/home/enrico/Desktop/Snakemake/InfoOutFile.txt",
         "/home/enrico/Desktop/Snakemake/Info-File.txt",
         "/home/enrico/Desktop/Snakemake/Report.ods"


rule GENEID:
    input:
        "/home/enrico/Desktop/Snakemake/RNA-Seq-counts.txt"
    output:
        temp("/home/enrico/Desktop/Snakemake/GeneIDList.txt")
    script:
        "/home/enrico/Desktop/GENEID.py"


rule biopython:
    input:
        "/home/enrico/Desktop/Snakemake/GeneIDList.txt"
    output:
        temp("/home/enrico/Desktop/Snakemake/allSequence_GCcontent.fasta")
    script:
        "/home/enrico/Desktop/Sequentie_GCpercentage.py"

rule KEGG:
    input:
        "/home/enrico/Desktop/Snakemake/RNA-Seq-counts.txt"
    output:
        temp("/home/enrico/Desktop/Snakemake/Kegg.txt")
    script:
        "/home/enrico/Desktop/KEGG.py"

rule BLAST:
    input:
        "/home/enrico/Desktop/Snakemake/allSequence_GCcontent.fasta"
    output:
        temp("/home/enrico/Desktop/Snakemake/Blast.txt")
    script:
        "/home/enrico/Desktop/Blast.py"

rule FindPubmedIDs:
    input:
        "/home/enrico/Desktop/Snakemake/allSequence_GCcontent.fasta",
        "/home/enrico/Desktop/Snakemake/GeneIDList.txt"
    output:
        temp("/home/enrico/Desktop/Snakemake/PubmedIDs.txt")
    script:
        "/home/enrico/Desktop/FindPubmedIDs.py"

rule MergeID:
    input:
        "/home/enrico/Desktop/Snakemake/GeneIDList.txt",
        "/home/enrico/Desktop/Snakemake/RNA-Seq-counts.txt"
    output:
        temp("/home/enrico/Desktop/Snakemake/MergedFile.txt")
    script:
        "/home/enrico/Desktop/MergeID.py"

rule MergeInfo:
    input:
        "/home/enrico/Desktop/Snakemake/MergedFile.txt",
        "/home/enrico/Desktop/Snakemake/Kegg.txt",
        "/home/enrico/Desktop/Snakemake/PubmedIDs.txt"
    output:
        temp("/home/enrico/Desktop/Snakemake/InfoFile.txt")
    script:
        "/home/enrico/Desktop/MergeInfo.py"

rule AddSeq:
    input:
        "/home/enrico/Desktop/Snakemake/InfoFile.txt",
        "/home/enrico/Desktop/Snakemake/allSequence_GCcontent.fasta"
    output:
        temp("/home/enrico/Desktop/Snakemake/InfoOutFile.txt"),
        temp("/home/enrico/Desktop/Snakemake/Info-File.txt")
    script:
        "/home/enrico/Desktop/addSeq.py"

rule MergeBlast:
    input:
        "/home/enrico/Desktop/Snakemake/Blast.txt",
        "/home/enrico/Desktop/Snakemake/Info-File.txt"
    output:
        "/home/enrico/Desktop/Snakemake/Report.ods"
    script:
        "/home/enrico/Desktop/MergeBlast.py"

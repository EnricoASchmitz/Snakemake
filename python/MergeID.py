GeneID = open("/home/enrico/Desktop/Snakemake/GeneIDList.txt", "r")
LpID = open("/home/enrico/Desktop/Snakemake/RNA-Seq-counts.txt", "r", encoding="latin-1")
Mergefile = open("/home/enrico/Desktop/Snakemake/MergedFile.txt","w")
LpID.readline()
Mergefile.write("geneid\t" + LpID.readline().strip().split("\t")[0] + "\n")
for line in GeneID:
    Mergefile.write(line.rstrip() + "\t" + LpID.readline().strip().split("\t")[0] + "\n")

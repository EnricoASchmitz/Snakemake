

def main():
    Mergefile = open("/home/enrico/Desktop/Snakemake/MergedFile.txt","r")
    Infofile = open("/home/enrico/Desktop/Snakemake/InfoFile.txt","w")
    Merge(Mergefile, Infofile)

def Merge(Mergefile, Infofile):
    KeggFile = open("/home/enrico/Desktop/Snakemake/Kegg.txt", 'r')
    PubFile = open("/home/enrico/Desktop/Snakemake/PubmedIDs.txt", 'r')
    PubFile.readline()
    Infofile.write(Mergefile.readline().strip() + "\t" + "Kegg" + "\t" + "Pubmed" +  "\n")
    try:
        for line in KeggFile:
            Infofile.write(Mergefile.readline().strip() + "\t" + line.rstrip().split("\t")[1] + "\t" + PubFile.readline().strip().split("\t")[1] +  "\n")
    except IndexError:
        pass

main()

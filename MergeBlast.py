def main():
    DictBlast = GetBlast()
    Merge(DictBlast)

def GetBlast():
    Blast = open("/home/enrico/Desktop/Snakemake/Blast.txt", "r")
    DictBlast = {}
    for line in Blast:
        if line.startswith(">"):
            ID = line.strip().split(">")[1]
        elif line == "\n":
            pass
        else:
            BlastRes = line.strip()
            # print("Regel\n" + BlastRes)
            if ID in DictBlast:
                BlastExtra = str(DictBlast.get(ID)) + BlastRes
                DictBlast.update({ID: BlastExtra})
            else:
                DictBlast.update({ID: BlastRes})
    return DictBlast

def Merge(DictBlast):
    InfoFile = open("/home/enrico/Desktop/Snakemake/Info-File.txt", "r")
    ReportFile = open("/home/enrico/Desktop/Snakemake/Report.ods", "w")
    ReportFile.write(InfoFile.readline().strip() + "\t" + "BLAST" + "\n")
    for line in InfoFile:
        ReportFile.write(line.strip() + "\t" + DictBlast.get(str(line.split("\t")[7].strip())) + "\n")

main()

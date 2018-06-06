
def main():
    global GC, IDList
    GC = []
    IDList = []
    gennaam = opengennaam()
    sequentie = opensequentie()
    insertinfo(gennaam, sequentie)
    insertGC()

def opengennaam():
    file = open("/home/enrico/Desktop/Snakemake/allSequence_GCcontent.fasta", "r")
    eiwitlist = ["Name"]

    for line in file:
        if ">" in line and "%" not in line:
            eiwit = line.split("[")[0].strip()
            if "," in line:
                eiwit = eiwit.split(",")[0].strip()
            ID = eiwit.split(" ")[0].split(">")[1]
            eiwit = eiwit.split(" ")[1:]
            IDList.append(ID)
            eiwitstring= " ".join(eiwit)
            eiwitlist.append(eiwitstring)
    return eiwitlist

def opensequentie():
    file = open("/home/enrico/Desktop/Snakemake/allSequence_GCcontent.fasta", "r")
    seq = ""
    alleseq = ["Sequentie"]
    for line in file:
        if line != "\n":
            if ">" not in line:
                if ";" in line:
                    GC.append(line.split(":")[1])
                else:
                    line = line.strip()
                    seq += line
        if line == "\n":
            alleseq.append(seq)
            seq = ""
    return  alleseq



def insertinfo(gennaam, sequentie):
    infile = open("/home/enrico/Desktop/Snakemake/InfoFile.txt","r")
    outfile = open("/home/enrico/Desktop/Snakemake/InfoOutFile.txt",'w')

    rows = [line.split('\t') for line in infile]
    cols = zip(*rows) # transposes 2Dlist
    cols = list(cols)

    cols.insert(2, gennaam)
    cols.insert(4, sequentie)
    rows = zip(*cols) # transpose back
    outfile.writelines(['\t'.join(row) for row in rows])
    infile.close()
    outfile.close()


def insertGC():
    outfile = open("/home/enrico/Desktop/Snakemake/Info-File.txt","w")
    infile = open("/home/enrico/Desktop/Snakemake/InfoOutFile.txt",'r')
    outfile.write(infile.readline().strip() + "\t" + "GCPer" + "\t" + "FastaID" + "\n")
    count = 0
    for line in infile:
        outfile.write(line.rstrip() + "\t" + GC[count].strip() + "\t" + IDList[count].strip() + "\n")
        count += 1
    infile.close()
    outfile.close()



main()

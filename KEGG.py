# extract all relations from all pathways
from bioservices.kegg import KEGG
kegg = KEGG()
output = open("/home/enrico/Desktop/Snakemake/Kegg.txt", 'w')
input = open("/home/enrico/Desktop/Snakemake/RNA-Seq-counts.txt", "r" ,encoding="latin-1")
line = input.readline().strip()
Header = input.readline().strip()
try:
    while line:
        line = input.readline().strip()
        ID, WCFS1_glc_1, WCFS1_glc_2, WCFS1_rib_1, WCFS1_rib_2, NC8_glc_1, NC8_glc_2, NC8_rib_1, NC8_rib_2 = line.strip().split("\t")
        res = str(kegg.get_pathway_by_gene(ID, "lpl")).strip('[]')
        if res != "None":
            output.write(ID + "\t" + res + "\n")
except:
    pass


input.close()
output.close()


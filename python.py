#import the library used to query a website
#import urllib2

#specify the url
Convert = "http://rest.kegg.jp/conv/ncbi-geneid/lpl:"

#Query the website and return the html to the variable 'page'


#import the Beautiful soup functions to parse the data returned from the website
#from bs4 import BeautifulSoup

#Parse the html in the 'page' variable, and store it in Beautiful Soup format

output = open("/home/enrico/Desktop/Snakemake/RNA-Seq-counts(1).txt", 'a')
input = open("/home/enrico/Desktop/Snakemake/RNA-Seq-counts.txt", "r" ,encoding="latin-1")
# # remove whitespace characters like `\n` at the end of each line
# content = [x.strip() for x in content]
line = input.readline()
Header = input.readline()
# use the read line to read further.
# If the file is not empty keep reading one line
# at a time, till the file is empty
count = 0
Locus_tags = []
try:
    while line:

        line = input.readline()
        print(line)
        # use realine() to read next line
        ID, WCFS1_glc_1, WCFS1_glc_2, WCFS1_rib_1, WCFS1_rib_2, NC8_glc_1, NC8_glc_2, NC8_rib_1, NC8_rib_2 = line.strip().split("\t")
        output.write(line)
        Locus_tags.append(ID)


        count += 1
except:
    pass
#Convert.append("+".join(Locus_tags))
#page = urllib2.urlopen(Convert)
#soup = BeautifulSoup(page)
#print(Convert)
input.close()
output.close()

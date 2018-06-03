rule GENEID:
    input:
        "/home/enrico/Desktop/Snakemake/RNA-Seq-counts.txt"
    output:
        "/home/enrico/Desktop/Snakemake/GeneIDList.txt"
    run:
        import urllib3
        import re
        Convert = "http://rest.kegg.jp/conv/ncbi-geneid/"
        output = open("/home/enrico/Desktop/Snakemake/GeneIDList.txt", 'w')
        input = open("/home/enrico/Desktop/Snakemake/RNA-Seq-counts.txt", "r" ,encoding="latin-1")
        line = input.readline().strip()
        Header = input.readline().strip()
        count = 0
        Locus_tags = []
        try:
            while line:
                line = input.readline().strip()
                ID, WCFS1_glc_1, WCFS1_glc_2, WCFS1_rib_1, WCFS1_rib_2, NC8_glc_1, NC8_glc_2, NC8_rib_1, NC8_rib_2 = line.strip().split("\t")
                Locus_tags.append("lpl:"+ID)
                count += 1
        except:
            pass

        http = urllib3.PoolManager()
        n = 200
        for i in range(0, len(Locus_tags), n):
                CURL = Convert + str("+".join(Locus_tags[i:i + n]))
                r = http.request('GET', CURL)
                GENEID = str(r.data)
                p = re.compile("geneid:[0-9]*")
                GENEID = p.findall(GENEID)
                for i in range(len(GENEID)):
                    output.write(GENEID[i].split(":")[1] + "\n")
        input.close()
        output.close()

rule Bio-python:

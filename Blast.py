

from Bio.Blast import NCBIWWW

from Bio.Blast import NCBIXML

from Bio import SeqIO
Blast = open("//home//enrico//Desktop//Snakemake//Blast.txt", "w")
with open("//home//enrico//Desktop//Snakemake//allSequence_GCcontent.fasta", "rU") as handle:
    try:
        for record in SeqIO.parse(handle, "fasta"):
            Blast.write(">" + record.id + "\n")
            sequence = record.seq
            result_handle = NCBIWWW.qblast("blastn","nr",sequence)
            blast_records = NCBIXML.parse(result_handle)
            blast_record = next(blast_records)
            E_VALUE_THRESH = 0.05
            for alignment in blast_record.alignments:
                for hsp in alignment.hsps:
                    if hsp.expect < E_VALUE_THRESH:
                        Blast.write('sequence:'+ alignment.title)
                        Blast.write('length:'+ str(alignment.length))
                        Blast.write('e value:'+ str(hsp.expect))
                        Blast.write("\n")
            Blast.write("\n")
    except ValueError:
        pass

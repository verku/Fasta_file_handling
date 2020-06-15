#!/usr/bin/python3

# Removes trailing "Ns" from the end of scaffolds. Accepts stretches of N plus one base.
# Requires BioPython
# Run by typing: python3 removeNs.py in.fasta out.fasta


import sys
import re
from Bio import SeqIO
from Bio.Seq import Seq


out_sequences = []

for record in SeqIO.parse(sys.argv[1], "fasta"):
    record.seq = Seq(re.sub(r"[nN]+[AaCcTtGgNn]$", '', str(record.seq)))
    out_sequences.append(record)

SeqIO.write(out_sequences, sys.argv[2], "fasta")

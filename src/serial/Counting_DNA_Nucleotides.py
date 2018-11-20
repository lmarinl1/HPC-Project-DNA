#! usr/bin/python3
fasta = open('../../data/Escherichia_coli_4_1_47FAA_uid39385/codigo1.fna','r')
a = 0
c = 0
g = 0
t = 0
n = 0

for line in fasta:
    if line[0] == '>': continue 
    for nucleotido in line:
        if nucleotido == 'A': a+=1
        elif nucleotido == 'C': c+=1
        elif nucleotido == 'G': g+=1
        elif nucleotido == 'T': t+=1
        else: n+=1
 
print("A =",a)
print("C =",c)
print("G =",g)
print("T =",t)
print("No reconocido =",n)
fasta.close()

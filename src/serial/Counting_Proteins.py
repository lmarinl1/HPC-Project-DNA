
import sys
from os import listdir 
from os.path import isfile, join
from datetime import datetime

# Map declaration this will list all the amino acids with their respective codon
m = {'GCT':'A','GCC':'A','GCA':'A','GCG':'A','CGT':'R','CGC':'R','CGA':'R','CGG':'R','AGA':'R','AGG':'R','AAT':'N','AAC':'N','GAT':'D','GAC':'D','TGT':'C','TGC':'C','CAA':'Q','CAG':'Q','GAA':'E','GAG':'E','GGT':'G','GGC':'G','GGA':'G','GGG':'G','CAT':'H','CAC':'H','ATT':'I','ATC':'I','ATA':'I','ATG':'1','TTA':'L','TTG':'L','CTT':'L','CTC':'L','CTA':'L','CTG':'L','AAA':'K','AAG':'K','ATG':'M','TTT':'F','TTC':'F','CCT':'P','CCC':'P','CCA':'P','CCG':'P','TCT':'S','TCC':'S','TCA':'S','TCG':'S','AGT':'S','AGC':'S','ACT':'T','ACC':'T','ACA':'T','ACG':'T','TGG':'W','TAT':'Y','TAC':'Y','GTT':'V','GTC':'V','GTA':'V','GTG':'V','TAA':'0','TGA':'0','TAG':'0'}
n = {'A':0,'R':0,'N':0,'D':0,'C':0,'Q':0,'E':0,'G':0,'H':0,'I':0,'1':0,'L':0,'K':0,'M':0,'F':0,'P':0,'S':0,'T':0,'W':0,'Y':0,'V':0,'0':0,'X':0 }

#This method returns the amino acid that belongs to a codon, if the codon is not identified it will return an X
def getCodon(tri):
    if m.has_key(tri):
        a = m[tri]
        n[a] += 1 
        return a
    else:
        n['X'] += 1
        return 'X'
    
# Method that will count how many amino acid are
def countNucleotides(folderName):
    """ Print the nucleotides count (A: Adenine, C: Citocine, G: Guanine, T: Timminine) and (N: not identified) """
    archivosFna = [filefna for filefna in listdir(folderName) if filefna[-3:] == ".fa"]
    if len(archivosFna) == 0: 
        print(" The Folder given has not fasta files ")
        return
    # Date time 
    instanteinicial = datetime.now()

    for filefna in archivosFna:
        filePath = folderName+'/'+filefna
        print " --- Analyzing "+filefna+" ------------ "+str((datetime.now()-instanteinicial).seconds)+" sec"
        
        fasta = open(filePath,'r')
        rfasta = open('results/'+filefna+".proteins",'w')
        fastaR = ""
        for line in fasta:
            rline = ''
            if line[0] == '>': continue
            i = 0
            while i < len(line[:-2]):
                rline += getCodon(line[i]+line[i+1]+line[i+2])
                i+=3
            fastaR += (rline+'\n')    
        rfasta.write(fastaR)
        rfasta.close()
        fasta.close()
        print " --- Generated "+filefna+".proteins --- "+str((datetime.now()-instanteinicial).seconds)+" sec"
        
# This method will print the countingof the amino acids
def printCounting():
    print 'Results ----------------------------------------------------------------------------------------'
    for i in n:
        print "> "+i+": "+str(n[i])

def main():
    if len(sys.argv) != 2:
        raise Exception('Usage python Counting_DNA_Nucleotides.py  <FolderName>')
    
    if not isfile(join(sys.argv[1])):
        countNucleotides(sys.argv[1])
        printCounting()
    else: 
        raise Exception('<FolderName> must be a Folder')


if __name__=='__main__':
    try:
        main()
    except ValueError as e:
        print "*** Error in Args ***" 


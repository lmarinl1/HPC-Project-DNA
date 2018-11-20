
import sys
from os import listdir 
from os.path import isfile, join

def countNucleotides(folderName):
    archivosFna = [filefna for filefna in listdir(folderName) if filefna[-4:] == ".fna"]
    a = 0
    c = 0
    g = 0
    t = 0
    n = 0
    
    for filefna in archivosFna:
        filePath = folderName+'/'+filefna
        print " --- Analyzing "+filefna+" --- "
        fasta = open(filePath,'r')
        for line in fasta:
            if line[0] == '>': continue 
            for nucleotido in line:
                if nucleotido == 'A': a+=1
                elif nucleotido == 'C': c+=1
                elif nucleotido == 'G': g+=1
                elif nucleotido == 'T': t+=1
                else: n+=1
        fasta.close()

    print "A =",a
    print "C =",c
    print "G =",g
    print "T =",t
    print "No reconocido =",n

def main():
    if len(sys.argv) != 2:
        raise Exception('Usage python Counting_DNA_Nucleotides.py  <FolderName>')
    
    if not isfile(join(sys.argv[1])):
        countNucleotides(sys.argv[1])
    else: 
        raise Exception('<FolderName> must be a Folder')


if __name__=='__main__':
    try:
        main()
    except ValueError as e:
        print("*** Error in Args ***")


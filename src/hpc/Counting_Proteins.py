import sys
from os import listdir 
from os.path import isfile, join
from datetime import datetime
from mpi4py import MPI 

# Map declaration
m = {'GCT':'A','GCC':'A','GCA':'A','GCG':'A','CGT':'R','CGC':'R','CGA':'R','CGG':'R','AGA':'R','AGG':'R','AAT':'N','AAC':'N','GAT':'D','GAC':'D','TGT':'C','TGC':'C','CAA':'Q','CAG':'Q','GAA':'E','GAG':'E','GGT':'G','GGC':'G','GGA':'G','GGG':'G','CAT':'H','CAC':'H','ATT':'I','ATC':'I','ATA':'I','ATG':'1','TTA':'L','TTG':'L','CTT':'L','CTC':'L','CTA':'L','CTG':'L','AAA':'K','AAG':'K','ATG':'M','TTT':'F','TTC':'F','CCT':'P','CCC':'P','CCA':'P','CCG':'P','TCT':'S','TCC':'S','TCA':'S','TCG':'S','AGT':'S','AGC':'S','ACT':'T','ACC':'T','ACA':'T','ACG':'T','TGG':'W','TAT':'Y','TAC':'Y','GTT':'V','GTC':'V','GTA':'V','GTG':'V','TAA':'0','TGA':'0','TAG':'0'}
#n = {'A':0,'R':0,'N':0,'D':0,'C':0,'Q':0,'E':0,'G':0,'H':0,'I':0,'1':0,'L':0,'K':0,'M':0,'F':0,'P':0,'S':0,'T':0,'W':0,'Y':0,'V':0,'0':0,'X':0 }


def getCodon(tri, n):
    if tri in m:
        a = m[tri]
        n[a] += 1 
        return a
    else:
        n['X'] += 1
        return 'X'

def reviewFile(folderName, filefna, n):
    # Date time 
    instanteinicial = datetime.now()
    filePath = folderName+'/'+filefna
    print(" --- Analyzing "+filefna+" ------------ "+str((datetime.now()-instanteinicial).seconds)+" sec")
    sys.stdout.flush()
    fasta = open(filePath,'r')
    rfasta = open('/opt/dna/proteins/'+filefna+".proteins",'w')
    fastaR = ""
    for line in fasta:
        rline = ''
        if line[0] == '>': continue
        i = 0
        while i < len(line[:-2]):
            rline += getCodon(line[i]+line[i+1]+line[i+2], n)
            i+=3
        fastaR += (rline+'\n')    
    rfasta.write(fastaR)
    rfasta.close()
    fasta.close()
    print(" --- Generated "+filefna+".proteins --- "+str((datetime.now()-instanteinicial).seconds)+" sec")
    sys.stdout.flush()
    
def printCounting(n):
    print('Results ----------------------------------------------------------------------------------------')
    for i in n:
        print("> "+i+": "+str(n[i]))
    sys.stdout.flush()
        

def countNucleotides(folderName):
    """ Print the nucleotides count (A: Adenine, C: Citocine, G: Guanine, T: Timminine) and (N: not identified) """
    archivosFna = [filefna for filefna in listdir(folderName) if filefna[-3:] == ".fa"]
    if len(archivosFna) == 0: 
        print(" The Folder given has not fasta files ")
        return

    n = {'A':0,'R':0,'N':0,'D':0,'C':0,'Q':0,'E':0,'G':0,'H':0,'I':0,'1':0,'L':0,'K':0,'M':0,'F':0,'P':0,'S':0,'T':0,'W':0,'Y':0,'V':0,'0':0,'X':0 }
    
    #Rank
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    if comm.rank == 0:
        reviewFile(folderName, archivosFna[0], n)
        comm.send(n,dest=3)
    elif comm.rank == 1:
        reviewFile(folderName, archivosFna[1], n)
        #k = n
        comm.send(n,dest=3)
    elif comm.rank == 2:
        reviewFile(folderName, archivosFna[2], n)
        #k = n
        comm.send(n,dest=3)
    else:
        for i in range(3):
            data = comm.recv(source=MPI.ANY_SOURCE)
            for key, value in data.items():
                n[key] += value
        printCounting(n)
        
    
    
def main():
    if len(sys.argv) != 2:
        raise Exception('Usage python Counting_DNA_Nucleotides.py  <FolderName>')
    
    if not isfile(join(sys.argv[1])):
        countNucleotides(sys.argv[1])
        #printCounting()
    else: 
        raise Exception('<FolderName> must be a Folder')


print(MPI.Get_processor_name())
if __name__=='__main__':
    try:
        main()
    except ValueError as e:
        print("*** Error in Args ***") 


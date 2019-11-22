import random
import sys
from Bio import SeqIO


for seq_record1 in SeqIO.parse("liver.fasta", "fasta"):
	chromosome1 = seq_record1.seq
	
for seq_record2 in SeqIO.parse("brain.fasta", "fasta"):
	chromosome2 = seq_record2.seq

chromosome1 = len(seq_record1)
chromosome2 = len(seq_record2)

print chromosome1, chromosome2

player = 0

while player!=-1:
        print ("Ta xromosomata  einai \n 1. chromosome1 = ", chromosome1, "\n 2. chromosome2= ", chromosome2)
        if player==0 and not(chromosome1 ==0 and chromosome2 == 0):
                print ("Paizei o 1os paixtis \n")
                if chromosome1 != 0 and chromosome2 != 0:
                        print ("thes na diagrapseis apo tin 1i, tin 2i i kai apo tis 2 allilouxies? apanta 1, 2 i 3")
                        choice = input()
                        while choice != 1 and choice != 2 and choice != 3:
                                        print ("Lathos eisodos.Dialekse metaksu tou 1, 2 i 3")
                                        choice = int(input())
                        print ("dialekse arithmo gia na ton diagrapseis apo tin/tis allilouxies pou dialekses")
                        if choice ==1:
                                choice1 = input()
                                while choice1 <= 0 and choice1 > chromosome1 :
                                        print ("arithmos mi arnitikos i 0 kai mikroteros i isos tou mikous tis allilouxias")
                                        choice1 = int(input())
                                chromosome1 = chromosome1 - choice1
                        elif choice ==2:
                                choice1 = input()
                                while choice1 <= 0 and choice1 > chromosome2 :
                                        print ("arithmos mi arnitikos i 0 kai mikroteros i isos tou mikous tis allilouxias")
                                        choice1 = int(input())
                                chromosome2 = chromosome2 - choice1
                        elif choice ==3 and chromosome1 <= chromosome2:
                                choice1 = int(input())
                                while choice1 <= 0 and choice1 > chromosome1 :
                                        print ("arithmos mi arnitikos i 0 kai mikroteros i isos tou mikous tis allilouxias")
                                        choice1 = input()
                                chromosome1 = chromosome1 - choice1
                                chromosome2 = chromosome2 - choice1
                        elif choice ==3 and chromosome2 < chromosome1:
                                choice1 = int(input())
                                while choice1 <= 0 and choice1 > chromosome2 :
                                        print ("arithmos mi arnitikos i 0 kai mikroteros i isos tou mikous tis allilouxias")
                                        choice1 = int(input())
                                chromosome1 = chromosome1 - choice1
                                chromosome2 = chromosome2 - choice1
                                
                elif chromosome1 !=0 and chromosome2 == 0 :
                        print ("dialekse arithmo gia na aferaiseis apo tin 1i allilouxia")
                        choice = int(input())
                        while choice <=0 and choice > chromosome1:
                                        print ("Lathos eisodos.Dialekse arithmo mi arnitiko i 0 kai mikrotero i iso tou mikous tis allilouxias")
                                        choice = int(input())
                        chromosome1 = chromosome1 - choice
                        
                elif chromosome1 ==0 and chromosome2 !=0:
                        print ("dialekse arithmo gia na aferaiseis apo tin 2i allilouxia")
                        choice = int(input())
                        while choice <=0 and choice > chromosome2:
                                        print ("Lathos eisodos.Dialekse arithmo mi arnitiko i 0 kai mikrotero i iso tou mikous tis allilouxias")
                                        choice = int(input())
                        chromosome2 = chromosome2 - choice
                                
                player = 1              
        elif player ==1 and  not(chromosome1 ==0 and chromosome2 == 0):
                print ("Paizei o 2os paixtis \n") 
                if chromosome1 != 0 and chromosome2 != 0:
                        print ("thes na diagrapseis apo tin 1i, tin 2i i kai apo tis 2 allilouxies? apanta 1, 2 i 3")
                        choice = input()
                        while choice != 1 and choice != 2 and choice != 3:
                                        print ("Lathos eisodos.Dialekse metaksu tou 1, 2 i 3")
                                        choice = int(input())
                        print ("dialekse arithmo gia na ton diagrapseis apo tin/tis allilouxies pou dialekses")
                        if choice ==1:
                                choice1 = input()
                                while choice1 <= 0 and choice1 > chromosome1 :
                                        print ("arithmos mi arnitikos i 0 kai mikroteros i isos tou mikous tis allilouxias")
                                        choice1 = int(input())
                                chromosome1 = chromosome1 - choice1
                        elif choice ==2:
                                choice1 = input()
                                while choice1 <= 0 and choice1 > chromosome2 :
                                        print ("arithmos mi arnitikos i 0 kai mikroteros i isos tou mikous tis allilouxias")
                                        choice1 = int(input())
                                chromosome2 = chromosome2 - choice1
                        elif choice ==3 and chromosome1 <= chromosome2:
                                choice1 = int(input())
                                while choice1 <= 0 and choice1 > chromosome1 :
                                        print ("arithmos mi arnitikos i 0 kai mikroteros i isos tou mikous tis allilouxias")
                                        choice1 = input()
                                chromosome1 = chromosome1 - choice1
                                chromosome2 = chromosome2 - choice1
                        elif choice ==3 and chromosome2 < chromosome1:
                                choice1 = int(input())
                                while choice1 <= 0 and choice1 > chromosome2 :
                                        print ("arithmos mi arnitikos i 0 kai mikroteros i isos tou mikous tis allilouxias")
                                        choice1 = int(input())
                                chromosome1 = chromosome1 - choice1
                                chromosome2 = chromosome2 - choice1
                                
                elif chromosome1 !=0 and chromosome2 == 0 :
                        print ("dialekse arithmo gia na aferaiseis apo tin 1i allilouxia")
                        choice = int(input())
                        while choice <=0 and choice > chromosome1:
                                        print ("Lathos eisodos.Dialekse arithmo mi arnitiko i 0 kai mikrotero i iso tou mikous tis allilouxias")
                                        choice = int(input())
                        chromosome1 = chromosome1 - choice
                        
                elif chromosome1 ==0 and chromosome2 !=0:
                        print ("dialekse arithmo gia na aferaiseis apo tin 2i allilouxia")
                        choice = int(input())
                        while choice <=0 and choice > chromosome2:
                                        print ("Lathos eisodos.Dialekse arithmo mi arnitiko i 0 kai mikrotero i iso tou mikous tis allilouxias")
                                        choice = int(input())
                        chromosome2 = chromosome2 - choice
                
                player = 0
                        
        elif chromosome1 ==0 and chromosome2 == 0:
                if player==0:
                        print ("o paixtis 2 nikise") 
                elif player==1:
                        print ("o paixtis 1 nikise")
                player = -1
                        
                        
                        


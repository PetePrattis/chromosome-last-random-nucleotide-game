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
        print ("The chromosomes are \n 1. chromosome1 = ", chromosome1, "\n 2. chromosome2= ", chromosome2)
        if player==0 and not(chromosome1 ==0 and chromosome2 == 0):
                print ("Player 1's round  \n")
                if chromosome1 != 0 and chromosome2 != 0:
                        print ("Do you want to delete from 1st, 2nd or both sequences? Answer with 1, 2 or 3")
                        choice = input()
                        while choice != 1 and choice != 2 and choice != 3:
                                        print ("Wrong input! Answer with 1, 2 or 3")
                                        choice = int(input())
                        print ("Pick a number to delete it from the sequence or sequences you picked")
                        if choice ==1:
                                choice1 = input()
                                while choice1 <= 0 and choice1 > chromosome1 :
                                        print ("Number can't be negative or smaller or equall to the length of the sequence")
                                        choice1 = int(input())
                                chromosome1 = chromosome1 - choice1
                        elif choice ==2:
                                choice1 = input()
                                while choice1 <= 0 and choice1 > chromosome2 :
                                        print ("Number can't be negative or smaller or equall to the length of the sequence")
                                        choice1 = int(input())
                                chromosome2 = chromosome2 - choice1
                        elif choice ==3 and chromosome1 <= chromosome2:
                                choice1 = int(input())
                                while choice1 <= 0 and choice1 > chromosome1 :
                                        print ("Number can't be negative or smaller or equall to the length of the sequence")
                                        choice1 = input()
                                chromosome1 = chromosome1 - choice1
                                chromosome2 = chromosome2 - choice1
                        elif choice ==3 and chromosome2 < chromosome1:
                                choice1 = int(input())
                                while choice1 <= 0 and choice1 > chromosome2 :
                                        print ("Number can't be negative or smaller or equall to the length of the sequence")
                                        choice1 = int(input())
                                chromosome1 = chromosome1 - choice1
                                chromosome2 = chromosome2 - choice1
                                
                elif chromosome1 !=0 and chromosome2 == 0 :
                        print ("Pick a number to deduct from the first sequence")
                        choice = int(input())
                        while choice <=0 and choice > chromosome1:
                                        print ("Wrong input! Number can't be negative or smaller or equall to the length of the sequence")
                                        choice = int(input())
                        chromosome1 = chromosome1 - choice
                        
                elif chromosome1 ==0 and chromosome2 !=0:
                        print ("Pick a number to deduct from the second sequence")
                        choice = int(input())
                        while choice <=0 and choice > chromosome2:
                                        print ("Wrong input! Number can't be negative or smaller or equall to the length of the sequence")
                                        choice = int(input())
                        chromosome2 = chromosome2 - choice
                                
                player = 1              
        elif player ==1 and  not(chromosome1 ==0 and chromosome2 == 0):
                print ("Player 2's round \n") 
                if chromosome1 != 0 and chromosome2 != 0:
                        print ("Do you want to delete from 1st, 2nd or both sequences? Answer with 1, 2 or 3")
                        choice = input()
                        while choice != 1 and choice != 2 and choice != 3:
                                        print ("Wrong input! Answer with 1, 2 or 3")
                                        choice = int(input())
                        print ("Pick a number to delete it from the sequence or sequences you picked")
                        if choice ==1:
                                choice1 = input()
                                while choice1 <= 0 and choice1 > chromosome1 :
                                        print ("Number can't be negative or smaller or equall to the length of the sequence")
                                        choice1 = int(input())
                                chromosome1 = chromosome1 - choice1
                        elif choice ==2:
                                choice1 = input()
                                while choice1 <= 0 and choice1 > chromosome2 :
                                        print ("Number can't be negative or smaller or equall to the length of the sequence")
                                        choice1 = int(input())
                                chromosome2 = chromosome2 - choice1
                        elif choice ==3 and chromosome1 <= chromosome2:
                                choice1 = int(input())
                                while choice1 <= 0 and choice1 > chromosome1 :
                                        print ("Number can't be negative or smaller or equall to the length of the sequence")
                                        choice1 = input()
                                chromosome1 = chromosome1 - choice1
                                chromosome2 = chromosome2 - choice1
                        elif choice ==3 and chromosome2 < chromosome1:
                                choice1 = int(input())
                                while choice1 <= 0 and choice1 > chromosome2 :
                                        print ("Number can't be negative or smaller or equall to the length of the sequence")
                                        choice1 = int(input())
                                chromosome1 = chromosome1 - choice1
                                chromosome2 = chromosome2 - choice1
                                
                elif chromosome1 !=0 and chromosome2 == 0 :
                        print ("Pick a number to deduct from the first sequence")
                        choice = int(input())
                        while choice <=0 and choice > chromosome1:
                                        print ("Wrong input! Number can't be negative or smaller or equall to the length of the sequence")
                                        choice = int(input())
                        chromosome1 = chromosome1 - choice
                        
                elif chromosome1 ==0 and chromosome2 !=0:
                        print ("Pick a number to deduct from the second sequence")
                        choice = int(input())
                        while choice <=0 and choice > chromosome2:
                                        print ("Wrong input! Number can't be negative or smaller or equall to the length of the sequence")
                                        choice = int(input())
                        chromosome2 = chromosome2 - choice
                
                player = 0
                        
        elif chromosome1 ==0 and chromosome2 == 0:
                if player==0:
                        print ("Player 2 won") 
                elif player==1:
                        print ("Player 1 won")
                player = -1
                        
                        
                        


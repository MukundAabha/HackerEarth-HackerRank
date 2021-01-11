# -*- coding: utf-8 -*-
"""
Jadoo, the Space Alien has befriended Koba upon landing on Earth. Since then, he wishes Koba to be more like him. In order to do so he decides to slowly transcribe Koba's DNA into RNA. But he has to write a very short code in order to do the transcription so as not to make Koba aware of the change.

The four nucleotides found in DNA are adenine (A), cytosine (C), guanine (G) and thymine (T).

The four nucleotides found in RNA are adenine (A), cytosine (C), guanine (G) and uracil (U).

Given a DNA strand, its transcribed RNA strand is formed by replacing each nucleotide with its complement:

G --> C
C --> G
T --> A
A --> U
 

Input: The input will always be a string of characters.
"""

# define a function for transcription 
def transcript(x) : 
	
# convert string into list 
    l = list(x) 

    for i in range(len(x)):
        if(l[i]=='G'):
            l[i]='C'
        elif(l[i]=='C'):
            l[i]='G'
        elif(l[i]=='T'):
            l[i]=='A'
        elif(l[i]=='A'):
            l[i]='U' 
        else: 
            print('Invalid Input')

    print(end="")
		    					 	 
    for char in l: 
	    print(char,end="") 

# Driver code 
#if __name__ == "__main__": 
	
x = input()
# function calling 
transcript(x) 

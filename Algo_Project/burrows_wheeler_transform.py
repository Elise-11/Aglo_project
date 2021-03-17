#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BWT script contains functions related to Burrows-Wheeler tranform
corresponding to a text pre-processing used in data compression
"""

from tkinter import filedialog, messagebox
import os
from pathlib import Path
    


def open_check_file():
    '''
    This functions opens an input file and retrieves its content
    in a variable named sequence.
    Then it checks that the sequence only contains letters from an alphabet
    here the alphabet contains only nucleotides (A,T,C,G)
    and a possible unidentified nucleotide N.

    Returns
    -------
    false : if the file is empty
    false : if the sequence contains another letter than ("ACGNT")
    sequence : sequence with a dollar added at the end
    '''
    #open a text file through a through a dialog window 
    file = filedialog.askopenfilename(title="Select a txt file",\
                                      filetypes=[("Text file", ".txt")])
    #check that the selected file is not empty 
    if os.stat(file).st_size != 0 :
        open_file = open(file, "r")
        sequence= ""
        
        for line in open_file :
            sequence += line
            sequence = sequence.strip("\n")
            valid = 'ACGNT'
            
            for letter in sequence.upper():
                if letter not in valid:
                    #if the letter is not in the alaphabet raise an error messsage
                    messagebox.showwarning("Error", "Your file not contain only DNA ")
                    return False
                
        #return the dna sequence with a $ added at its end and the file path
        return sequence.upper()+"$", file
        open_file.close()
    
    else :
        #if the file is empty raise an error message
        messagebox.showwarning("Error", "Your file is empty ")
        return False



def transform():
    """
    This function is the main function of the program
    it performs the Burrows-Wheeler transform.

    Returns
    -------
    sequence : the original sequence with a dollar added at the end
    bwt_pattern : bwt tranformed sequence
    file : file path
    seq_list : shifted_matrix
    """
    #retrieve the sequence and the file path
    sequence, file = open_check_file()

    #add each letter of the sequence in a list named nucleotides
    nucleotides = []
    for i in range(0, len(sequence),1):
        nucleotides.append(sequence[i])
        i+=1

    #construction of the shift matrix 
    seq_list = []
    for i in range(0,len(nucleotides),1):
        #shift with a step of 1
        word = sequence[-1] + sequence[:-1]
        new = ''.join(word)
        sequence = new
        #add the shifted sequence to the list 
        seq_list.append(new)
        i += 1

    #lexical sort of the matrix
    sort = sorted(seq_list)

    #retrieve in a new list the last letters of the list items
    bwt = []
    for i in range(len(nucleotides)):
        element = sort[i]
        #last letter of each words of the sorted list 
        last = element[- 1]
        i += 1
        #add in a list named bwt
        bwt.append(last)
        #join every items of the list to retrive bwt sequence in a single item
        bwt_pattern = "".join(bwt)
    
    return sequence, bwt_pattern, file, seq_list



def save_transform():
    """
    This function allows to save the result of Burrows_Wheeler transform
    in a new created text file ending with _bwt.txt

    Returns
    -------
    seq : the original sequence with a dollar added at the end
    bwt : bwt tranformed sequence
    """
    
    seq, bwt, file, seq_list = transform()
    
    #cut the file path by extension and retrieve the first part
    file_path = os.path.splitext(file)[0]
    
    #create a new file named with the file name of the file containing the original sequence
    #write the bwt sequence
    file = open(file_path+ "_bwt.txt", "w")
    file.write(bwt)
    file.close()

    messagebox.showinfo("Information", "Your bwt result has been saved in" \
                        +file_path+"_bwt.txt.")
    return seq, bwt

    

def bwt_inverse():
    '''
    This function performs the Burrows-Wheeler reconstruction
    from a bwt sequence in a text file, and print it in a new file

    Returns
    -------
    bwt : bwt sequence
    inverse_bwt : the original sequence
    '''

    file = filedialog.askopenfilename(title="Select a txt file" \
                                      ,filetypes=[("Text file", ".txt")])
    if os.stat(file).st_size != 0 :
        open_file = open(file, "r")
        bwt= ""
        
        #retrive the bwt sequence in bwt variable and delete "\n"
        for line in open_file :
            bwt += line
            bwt = bwt.strip("\n")
    
        #create an empty table according to the size of the bwt sequence
        table = [""] * len(bwt)
    
        #this loop adds each items of the sequence in a list 
        #perform a lexical sort of the list 
        #and adds again each items of the sequence in the sorted list before the items already in the list 
        for i in range(0,len(bwt),1):            
            table = [bwt[i] + table[i] for i in range(0,len(bwt),1)]
            table = sorted(table)

        
        #find the row ending in $ and save it in inverse_bwt variable 
        #inverse bwt corresponds to the original sequence
        for row in table : 
            if row.endswith("$"):
                inverse_bwt = row
        
        #cut the '$' from the reconstructed sequence
        inverse_bwt = inverse_bwt.rstrip("$")  
        
        open_file.close() 
        
        #write the original sequence in a new created file 
        file_path = os.path.splitext(file)[0]
        file_inv = open(file_path + "_inversion.txt", "w") 
        file_inv.write(inverse_bwt) 
        file_inv.close()
        
        messagebox.showinfo("Information", "Your bwt inversion has been saved in " \
                            +file_path +"_inversion.txt file.")
        return bwt,inverse_bwt
    
    else :
        messagebox.showwarning("Error", "Your file is empty")
        return False

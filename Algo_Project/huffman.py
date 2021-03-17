#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
huffman script contains functions related 
to the Huffman Compression
"""

from burrows_wheeler_transform import * 
import json

from tkinter import filedialog, messagebox
import os


class NodeTree():
    """
    A class corresponding to nodes of a huffman coding tree.
     
    Attributes
    ----------
    left : left child of a node
    right : right child of a node
        
    """
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)

    def nodes(self):
        return (self.left, self.right)

    def __str__(self):
        return '%s_%s' % (self.left, self.right)



# Main function implementing huffman coding
def huffman_code_tree(node, left=True, binString=''):
    """
    This functions determine the way of construction 
    for the Huffman tree, a path is created by a binary string, 
    it adds a 0 for a left child and a 1 for a right child. 
    the function saves the binary path in a dictionnary.

    Returns
    -------
    dico_binary : dictionnary containing binary path

    """
    if type(node) is str:
        return {node: binString}
    
    (l, r) = node.children()
    dico_binary = {}
    dico_binary.update(huffman_code_tree(l, True, binString + '0'))
    dico_binary.update(huffman_code_tree(r, False, binString + '1'))

    return dico_binary



def huffman_construction(seq) : 
    """
    This function calculate the frequency for each items of the sequence, 
    and build the tree according to these frequencies. 

    Parameters
    ----------
    seq : the sequence to be compressed 

    Returns
    -------
    huffman_code = the dictionnary containing binary coding 
    binary_seq = the binary sequence code 

    """
    # Calculating frequency
    freq = {}
    for c in seq:
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1

    freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    nodes = freq

    while len(nodes) > 1:
        (key1, c1) = nodes[-1]
        (key2, c2) = nodes[-2]
        nodes = nodes[:-2]
        node = NodeTree(key1, key2)
        nodes.append((node, c1 + c2))
        nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

    huffman_code = huffman_code_tree(nodes[0][0])

    #construction of the binary sequence code
    #for each items of the sequence we search the corresponding code 
    #in the dictionnary example : {"T":001}
    #and add the corresponding code in a list and join it 
    binary_list= []
    for element in seq:
        for key in huffman_code.keys():
            if element == key:
                binary_list += huffman_code[key]
                binary_seq ="".join(binary_list)

    return huffman_code, binary_seq


    
def binary_conversion(): 
    """
    This function allows to choose a file to be compressed, 
    retrieve the binary coding by adding a certain number of zeros so 
    that the binary sequence is coded on 8 bits.

    Returns
    -------
    added : the number of zeros added at the end of the binary sequence
    binary_seq : the resulting binary sequence
    seq : the sequence to be compressed
    file : file path of the file containing the sequence
    """
    file = filedialog.askopenfilename(title="Select a txt ",filetypes=[("Text file", ".txt")])
    if os.stat(file).st_size != 0:
        open_file = open(file, "r")
        seq = ""
        for line in open_file :
            seq += line
            seq = seq.strip("\n")
            
        huffman_code, binary_seq = huffman_construction(seq)
        #count the number of "0" added
        added = 0 
        while len(binary_seq) % 8 !=0:
            added +=1 
            binary_seq += '0'
        open_file.close()
        
    else :
        messagebox.showwarning("Error", "Your file is empty ")
    
    return added, binary_seq, seq, file



def binary_to_utf8(): 
    """
    This function convert binary string in utf-8 string, 
    that correspond to the compressed sequence

    Returns
    -------
    added : the number of zeros added at the end of the binary sequence
    comp_seq : the compressed sequence coded in utf-8
    binary_seq : the resulting binary sequence
    seq : the sequence to be compressed
    file : file path of the file containing the sequence
    """
    added, binary_seq, seq, file = binary_conversion()
    
    comp_seq = ""
    for bit in range(0, len(binary_seq), 8):
        #cut the sequence each 8 bits
        byte = binary_seq[bit:bit+8]
        code = int(byte, 2)
        #transforms 8 bits into a single character coded in utf-8
        comp_seq += chr(code)

    return added, comp_seq, binary_seq, seq, file



def save_compression(): 
    """
    This function allows to save the dictionnary and the compressed sequence 
    in a file ending with _compressed.txt

    Returns
    -------
    comp_seq : the compressed sequence 
    binary_seq : the sequence coded by a binary string 
    seq : the original sequencen not compressed
    """
    added,comp_seq, binary_seq, seq, file = binary_to_utf8()
    huffman_code, binary_seq = huffman_construction(seq)
    
    #save the number of zeroes added to the dictionnary 
    huffman_code["add"]= added
    created_file = os.path.splitext(file)[0]
    file_comp = open(created_file + "_compressed.txt", "w") 
    
    #save the dictionnary in the file and the compressed sequence
    json.dump(huffman_code, file_comp)
    file_comp.write("\n"+comp_seq) 
    file_comp.close()
    
    messagebox.showinfo("Information", "Your compression has been saved in "+created_file +"_compressed.txt file.")
    return comp_seq, binary_seq, seq



def bwt_binary_conversion():
    """
    This function allows to perform the bwt algorithm and a compression

    Returns
    -------
    seq : The original sequence
    binary_seq : the sequence coded by a binary string 
    comp_seq : the compressed sequence 
    """
    #call bwt function
    sequence,bwt_pattern, file, seq_list = transform()
    seq = bwt_pattern
    #retrieve the dictionnary containing binary code and the binary sequence
    huffman_code, binary_seq = huffman_construction(seq)
    
    #add zeroes
    added = 0 
    while len(binary_seq) % 8 !=0:
        added +=1 
        binary_seq += '0'
    
    #convert binary sequence in utf-8 sequence
    comp_seq = ""
    for bit in range(0, len(binary_seq), 8):
        byte = binary_seq[bit:bit+8]
        code = int(byte, 2)
        comp_seq += chr(code)
    
    #save the number of zeroes added 
    huffman_code["add"]= added
    
    #save the dictionnary in the file and the compressed sequence
    created_file = os.path.splitext(file)[0]
    file_comp = open(created_file + "_bwt_compressed.txt", "w") 
    json.dump(huffman_code, file_comp)
    file_comp.write("\n"+comp_seq) 
    
    file_comp.close()
    
    messagebox.showinfo("Information", "Your compression has been saved in "+created_file +"_bwt_compressed.txt file.")
    
    return seq, binary_seq, comp_seq



def read_compressed_file():
    """
    This function read the file containing the compressed sequence, 
    retrieve the dictionnary and the compressed sequence

    Returns
    -------
    dico_binary : the dictionnary containing binary coding 
    comp_seq : the compressed sequence
    file_comp : the path of the file 
    """
    file_comp = filedialog.askopenfilename(title="Select a txt ",filetypes=[("Text file", ".txt")])

    if os.stat(file_comp).st_size != 0:
        file = open(file_comp, "r")
        head = file.readline()
        dico_binary = json.loads(head)
        comp_seq = ""
        for line in file :
            comp_seq += line
    
        file.close()
        
    else :
        messagebox.showwarning("Error", "Your file is empty ")
        
    return dico_binary, comp_seq, file_comp



def utf8_to_binary() :
    """
    This function allows to convert utf-8 sequence in binary sequence

    Returns
    -------
    bin_seq : binary sequence
    dico_binary : the dictionnary containing binary coding 
    comp_seq : the compressed sequence
    file_comp : the path of the file 
    """
    dico_binary, comp_seq, file_comp = read_compressed_file()
    
    #for each items of the sequence convert it in binary string on 8 bits
    bin_str = ""
    for value in comp_seq:
        code = ord(value)
        bin_str += '{:08b}'.format(code)
        
    #remove the number of zeroes added 
    
    added = int(dico_binary["add"])
    #if the padding is equal to 0, don't cut anathing from the sequence
    if added == 0: 
        bin_seq = bin_str
    else: 
        bin_seq = bin_str[:-added]
    
    return bin_seq, dico_binary, comp_seq, file_comp


def binary_to_seq():
    """
    This function converts binary string in orignal sequence 
    according to the dictionnary containing the binary code

    Returns
    -------
    dna_seq : original sequence decompressed 
    bin_seq : binary sequence
    comp_seq : the compressed sequence
    file_comp : the path of the file 
    """
    bin_seq, dico_binary, comp_seq, file_comp = utf8_to_binary()
    
    #for each binary value associate the corresponding letter (key) 
    #according to the dictionnary 
    dna_seq = ""
    reading_binary = ""
    for value in bin_seq:
        reading_binary += value
        for letter, code in dico_binary.items():
            if code == reading_binary:
                dna_seq += letter
                reading_binary = ""
                break
    
    #print(dna_seq, bin_seq, comp_seq, file_comp)
    return dna_seq, bin_seq, comp_seq, file_comp



def save_decompression(): 
    """
    This function saves the decompressed sequence in a new file

    Returns
    -------
    comp_seq : the compressed sequence
    dna_seq : original sequence decompressed 
    bin_seq : binary sequence
    """
    dna_seq, bin_seq, comp_seq, file_comp = binary_to_seq()
    
    #create a new file containing the original sequence
    file_path = os.path.splitext(file_comp)[0]
    file = open(file_path+ "_decompressed.txt", "w")
    file.write(dna_seq)
    file.close()
    
    #show a message for saving
    messagebox.showinfo("Information", "Your decompression has been saved in "
                        +file_path+"_decompressed.txt.")
    
    #print(comp_seq, dna_seq, bin_seq)
    return comp_seq, dna_seq, bin_seq



def decompression_inversion(): 
    """
    This function performs a decompression followed by a bwt reconstruction
    from a file containing a bwt compressed sequence. 
    And saves the result in a new file 

    Returns
    -------
    dna_seq : the sequence decompressed
    comp_seq : the compressed sequence
    inverse_bwt : the original sequence after bwt reconstruction

    """
    dna_seq, bin_seq, comp_seq, file_comp = binary_to_seq()
    
    #bwt reconstruction
    table = [""] * len(dna_seq)

    for i in range(0,len(dna_seq),1):
        table = [dna_seq[i] + table[i] for i in range(0,len(dna_seq))]
        table = sorted(table)
    
    original_seq = None 
    for row in table : 
        if row.endswith("$"):
           original_seq = row

    inverse_bwt = original_seq.rstrip("$")  
    
    
    #write the original sequence in a new created file 
    file_path = os.path.splitext(file_comp)[0]
    file_inv = open(file_path + "_decompressed_original.txt", "w") 
    file_inv.write(inverse_bwt) 
    file_inv.close()
    
    messagebox.showinfo("Information", "Your decompressed and bwt reconstruction has been saved in " \
                        +file_path +"_decompressed_original.txt file.")
 
    return dna_seq, comp_seq, inverse_bwt
   

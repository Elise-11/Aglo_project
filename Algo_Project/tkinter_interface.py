#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This script contains functions related to the interface
"""
from tkinter import Tk,Label, Button
from burrows_wheeler_transform import * 
from huffman import *


        
def cut_display(seq_view): 
    """
    This function allows a better display of elements in the labels 
    it cut element each 30 characteres and add a \n to make a return to the line 
    """
    seq_list = []
    for i in range(0,len(seq_view), 30): 
        sequence = seq_view[i:i+30]
        seq_list.append(sequence)
        
    display_seq = "\n".join(seq_list)
        
    return display_seq
    


def bwt_interface() :
    """
    This function retrieve the orginal sequence and bwt sequence from the 
    save_transform function, and change the text in a label to show
    the orginal sequence with the added $ and the transformed sequence.
    """
    seq, bwt = save_transform()
    display_seq = cut_display(seq)
    display_bwt = cut_display(bwt)
    
    label_bwt1.configure(text="Original sequence \n" + display_seq +"\n" +"\n"+ \
                               "Bwt sequence \n"+display_bwt)



def bwt_inversion():
    """
    This function retrieve the bwt sequence and sequence reconstructed 
    from the bwt_inverse function , and change the text in a label to show
    the bwt sequence and the result of detransformation 
    corresponding to the original sequence. 
    """
    bwt,inverse_bwt = bwt_inverse()
    display_bwt = cut_display(bwt)
    display_seq = cut_display(inverse_bwt)

    label_bwtinv1.configure(text= "Bwt sequence \n" + display_bwt +"\n" + "\n" 
                               "Original sequence "+"\n"+ display_seq)
    
    


def huffman_compression(): 
    """
    This function retrieves the sequence not compressed, the binary sequence and
    the utf-8 sequence (compressed sequence), and display them in a label
    """
    comp_seq, binary_seq, seq = save_compression()
    display_binseq = cut_display(binary_seq)
    display_comp = cut_display(comp_seq)
    display_seq = cut_display(seq)
    
    label_compression1.configure( text =" DNA sequence \n" + display_seq +"\n" + "\n" 
                                       "Binary sequence "+"\n"+ display_binseq +"\n" + "\n"+ 
                                           "UTF-8 sequence "+"\n"+ display_comp )
            
        
        
def bwt_and_compression():
    """
    This function retrieves the bwt sequence not compressed, the binary sequence and
    the utf-8 sequence (compressed sequence), and display them in a label. 
    """
    seq, binary_seq, comp_seq = bwt_binary_conversion()
    display_seq = cut_display(seq)
    display_binseq = cut_display(binary_seq)
    display_comp = cut_display(comp_seq)

    label_compression2.configure( text =" BWT sequence \n" + display_seq +"\n" + "\n" 
                                   "Binary sequence "+"\n"+ display_binseq +"\n" + "\n"+ 
                                       "UTF-8 sequence "+"\n"+ display_comp )
    
        
def huffman_decompression(): 
    """
    This function retrieves the compressed sequence, the binary sequence and
    the decompressed sequence, and display them in a label. 
    """
    comp_seq, dna_seq, bin_seq = save_decompression()
    print(comp_seq, dna_seq, bin_seq)
    display_comp = cut_display(comp_seq)
    display_binseq = cut_display(bin_seq)
    display_seq = cut_display(dna_seq)
    
    label_decompression1.configure( text =" UTF-8 sequence \n" + display_comp +"\n" + 
    								"\n"+"Binary sequence "+"\n"+ display_binseq +"\n" + "\n" + 
                                        "Decompressed sequence "+"\n"+ display_seq )

        
        
        
def decompression_bwtinversion(): 
    """
    This function retrieves the compressed sequence, the decompressed bwt sequence and
    the reconstructed original sequence, and display them in a label. 
    """
    dna_seq, comp_seq, inverse_bwt = decompression_inversion()
    comp_seq = cut_display(comp_seq)
    dna_seq = cut_display(dna_seq)
    inverse_bwt = cut_display(inverse_bwt)

    label_decompression2.configure(text =" UTF-8 sequence \n" + comp_seq +"\n" + "\n" 
                                "Decompressed BWT sequence  "+"\n"+ dna_seq +"\n" + "\n"+ 
                                    "Original sequence "+"\n"+ inverse_bwt)


        
#Creation of the main interface 
window = Tk()
window.title("BWT & Huffman compression")

##############################################################################
##############################################################################

#Creation of informative labels above the buttons 
label_info1= Label(window, text = "BWT \n one-step \n without compression")
#label_info2= Label(window, text = "BWT \n step-by-step \n without compression")
label_info3=Label(window,text="BWT reconstruction \n one-step \n without compression")
#label_info4=Label(window,text="BWT reconstruction \n step-by-step \n without compression")

label_info5= Label(window, text = "Single \n Huffman compression")
label_info6= Label(window, text = "BWT \n & \n Huffman compression ")
label_info7 = Label(window, text = "Single decompression")
label_info8 = Label(window, text = "Decompression \n & \n BWT reconstruction ")


#gridding informatives
label_info1.grid(row=1, column=2,padx=5, pady=5)
#label_info2.grid(row=1, column=2,padx=5, pady=5)
label_info3.grid(row=1, column=3,padx=5, pady=5)
#label_info4.grid(row=1, column=4,padx=5, pady=5)

label_info5.grid(row=4, column=1,padx=5, pady=5)
label_info6.grid(row=4, column=2,padx=5, pady=5)
label_info7.grid(row=4, column=3,padx=5, pady=5)
label_info8.grid(row=4, column=4,padx=5, pady=5)

##############################################################################
##############################################################################

#button creation 
button1= Button(window, text = "BWT", height=3, width=17, command = bwt_interface)
#button2= Button(window,height=3, width=17, text="   >   ", command=transform_step)
button3=Button(window, text="BWT reconstruction",height=3, width=17, command = bwt_inversion)
#button4=Button(window, text="Reconstruction matrix",height=3, width=17)

button5= Button(window, text="Compress",height=3, width=17, command = huffman_compression)
button6= Button(window, text="BWT \n + \n compress",height=3, width=17, command= bwt_and_compression)
button7 = Button(window, text="Decompress", height=3, width=17, command = huffman_decompression)
button8 = Button(window, text="Decompress \n + \n BWT reconstruction"
                                  ,height=3, width=17, command=decompression_bwtinversion)

#button grid 
button1.grid(row=2, column=2,padx=5, pady=5)
#button2.grid(row=2, column=2, padx=5, pady=5)
button3.grid(row=2, column=3, padx=5, pady=5)
#button4.grid(row=2, column=4, padx=5, pady=5)

button5.grid(row=5, column=1,padx=5, pady=5)
button6.grid(row=5, column=2,padx=5, pady=5)
button7.grid(row=5, column=3, padx=5, pady=5)
button8.grid(row=5, column=4, padx=5, pady=5)

##############################################################################
##############################################################################
    
#creation of labels containing the results below the buttons 
label_bwt1= Label(window,bg="white",text = "",justify="left", height=15, width=32)
#label_bwt2 = Label(window,bg="white",text = "",justify="left", height=15, width=32)
label_bwtinv1=Label(window,bg="white",text="",justify="left",height=15, width=32)
#label_bwtinv2=Label(window,bg="white",text="",justify="left",height=15, width=32)

label_compression1= Label(window,bg="white", justify="left",text ="",height=15, width=32)
label_compression2 = Label(window,bg="white", justify="left", text = "",height=15, width=32)
label_decompression1 = Label(window,bg="white", justify="left",text = "",height=15, width=32)
label_decompression2= Label(window,bg="white",justify="left",text = "",height=15, width=32)


#result label grid 
label_bwt1.grid(row=3, column=2,padx=5, pady=5)
#label_bwt2.grid(row=3, column=2,padx=5, pady=5)
label_bwtinv1.grid(row=3, column=3,padx=5, pady=5)
#label_bwtinv2.grid(row=3, column=4,padx=5, pady=5)

label_compression1.grid(row=6, column=1, padx=5, pady=5)
label_compression2.grid(row=6, column=2, padx=5, pady=5)
label_decompression1.grid(row=6, column=3,padx=5, pady=5)
label_decompression2.grid(row=6, column=4,padx=5, pady=5)

##############################################################################
##############################################################################

#lauch the interface
window.mainloop()
window.destroy()



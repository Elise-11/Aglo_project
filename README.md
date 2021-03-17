
# Algorithmic project 



## Burrows-Wheeler transform & Huffman compression

* This project aims to implement the Burrows-Wheeler transform algorithm and a Huffman compression
  and perform them on a DNA sequence.
* The programming language used is python.
* The different algorithms are executed through a graphical interface.



### Dependencies 

* This project uses python3, if your python version is not update please write the following command in your terminal.

```{}
sudo apt update
sudo apt -y upgrade

python3 -V
```

* For the proper functioning of the GUI we need tkinter, the following command allows to install it.

```{}
sudo apt-get install python3-tk
```



### Launch the program
* clone the repository Algo_project, move to the folder Algo_project. 
* To launch the program write the following command in your terminal :python3 main.py
* To test the interface you can use the file present in the Algo_project folder named sequence_test.txt.

```{}
git clone https://github.com/Elise-11/Algo_project_final.git
cd Algo_project_final/Algo_project
python3 main.py 
```



### How the graphical interface works ?

#### Buttons 

All buttons open a window to choose the file on which you want to perform the operation, display the results of the operation in the window and save the result of the operation in a new file.

#### file content 

* BWT : Input file -> DNA sequence in lower case and/or upper case
output file -> BWT sequence (DNA sequence transformed)

* BWT reconstruction : Input file -> BWT sequence (DNA sequence transformed)
Output file -> Original DNA sequence (rebuilt)

* Compress : Input file -> the sequence to be compressed 
Output file -> the decompressed sequence

* BWT + compress : Input file -> DNA sequence in lower case and/or upper case to be transformed and compressed
Output file -> BWT sequence compressed 

* Decompress : Input file -> compressed sequence 
Output file -> decompressed sequence

* Decompress + BWT reconstruction : Input file -> BWT compressed sequence
Output file -> Original DNA sequence rebuilt



### Possible improvements 

* For the display it would be interesting to change the Label in Text with a scrollbar because for long sequences the display is not optimal. 

* Regarding the BWT transformation, it would be interesting to add intermediate steps at the display level so that the user can see the different steps of the algorithm, although this would increase the complexity of the code in memory. 

* It would be interesting to improve the bwt transformation by changing the naive algorithm into an advanced algorithm to reduce the complexity of time. 

* It would be interesting to improve the Huffman compression taking into account the BWT transformation to increase the compression.

# FOLDING OF AN HP MODEL OF PROTEIN BY A MONTE CARLO ALGORITHM

Authors : Julien PICHON and Opale RAMBAUD

In a context of scholar project for Université de Paris 

## Objective

Create a program using the method described in an article. 
This method makes it possible to calculate the folding of a protein by means of a Monte Carlo algorithm . 
An arbitrary protein sequence can be submitted to the program in order to calculate its folding by this model.

Our work is based on this article : 

Thachuk C, Shmygelska A, Hoos HH. A replica exchange Monte Carlo algorithm for protein folding in the HP model. 
BMC Bioinformatics. 2007 Sep 17;8:342. PubMed PMID: 17875212; PubMed Central PMCID: PMC2071922.


## Environment and prerequisites : 

Python 3.7.3

Pymol 2.3.5

**Modules :** 

- random 
- sys
- argparse
- pymol
- copy

## Directories :


The data directory contains examples of sequenceHP in txt format 
The src directory contains all the source codes 
The docs directory contains the project report in pdf format

## Program :

To run the program the following command must be executed: 

python create_res.py --input_file --steps --output_pdb

with the following arguments:

--input_file : a file containing the HP sequence 
--steps : the number of steps you want (this argument is optional, the default value is 10000)
--output_pdb : the name of the output file in pdb format 

So, one example of this command is : 

python create_res --input_file HP1.txt --steps 1000 --output_pdb my_model.pdb 

The ouput is a pdb with a model for every folding. 



## Information :

The Crankshaft movement does not work optimally on long chains or when the number of steps is very large. 

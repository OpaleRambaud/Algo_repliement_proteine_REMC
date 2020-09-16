# FOLDING OF AN HP MODEL OF PROTEIN BY A MONTE CARLO ALGORITHM

Authors : 

Julien PICHON : julien.pichon@cri-paris.org

Opale RAMBAUD : opale.rambaud@gmail.fr

In a context of scholar project for Université de Paris.

*Do not hesitate to contact us for further information* 

## Objective

Create a program using the method described in an article. 
This method makes it possible to calculate the folding of a protein by means of a Monte Carlo algorithm . 
An arbitrary protein sequence can be submitted to the program in order to calculate its folding by this model.

Our work is based on [this article](https://bmcbioinformatics.biomedcentral.com/articles/10.1186/1471-2105-8-342).

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


The data directory contains examples of HP sequences in txt format (3from the article and 2 building by us).

The src directory contains all the source codes. 

The docs directory contains the project report in pdf format.

You can also find a yamal file to create the optimal environment on your machine to run our scripts.

## Program :

Please clone the entire github bdefore using scripts.


To run the program the following command must be executed: 

python create_res.py --input_file --steps --output_pdb

with the following arguments:

--input_file : a file containing the HP sequence (-i)

--steps : the number of steps you want (this argument is optional, the default value is 10000) (-n)

--output_pdb : the name of the output file in pdb format (-o)

--crankshaft : choose to use the Crankshaft move that is risky because of errors (-c)

So, one example of this command is : 

`python create_res -i HP1.txt -n 1000 -o my_model.pdb `

The ouput is a pdb with a model for every folding. 



## Information :

The Crankshaft movement does not work optimally on long chains or when the number of steps is very large. 

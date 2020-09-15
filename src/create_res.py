import random as rd
import sys
import argparse
import residue
import MC


def myargs():
	parser = argparse.ArgumentParser()												
	parser.add_argument('-i', '--input_file', required = True, help = 
						'location of HP_file of the protein path')
	parser.add_argument('-n', '--steps', required = False, help = 
						'number of steps', default=10000,
					   type=int)
	parser.add_argument('-o', '--output_pdb', required = True, help = 
						'name of the pdb in output')				   
  
	args = parser.parse_args()
	return args

	

def argdet():
	if len(sys.argv) < 5:
		print('Check number of input argument!')
		exit()
	elif len(sys.argv) == 5:
		print('Run with default number of steps: 10000')
		args = myargs()
		return args
	elif len(sys.argv) == 7:
		print('Run with number of steps you choose')
		args = myargs()
		return args
		print(args)



def get_seq(input_file):
	coordinates = []
	with open(input_file, "r") as filin:
		for n, line in enumerate(filin):
			if n == 0:
				seq = line.strip()
			else:
				line = line.strip()
				line = line[1:-1].split(",")
				line = list(map(int, line))
				coordinates.append(line)
	return [seq, coordinates]
			




			
if __name__ == "__main__":

	"""
	args = argdet()
	input_file = args.input_file
	stp = args.steps
	output_pdb = args.output_pdb
	"""	
	seq, coordinates = get_seq("../data/HP1.txt")
	
	# creating list		   
	protein = []
  
	# appending instances to list
	for n, res in enumerate(seq):
		protein.append(residue.Residue("residue" + str((n+1)), res, coordinates[n], n))
	
	# Creating set for all coordinates
	protein_coordinates = set()
	for res in protein:
		protein_coordinates.add(tuple(res.coordinates))

	for res in protein:
		print(res.coordinates)
	print("\n")
	MC.MCsearch(1, protein, protein_coordinates)
	for res in protein:
		print(res.coordinates)
	print("\n")

	"""
	print(protein[2].coordinates)
	print(protein[3].coordinates)
	print(protein[4].coordinates)
	print("\n")
	print(protein_coordinates)
	
	protein[3].crankshaft_move(protein, protein_coordinates)
	print("\n")
	print(protein[2].coordinates)
	print(protein[3].coordinates)
	print(protein[4].coordinates)
	print("\n")
	print(protein_coordinates)
	
	
	protein[-1].end_move(protein[-2], protein_coordinates)
	print("\n")
	print(protein[-1].coordinates)
	print("\n")
	print(protein_coordinates)
	
	
	protein[2].corner_move(protein, protein_coordinates, 2)
	print("\n")
	print(protein[2].coordinates)
	print("\n")
	print(protein_coordinates)
	"""
	
	
	
	
	
	
	
	

import random as rd
import argparse
import residue
import MC


def get_args(argv = None):
	parser = argparse.ArgumentParser()												
	parser.add_argument('-i', '--input_file', required = True, help = 
						'location of HP_file of the protein path')
	parser.add_argument('-n', '--steps', required = False, help = 
						'number of steps', default=10000,
					   type=int)
	parser.add_argument('-o', '--output_pdb', required = True, help = 
						'name of the pdb in output')
	parser.add_argument('-c' '--crankshaft', help = 'add crankshaft_move(risky)', action="store_true")
	parser.set_defaults(crankshaft = False)
	return parser.parse_args(argv)

	
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
			

def create_protein(seq, coordinates):
	protein = []
	for n, res in enumerate(seq):
		protein.append(residue.Residue("residue" + str((n+1)), res, coordinates[n], n))
	protein_coordinates = set()
	for res in protein:
		protein_coordinates.add(tuple(res.coordinates))
	return [protein, protein_coordinates]
			
if __name__ == "__main__":

	argvals = None
	args = get_args(argvals)
	seq, coordinates = get_seq(args.input_file)
	protein, protein_coordinates = create_protein(seq, coordinates)
	if args.crankshaft:
		crankshaft = True
	else:
		crankshaft = False
	MC.MCsearch(protein, protein_coordinates, crankshaft, args.steps, args.output_pdb)

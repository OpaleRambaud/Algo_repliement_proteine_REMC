import random as rd
import sys
import argparse


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
			


class Residue:
	def __init__(self, name, polarity, coordinates):
		self.name = name
		self.polarity = polarity
		self.coordinates = coordinates
	
	def end_move(self, neighbour, protein_coordinates):
		available_mvt = []
		right = [neighbour.coordinates[0] + 1, neighbour.coordinates[1]]
		left = [neighbour.coordinates[0] - 1, neighbour.coordinates[1]]
		bottom = [neighbour.coordinates[0], neighbour.coordinates[1] - 1]
		top = [neighbour.coordinates[0], neighbour.coordinates[1] + 1]	
		if tuple(right) not in protein_coordinates:
			available_mvt.append(right)
		if tuple(left) not in protein_coordinates:
			available_mvt.append(left)
		if tuple(bottom) not in protein_coordinates:
			available_mvt.append(bottom)
		if tuple(top) not in protein_coordinates:
			available_mvt.append(top)
		mvt = rd.choice(available_mvt)
		protein_coordinates.remove(tuple(self.coordinates))
		self.coordinates = mvt
		protein_coordinates.add(tuple(self.coordinates))
	
	def corner_move(self, neighbour_list, protein_coordinates, residue_number):
		if (neighbour_list[residue_number - 1].coordinates[0] != neighbour_list[residue_number + 1].coordinates[0] and
			neighbour_list[residue_number + 1].coordinates[1] != neighbour_list[residue_number - 1].coordinates[1]):
			if tuple([neighbour_list[residue_number - 1].coordinates[0], neighbour_list[residue_number + 1].coordinates[1]]) not in protein_coordinates:
				protein_coordinates.remove(tuple(self.coordinates))
				self.coordinates = [neighbour_list[residue_number - 1].coordinates[0], neighbour_list[residue_number + 1].coordinates[1]]
				protein_coordinates.add(tuple(self.coordinates))
			elif tuple([neighbour_list[residue_number - 1].coordinates[1], neighbour_list[residue_number + 1].coordinates[0]]) not in protein_coordinates:
				protein_coordinates.remove(tuple(self.coordinates))
				self.coordinates = [neighbour_list[residue_number - 1].coordinates[1], neighbour_list[residue_number + 1].coordinates[0]]
				protein_coordinates.add(tuple(self.coordinates))
			else:
				print("redo step")
		
	def crankshaft_move(self, neighbour_list, protein_coordinates):
	#take list from self-3:self+3
		if neighbour_list[2].coordinates[0] != neighbour_list[4].coordinates[0] and neighbour_list[2].coordinates[1] != neighbour_list[4].coordinates[1]:
			if self.coordinates[0] != neighbour_list[5].coordinates[0] and self.coordinates[1] != neighbour_list[5].coordinates[1]:
				if neighbour_list[1].coordinates[0] == neighbour_list[2].coordinates[0] == neighbour_list[5].coordinates[0] == neighbour_list[-1].coordinates[0]:
					if self.coordinates[0] < neighbour_list[2].coordinates[0]:
						if (tuple([self.coordinates[0] + 2, self.coordinates[1]]) not in protein_coordinates and 
							tuple([neighbour_list[4].coordinates[0] + 2, neighbour_list[4].coordinates[1]]) not in protein_coordinates):
							protein_coordinates.remove(tuple(self.coordinates))
							protein_coordinates.remove(tuple(neighbour_list[4].coordinates))
							self.coordinates = [self.coordinates[0] + 2, self.coordinates[1]]
							neighbour_list[4].coordinates = [neighbour_list[4].coordinates[0] + 2, neighbour_list[4].coordinates[1]]
							protein_coordinates.add(tuple(self.coordinates))
							protein_coordinates.add(tuple(neighbour_list[4].coordinates))
						else:
							print("redo step")
					elif self.coordinates[0] > neighbour_list[2].coordinates[0]:
						if (tuple([self.coordinates[0] - 2, self.coordinates[1]]) not in protein_coordinates and 
							tuple([neighbour_list[4].coordinates[0] - 2, neighbour_list[4].coordinates[1]]) not in protein_coordinates):
							protein_coordinates.remove(tuple(self.coordinates))
							protein_coordinates.remove(tuple(neighbour_list[4].coordinates))
							self.coordinates = [self.coordinates[0] - 2, self.coordinates[1]]
							neighbour_list[4].coordinates = [neighbour_list[4].coordinates[0] - 2, neighbour_list[4].coordinates[1]]
							protein_coordinates.add(tuple(self.coordinates))
							protein_coordinates.add(tuple(neighbour_list[4].coordinates))
						else:
							print("redo step")
				elif neighbour_list[1].coordinates[1] == neighbour_list[2].coordinates[1] == neighbour_list[5].coordinates[1] == neighbour_list[-1].coordinates[1]:
					if self.coordinates[1] < neighbour_list[2].coordinates[1]:
						if (tuple([self.coordinates[0], self.coordinates[1] + 2]) not in protein_coordinates and 
							tuple([neighbour_list[4].coordinates[0], neighbour_list[4].coordinates[1] + 2]) not in protein_coordinates):
							protein_coordinates.remove(tuple(self.coordinates))
							protein_coordinates.remove(tuple(neighbour_list[4].coordinates))
							self.coordinates = [self.coordinates[0], self.coordinates[1] + 2]
							neighbour_list[4].coordinates = [neighbour_list[4].coordinates[0], neighbour_list[4].coordinates[1] + 2]
							protein_coordinates.add(tuple(self.coordinates))
							protein_coordinates.add(tuple(neighbour_list[4].coordinates))
						else:
							print("redo step")
					elif self.coordinates[1] > neighbour_list[2].coordinates[1]:
						if (tuple([self.coordinates[0], self.coordinates[1] - 2]) not in protein_coordinates and 
							tuple([neighbour_list[4].coordinates[0], neighbour_list[4].coordinates[1] - 2]) not in protein_coordinates):
							protein_coordinates.remove(tuple(self.coordinates))
							protein_coordinates.remove(tuple(neighbour_list[4].coordinates))
							self.coordinates = [self.coordinates[0], self.coordinates[1] - 2]
							neighbour_list[4].coordinates = [neighbour_list[4].coordinates[0], neighbour_list[4].coordinates[1] - 2]
							protein_coordinates.add(tuple(self.coordinates))
							protein_coordinates.add(tuple(neighbour_list[4].coordinates))
						else:
							print("redo step")
				elif neighbour_list[0].coordinates[0] == neighbour_list[0].coordinates[0] == neighbour_list[4].coordinates[0] == neighbour_list[5].coordinates[0]:
					if self.coordinates[0] < neighbour_list[4].coordinates[0]:
						if (tuple([self.coordinates[0] + 2, self.coordinates[1]]) not in protein_coordinates and 
							tuple([neighbour_list[2].coordinates[0] + 2, neighbour_list[2].coordinates[1]]) not in protein_coordinates):
							protein_coordinates.remove(tuple(self.coordinates))
							protein_coordinates.remove(tuple(neighbour_list[2].coordinates))
							self.coordinates = [self.coordinates[0] + 2, self.coordinates[1]]
							neighbour_list[2].coordinates = [neighbour_list[2].coordinates[0] + 2, neighbour_list[2].coordinates[1]]
							protein_coordinates.add(tuple(self.coordinates))
							protein_coordinates.add(tuple(neighbour_list[2].coordinates))
						else:
							print("redo step")
					elif self.coordinates[0] > neighbour_list[4].coordinates[0]:
						if (tuple([self.coordinates[0] - 2, self.coordinates[1]]) not in protein_coordinates and 
							tuple([neighbour_list[2].coordinates[0] - 2, neighbour_list[2].coordinates[1]]) not in protein_coordinates):
							protein_coordinates.remove(tuple(self.coordinates))
							protein_coordinates.remove(tuple(neighbour_list[2].coordinates))
							self.coordinates = [self.coordinates[0] - 2, self.coordinates[1]]
							neighbour_list[2].coordinates = [neighbour_list[2].coordinates[0] - 2, neighbour_list[2].coordinates[1]]
							protein_coordinates.add(tuple(self.coordinates))
							protein_coordinates.add(tuple(neighbour_list[2].coordinates))
						else:
							print("redo step")
				elif neighbour_list[0].coordinates[1] == neighbour_list[0].coordinates[1] == neighbour_list[4].coordinates[1] == neighbour_list[5].coordinates[1]:
					if self.coordinates[1] < neighbour_list[4].coordinates[1]:
						if (tuple([self.coordinates[0], self.coordinates[1] + 2]) not in protein_coordinates and 
							tuple([neighbour_list[2].coordinates[0], neighbour_list[2].coordinates[1] + 2]) not in protein_coordinates):
							protein_coordinates.remove(tuple(self.coordinates))
							protein_coordinates.remove(tuple(neighbour_list[2].coordinates))
							self.coordinates = [self.coordinates[0], self.coordinates[1] + 2]
							neighbour_list[2].coordinates = [neighbour_list[2].coordinates[0], neighbour_list[2].coordinates[1] + 2]
							protein_coordinates.add(tuple(self.coordinates))
							protein_coordinates.add(tuple(neighbour_list[2].coordinates))
						else:
							print("redo step")
					elif self.coordinates[1] > neighbour_list[4].coordinates[1]:
						if (tuple([self.coordinates[0], self.coordinates[1] - 2]) not in protein_coordinates and 
							tuple([neighbour_list[2].coordinates[0], neighbour_list[2].coordinates[1] - 2]) not in protein_coordinates):
							protein_coordinates.remove(tuple(self.coordinates))
							protein_coordinates.remove(tuple(neighbour_list[2].coordinates))
							self.coordinates = [self.coordinates[0], self.coordinates[1] - 2]
							neighbour_list[2].coordinates = [neighbour_list[2].coordinates[0], neighbour_list[2].coordinates[1] - 2]
							protein_coordinates.add(tuple(self.coordinates))
							protein_coordinates.add(tuple(neighbour_list[2].coordinates))
						else:
							print("redo step")
				else:
					print("redo step")

			
if __name__ == "__main__":


	args = argdet()
	input_file = args.input_file
	stp = args.steps
	output_pdb = args.output_pdb
	
	seq, coordinates = get_seq(input_file)
	
	# creating list		   
	protein = []
  
	# appending instances to list
	for n, res in enumerate(seq):
		protein.append(Residue("residue" + str((n+1)), res, coordinates[n]))
	
	# Creating set for all coordinates
	protein_coordinates = set()
	for res in protein:
		protein_coordinates.add(tuple(res.coordinates))

	print(protein[2].coordinates)
	print(protein[3].coordinates)
	print(protein[4].coordinates)
	print("\n")
	print(protein_coordinates)
	"""
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
	"""
	
	protein[2].corner_move(protein, protein_coordinates, 2)
	print("\n")
	print(protein[2].coordinates)
	print("\n")
	print(protein_coordinates)
	
	
	
	
	
	
	
	
	

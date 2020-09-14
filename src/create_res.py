import random as rd

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
		right = neighbour.coordinates[0] + 1, neighbour.coordinates[1]
		left = neighbour.coordinates[0] - 1, neighbour.coordinates[1]
		bottom = neighbour.coordinates[0], neighbour.coordinates[1] + 1
		top = neighbour.coordinates[0], neighbour.coordinates[1] - 1		
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
			
			
if __name__ == "__main__":
	
	seq, coordinates = get_seq("../data/HP1.txt")
	
	# creating list        
	protein = []
  
	# appending instances to list
	for n, res in enumerate(seq):
		protein.append(Residue("residue" + str((n+1)), res, coordinates[n]))
	
	# Creating set for all coordinates
	protein_coordinates = set()
	for res in protein:
		protein_coordinates.add(tuple(res.coordinates))

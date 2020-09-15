import random as rd

class Residue:
	def __init__(self, name, polarity, coordinates, number):
		self.name = name
		self.polarity = polarity
		self.coordinates = coordinates
		self.number = number
	
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
	
	def corner_move(self, neighbour_list, protein_coordinates):
		if (neighbour_list[self.number - 1].coordinates[0] != neighbour_list[self.number + 1].coordinates[0] and
			neighbour_list[self.number + 1].coordinates[1] != neighbour_list[self.number - 1].coordinates[1]):
			if tuple([neighbour_list[self.number - 1].coordinates[0], neighbour_list[self.number + 1].coordinates[1]]) not in protein_coordinates:
				protein_coordinates.remove(tuple(self.coordinates))
				self.coordinates = [neighbour_list[self.number - 1].coordinates[0], neighbour_list[self.number + 1].coordinates[1]]
				protein_coordinates.add(tuple(self.coordinates))
			elif tuple([neighbour_list[self.number - 1].coordinates[1], neighbour_list[self.number + 1].coordinates[0]]) not in protein_coordinates:
				protein_coordinates.remove(tuple(self.coordinates))
				self.coordinates = [neighbour_list[self.number - 1].coordinates[1], neighbour_list[self.number + 1].coordinates[0]]
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

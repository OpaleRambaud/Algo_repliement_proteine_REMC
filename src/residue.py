import random as rd

class Residue:
	"""This class allows to simulate create a residue object, which is ofter part of a protein."
	
	The class contains attributes relative to the name of amino-acid, if he is polar or not, its
	coordinates in a 2D lattice and its position in the protein.
	He has 3 methods, describing the 3 main movements possible in the HP model call VSHD movement.
	However, its crankshaft method has unidentified issue appearing sometimes for long chain protein
	or when there is a lot of step movement performed.
	"""
	
	def __init__(self, name, polarity, coordinates, number):
		"""Polarity, coordinates and number are the important attributes for methods, name is for further application.
		
		Name attribute is usually a string such as residue[1]. 
		Polarity is a string, H for hydrophobic and P for polar.
		Coordinates is a list such as [x, y].
		Number is a int, corresponding to the position IN THE LIST containing all the objects, not the position in the protein.
		"""
		
		self.name = name
		self.polarity = polarity
		self.coordinates = coordinates
		self.number = number
	
	def end_move(self, neighbour, protein_coordinates):
		"""Method for amino-acid with a free-end, allows it to translate to 90,180, 270°.
		
		neighbour corresponds to the only one object close to him in the protein.
		protein_coordinates is a set of all the coordinates already taken by an object in the protein.
		If several options are available, movement are random.
		"""
		
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
		if len(available_mvt) == 0:
			return
		if len(available_mvt) == 1:
			mvt = available_mvt[0]
		else:
			mvt = rd.choice(available_mvt)
		protein_coordinates.remove(tuple(self.coordinates))
		self.coordinates = mvt
		protein_coordinates.add(tuple(self.coordinates))
	
	def corner_move(self, neighbour1, neighbour2, protein_coordinates):
		"""Movement when an object and it's neighbour form an elbow with its two neighbours.
		
		The objet moved to the coordinates forming a symmetry with it's two neighbours as axis.
		Neighbour1 is the object before self in the protein, neighbour2 is the one after.
		"""
		
		# Right bottom movement. 
		if neighbour1.coordinates[0] > self.coordinates[0] and neighbour2.coordinates[1] < self.coordinates[1]:
			if tuple([neighbour1.coordinates[0], neighbour2.coordinates[1]]) not in protein_coordinates:
				protein_coordinates.remove(tuple(self.coordinates))
				self.coordinates = [neighbour1.coordinates[0], neighbour2.coordinates[1]]
				protein_coordinates.add(tuple(self.coordinates))
		elif neighbour2.coordinates[0] > self.coordinates[0] and neighbour1.coordinates[1] < self.coordinates[1]:
			if tuple([neighbour2.coordinates[0], neighbour1.coordinates[1]]) not in protein_coordinates:
				protein_coordinates.remove(tuple(self.coordinates))
				self.coordinates = [neighbour2.coordinates[0], neighbour1.coordinates[1]]
				protein_coordinates.add(tuple(self.coordinates))
		# Left top movement.
		elif neighbour1.coordinates[0] < self.coordinates[0] and neighbour2.coordinates[1] > self.coordinates[1]:
			if tuple([neighbour1.coordinates[0], neighbour2.coordinates[1]]) not in protein_coordinates:
				protein_coordinates.remove(tuple(self.coordinates))
				self.coordinates = [neighbour1.coordinates[0], neighbour2.coordinates[1]]
				protein_coordinates.add(tuple(self.coordinates))
		elif neighbour2.coordinates[0] < self.coordinates[0] and neighbour1.coordinates[1] > self.coordinates[1]:
			if tuple([neighbour2.coordinates[0], neighbour1.coordinates[1]]) not in protein_coordinates:
				protein_coordinates.remove(tuple(self.coordinates))
				self.coordinates = [neighbour2.coordinates[0], neighbour1.coordinates[1]]
				protein_coordinates.add(tuple(self.coordinates))
		# Right top movement.
		elif neighbour1.coordinates[0] > self.coordinates[0] and neighbour2.coordinates[1] > self.coordinates[1]:
			if tuple([neighbour1.coordinates[0], neighbour2.coordinates[1]]) not in protein_coordinates:
				protein_coordinates.remove(tuple(self.coordinates))
				self.coordinates = [neighbour2.coordinates[0], neighbour1.coordinates[1]]
				protein_coordinates.add(tuple(self.coordinates))
		elif neighbour2.coordinates[0] > self.coordinates[0] and neighbour1.coordinates[1] > self.coordinates[1]:
			if tuple([neighbour2.coordinates[0], neighbour1.coordinates[1]]) not in protein_coordinates:
				protein_coordinates.remove(tuple(self.coordinates))
				self.coordinates = [neighbour2.coordinates[0], neighbour1.coordinates[1]]
				protein_coordinates.add(tuple(self.coordinates))
		# Left bottom movement
		elif neighbour1.coordinates[0] < self.coordinates[0] and neighbour2.coordinates[1] < self.coordinates[1]:
			if tuple([neighbour1.coordinates[0], neighbour2.coordinates[1]]) not in protein_coordinates:
				protein_coordinates.remove(tuple(self.coordinates))
				self.coordinates = [neighbour1.coordinates[0], neighbour2.coordinates[1]]
				protein_coordinates.add(tuple(self.coordinates))
		elif neighbour2.coordinates[0] < self.coordinates[0] and neighbour1.coordinates[1] < self.coordinates[1]:
			if tuple([neighbour2.coordinates[0], neighbour1.coordinates[1]]) not in protein_coordinates:
				protein_coordinates.remove(tuple(self.coordinates))
				self.coordinates = [neighbour2.coordinates[0], neighbour1.coordinates[1]]
				protein_coordinates.add(tuple(self.coordinates))
		
	def crankshaft_move(self, neighbour_list, protein_coordinates):
		"""Movement for U-shaped part of the protein, where we could imagine 2 objects moving to have a reversed U.
	
		neighbour_list is a list of all objects of the protein.
		There is an issue with this method, doing sometimes a crankshaft when and where it shouldn't.
		Method could be factorized with a function taking axis movement, sens of the protein and movement direction as arguments, but didn't had the time.
		"""
	
		# Move on x axis.
		if (neighbour_list[self.number - 2].coordinates[0] == neighbour_list[self.number - 1].coordinates[0] == 
			neighbour_list[self.number + 2].coordinates[0] == neighbour_list[self.number + 3].coordinates[0]):
			# Right forward move.
			if self.coordinates[0] < neighbour_list[self.number - 1].coordinates[0]:
				if (tuple([self.coordinates[0] + 2, self.coordinates[1]]) not in protein_coordinates and 
					tuple([neighbour_list[self.number + 1].coordinates[0] + 2, neighbour_list[self.number + 1].coordinates[1]]) not in protein_coordinates):
					protein_coordinates.remove(tuple(self.coordinates))
					protein_coordinates.remove(tuple(neighbour_list[self.number + 1].coordinates))
					self.coordinates = [self.coordinates[0] + 2, self.coordinates[1]]
					neighbour_list[self.number + 1].coordinates = [neighbour_list[self.number + 1].coordinates[0] + 2, neighbour_list[self.number + 1].coordinates[1]]
					protein_coordinates.add(tuple(self.coordinates))
					protein_coordinates.add(tuple(neighbour_list[self.number + 1].coordinates))
			elif self.coordinates[0] > neighbour_list[self.number - 1].coordinates[0]:
				# Left forward move.
				if (tuple([self.coordinates[0] - 2, self.coordinates[1]]) not in protein_coordinates and 
					tuple([neighbour_list[self.number + 1].coordinates[0] - 2, neighbour_list[self.number + 1].coordinates[1]]) not in protein_coordinates):
					protein_coordinates.remove(tuple(self.coordinates))
					protein_coordinates.remove(tuple(neighbour_list[self.number + 1].coordinates))
					self.coordinates = [self.coordinates[0] - 2, self.coordinates[1]]
					neighbour_list[self.number + 1].coordinates = [neighbour_list[self.number + 1].coordinates[0] - 2, neighbour_list[self.number + 1].coordinates[1]]
					protein_coordinates.add(tuple(self.coordinates))
					protein_coordinates.add(tuple(neighbour_list[self.number + 1].coordinates))
			# Right reverse move.
		elif (neighbour_list[self.number + 2].coordinates[0] == neighbour_list[self.number + 1].coordinates[0] == 
			neighbour_list[self.number - 2].coordinates[0] == neighbour_list[self.number - 3].coordinates[0]):
			if self.coordinates[0] < neighbour_list[self.number - 1].coordinates[0]:
				if (tuple([self.coordinates[0] + 2, self.coordinates[1]]) not in protein_coordinates and 
					tuple([neighbour_list[self.number - 1].coordinates[0] + 2, neighbour_list[self.number - 1].coordinates[1]]) not in protein_coordinates):
					protein_coordinates.remove(tuple(self.coordinates))
					protein_coordinates.remove(tuple(neighbour_list[self.number + 1].coordinates))
					self.coordinates = [self.coordinates[0] + 2, self.coordinates[1]]
					neighbour_list[self.number - 1].coordinates = [neighbour_list[self.number - 1].coordinates[0] + 2, neighbour_list[self.number - 1].coordinates[1]]
					protein_coordinates.add(tuple(self.coordinates))
					protein_coordinates.add(tuple(neighbour_list[self.number - 1].coordinates))
			# Left reverse move.
			elif self.coordinates[0] > neighbour_list[self.number - 1].coordinates[0]:
				if (tuple([self.coordinates[0] - 2, self.coordinates[1]]) not in protein_coordinates and 
					tuple([neighbour_list[self.number - 1].coordinates[0] - 2, neighbour_list[self.number - 1].coordinates[1]]) not in protein_coordinates):
					protein_coordinates.remove(tuple(self.coordinates))
					protein_coordinates.remove(tuple(neighbour_list[self.number + 1].coordinates))
					self.coordinates = [self.coordinates[0] - 2, self.coordinates[1]]
					neighbour_list[self.number - 1].coordinates = [neighbour_list[self.number - 1].coordinates[0] - 2, neighbour_list[self.number - 1].coordinates[1]]
					protein_coordinates.add(tuple(self.coordinates))
					protein_coordinates.add(tuple(neighbour_list[self.number - 1].coordinates))
		# If move not available on x axis, try it on y axis.
		elif (neighbour_list[self.number - 2].coordinates[1] == neighbour_list[self.number - 1].coordinates[1] == 
			neighbour_list[self.number + 2].coordinates[1] == neighbour_list[self.number + 3].coordinates[1]):
			# Right forward move.
			if self.coordinates[1] < neighbour_list[self.number - 1].coordinates[1]:
				if (tuple([self.coordinates[0], self.coordinates[1] + 2]) not in protein_coordinates and 
					tuple([neighbour_list[self.number + 1].coordinates[0], neighbour_list[self.number + 1].coordinates[1] + 2]) not in protein_coordinates):
					protein_coordinates.remove(tuple(self.coordinates))
					protein_coordinates.remove(tuple(neighbour_list[self.number + 1].coordinates))
					self.coordinates = [self.coordinates[0] + 2, self.coordinates[1]]
					neighbour_list[self.number + 1].coordinates = [neighbour_list[self.number + 1].coordinates[0], neighbour_list[self.number + 1].coordinates[1] + 2]
					protein_coordinates.add(tuple(self.coordinates))
					protein_coordinates.add(tuple(neighbour_list[self.number + 1].coordinates))
			# Left forward move.
			elif self.coordinates[1] > neighbour_list[self.number - 1].coordinates[1]:
				if (tuple([self.coordinates[0], self.coordinates[1] - 2]) not in protein_coordinates and 
					tuple([neighbour_list[self.number + 1].coordinates[0], neighbour_list[self.number + 1].coordinates[1] - 2]) not in protein_coordinates):
					protein_coordinates.remove(tuple(self.coordinates))
					protein_coordinates.remove(tuple(neighbour_list[self.number + 1].coordinates))
					self.coordinates = [self.coordinates[0], self.coordinates[1] - 2]
					neighbour_list[self.number + 1].coordinates = [neighbour_list[self.number + 1].coordinates[0], neighbour_list[self.number + 1].coordinates[1] - 2]
					protein_coordinates.add(tuple(self.coordinates))
					protein_coordinates.add(tuple(neighbour_list[self.number + 1].coordinates))
			# Right reverse move.
		elif (neighbour_list[self.number + 2].coordinates[1] == neighbour_list[self.number + 1].coordinates[1] == 
			neighbour_list[self.number - 2].coordinates[1] == neighbour_list[self.number - 3].coordinates[1]):
			if self.coordinates[0] < neighbour_list[self.number - 1].coordinates[1]:
				if (tuple([self.coordinates[0], self.coordinates[1] + 2]) not in protein_coordinates and 
					tuple([neighbour_list[self.number - 1].coordinates[0], neighbour_list[self.number - 1].coordinates[1] + 2]) not in protein_coordinates):
					protein_coordinates.remove(tuple(self.coordinates))
					protein_coordinates.remove(tuple(neighbour_list[self.number + 1].coordinates))
					self.coordinates = [self.coordinates[0], self.coordinates[1] + 2]
					neighbour_list[self.number - 1].coordinates = [neighbour_list[self.number - 1].coordinates[0], neighbour_list[self.number - 1].coordinates[1] + 2]
					protein_coordinates.add(tuple(self.coordinates))
					protein_coordinates.add(tuple(neighbour_list[self.number - 1].coordinates))
			elif self.coordinates[0] > neighbour_list[self.number - 1].coordinates[1]:
				if (tuple([self.coordinates[0], self.coordinates[1] - 2]) not in protein_coordinates and 
					tuple([neighbour_list[self.number - 1].coordinates[0], neighbour_list[self.number - 1].coordinates[1] - 2]) not in protein_coordinates):
					protein_coordinates.remove(tuple(self.coordinates))
					protein_coordinates.remove(tuple(neighbour_list[self.number + 1].coordinates))
					self.coordinates = [self.coordinates[0], self.coordinates[1] - 2]
					neighbour_list[self.number - 1].coordinates = [neighbour_list[self.number - 1].coordinates[0], neighbour_list[self.number - 1].coordinates[1] - 2]
					protein_coordinates.add(tuple(self.coordinates))
					protein_coordinates.add(tuple(neighbour_list[self.number - 1].coordinates))

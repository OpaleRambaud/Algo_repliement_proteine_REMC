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
	# Method could be factorize with a function taking axis movement, sens of the protein and movement direction as arguments, but didn't had the time.
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
			else:
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
			else:
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
			else:
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
			else:
				if (tuple([self.coordinates[0], self.coordinates[1] - 2]) not in protein_coordinates and 
					tuple([neighbour_list[self.number - 1].coordinates[0], neighbour_list[self.number - 1].coordinates[1] - 2]) not in protein_coordinates):
					protein_coordinates.remove(tuple(self.coordinates))
					protein_coordinates.remove(tuple(neighbour_list[self.number + 1].coordinates))
					self.coordinates = [self.coordinates[0], self.coordinates[1] - 2]
					neighbour_list[self.number - 1].coordinates = [neighbour_list[self.number - 1].coordinates[0], neighbour_list[self.number - 1].coordinates[1] - 2]
					protein_coordinates.add(tuple(self.coordinates))
					protein_coordinates.add(tuple(neighbour_list[self.number - 1].coordinates))

					
					
					
					
					
					
		
		
		
		
		
		

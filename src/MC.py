import random as rd
import copy
import math

def MCsearch(step, conformation, protein_coordinates, crankshaft, TEMPERATURE):
	for n, i in enumerate(range(step)):		
		if n == 0:
			for aa in conformation:
				print(aa.coordinates)
			print("\n")
			energy = calcul_energy(conformation)
		current_res = rd.choice(conformation)
		previous_coordinates = copy.deepcopy(protein_coordinates)
		previous_conformation = copy.deepcopy(conformation)
		if current_res == conformation[0]:
			current_res.end_move(conformation[1], protein_coordinates)
		elif current_res == conformation[-1]:
			current_res.end_move(conformation[-2], protein_coordinates)
		else:
			if crankshaft == True:
				if current_res.number < 3 or current_res.number > len(conformation) - 4:
					current_res.corner_move(conformation[current_res.number - 1], conformation[current_res.number + 1], protein_coordinates)
				else:
					rd.choice([current_res.corner_move(conformation[current_res.number - 1], conformation[current_res.number + 1], protein_coordinates),
						current_res.crankshaft_move(conformation, protein_coordinates)])
			else:
				current_res.corner_move(conformation[current_res.number - 1], conformation[current_res.number + 1], protein_coordinates)
		for position, resi in enumerate(conformation[:-1]):
			if abs(resi.coordinates[0] - conformation[position].coordinates[0]) > 1 and abs(resi.coordinates[1] - conformation[position].coordinates[1]) > 1:
				conformation_error = True
			else:
				conformation_error = False
		if conformation_error == True:
			conformation = previous_conformation
			protein_coordinates = previous_coordinates
			continue
		if previous_conformation == conformation:
			conformation = previous_conformation
			protein_coordinates = previous_coordinates
			continue
		else:
			if calcul_energy(conformation) <= energy:
				print(energy)
				energy = calcul_energy(conformation)
				print(energy)
			else:
				new_energy = calcul_energy(conformation)
				prob = rd.uniform(0,1)
				if prob > math.exp(-(new_energy - energy)/TEMPERATURE):
					energy = new_energy
				else:
					conformation = previous_conformation
					protein_coordinates = previous_coordinates
		for aa in conformation:
			print(aa.coordinates)
		print("\n")


def calcul_energy(conformation):
	energy = 0
	hydrophobic_coordinates = set()
	for res in conformation:
		if res.polarity == "H":
			hydrophobic_coordinates.add(copy.deepcopy(tuple(res.coordinates)))
	for n, res in enumerate(conformation):
		if res.polarity == "P":
			continue
		if tuple(res.coordinates) not in hydrophobic_coordinates:
			continue
		else:
			if n == 0:
				neighbour_res2 = conformation[n + 1]
			elif n == len(conformation) - 1:
				neighbour_res1 = conformation[n - 1]
			else:
				neighbour_res1 = conformation[n - 1]
				neighbour_res2 = conformation[n + 1]
			neighbour_coordinates = [[res.coordinates[0] + 1, res.coordinates[1]], [res.coordinates[0] - 1,
				res.coordinates[1]], [res.coordinates[0], res.coordinates[1] + 1], [res.coordinates[0], res.coordinates[1] - 1]]
			print(neighbour_coordinates)
			for coordinates in neighbour_coordinates:
				if n == 0:
					if tuple(coordinates) in hydrophobic_coordinates and coordinates != neighbour_res2.coordinates:
						energy -= 1
						hydrophobic_coordinates.remove(tuple(coordinates))
				elif n == len(conformation) - 1:
					if tuple(coordinates) in hydrophobic_coordinates and coordinates != neighbour_res1.coordinates:
						energy -= 1
						hydrophobic_coordinates.remove(tuple(coordinates))
				else:
					if tuple(coordinates) in hydrophobic_coordinates and coordinates != neighbour_res1.coordinates and coordinates != neighbour_res2.coordinates:
						energy -= 1
						hydrophobic_coordinates.remove(tuple(coordinates))
		hydrophobic_coordinates.remove(tuple(res.coordinates))
	return energy
			
	

import random as rd
import copy

def MCsearch(step, conformation, protein_coordinates):
	for i in range(step):
		current_res = rd.choice(conformation)
		previous_conformation = copy.deepcopy(conformation)
		if current_res == conformation[0]:
			current_res.end_move(conformation[1], protein_coordinates)
		elif current_res == conformation[-1]:
			current_res.end_move(conformation[-2], protein_coordinates)
		else:
			rd.choice(current_res.corner_move(conformation, protein_coordinates), 
			current_res.crankshaft_move(conformation[current_res.number -3:current_res.number + 4], protein_coordinates))

			# if crankshaft > 3
	

import copy

"""
Any live cell with two or three neighbors survives.

Any dead cell with three live neighbors becomes a live cell.

All other live cells die in the next generation. Similarly, all other dead cells stay dead.
"""

def get_matrix(m, n):
	return [[0 for i in range(n)] for j in range(m)]
	
def pretty_print(matrix):
	for row in matrix:
		print row

def get_valid_neighbors(matrix, i, j):
	neighbors = [(i-1, j), (i+1, j), (i-1, j-1), (i, j-1),(i+1, j-1), (i-1, j+1), (i,j+1), (i+1, j+1)]
	
	for check, _ in enumerate(neighbors):
		if neighbors[check][0] < 0 or neighbors[check][0] > len(matrix)-1:
			continue
		if neighbors[check][1] < 0 or neighbors[check][1] > len(matrix[0])-1:
			continue
		if neighbors[check][0] == i and neighbors[check][1] == j:
			continue
		yield neighbors[check]
		
		
def get_live_neighbor_count(matrix, i, j):
	neighbors = get_valid_neighbors(matrix, i, j)
	
	living_neighbors_count = 0
	for neighbor in neighbors:
		if matrix[neighbor[0]][neighbor[1]] == 1:
			living_neighbors_count += 1
	return living_neighbors_count
		
def apply_rules(shadow_matrix, matrix, i, j):
	
	living_neighbors = get_live_neighbor_count(matrix, i, j)
	if living_neighbors < 2:
		shadow_matrix[i][j] = 0
	elif living_neighbors == 3:
		shadow_matrix[i][j] = 1
	elif living_neighbors > 3:
		shadow_matrix[i][j] = 0
		
def play_game(matrix, initial_cells):
	shadow_matrix = get_matrix(3, 3)
	for cel in initial_cells:
		matrix[cel[0]][cel[1]] = 1
		shadow_matrix[cel[0]][cel[1]] = 1
	print "Initial state of board:"
	pretty_print(matrix)
		
	ticks = 6
	for tick in range(ticks):
		for row_index, _ in enumerate(matrix):
			for cell_index, _ in enumerate(matrix[row_index]):
				apply_rules(shadow_matrix, matrix, row_index, cell_index)
		print "Board after round " + str(tick) + ": "
		pretty_print(shadow_matrix)
		matrix = copy.deepcopy(shadow_matrix)
				
		
def main():
	matrix = get_matrix(3, 3)
	initial_cells = [(1,1), (0, 1), (2, 1)]
	play_game(matrix, initial_cells)
	print "Final board state:"
	pretty_print(matrix)

if __name__== "__main__":
	main()

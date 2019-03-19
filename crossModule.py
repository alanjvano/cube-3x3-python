# Currently in progress

import cube_info
import cubeModule

import math
import copy

# definitions
cross_sol = []

# Checks to see if cross is solved
# note: color uses numeric value (0-5)
def findCrossEdges(color, cube_in):
	pos = []

	# identify location of edge pieces
	for i in range(len(cube_info.edges)):
		for each in cube_info.edges[i]:
			if cube_in.cube[each] == color:
				pos.append([each, cube_info.edges[i]])

	return pos

def findSlice(position):
	for i in range(4):
		if edges[i].includes(position):  	# upper slice
			return 0
	
	for i in range(4,8): 
		if edges[i].includes(position):		# middle slice
			return 1
	
	else:
		return 2 							#bottom slice


# find target location for each cross edge piece
def findCrossTargets(edg_loc, cube_in):
	# locate the target of each cross edge piece in order	
	target = []
	for each in edg_loc:
		for index in cube_info.edges:

			tmp_target = [cube_info.solved[index[0]], cube_info.solved[index[1]]] 
			tmp = [cube_in.cube[each[1][0]], cube_in.cube[each[1][1]]]

			print("tmp_target", tmp_target, "tmp", tmp)

			if tmp_target == tmp or tmp_target == tmp.reverse():
				for both in index:
					if cube_in.cube[each[0]] == cube_info.solved[both]:
						target.append(both)
	return target

def sameSide(position, target):
	for i in range(len(cube_info.faces)):
		if faces[i] in math.floor(position/9) and faces[i] in math.floor(target/9): 
			return true
	return false

def solveEdge(position, target, cube_in):
	# first, determine which slice position and target are in
	pos_slice = findSlice(position)
	# target slice should always be on the bottom
	
	# first rotate target edge to front side
	
		

	# case 1: edge is on same slice
	if pos_Slice == 2:
		print('same slice')

		# see if on same side
		if this.sameSide(position, target):
			print('same side')
		else:
			# need to flip edge
			print('flip edge')

	elif pos_slice == 1:
		# case 2: edge is on middle slice
		print('middle slice')


	else: 
		# case 3: edge is on opposite, upper slice
		
		# first rotate upper slice until edge is above corresponding cross piece
		if target == 3 or target == 5:
			permutation = 'U'
			while pos != target - 45:
				cross_sol.append(permutation)
				pos, target = updateCross(pos, target, permutation)
				

def updateCross(pos, target, permutation):
	# create temporary cube to modify
	tmp_cube = cubeModule.cube()
	tmp_cube.cube[pos] = 'pos'
	tmp_cube.cube[target] = 'tar'
	
	# modify cube with given permutation
	tmp_cube.perm(permutation)
	
	# return updated pos and target
	return tmp_cube.index('pos'), tmp_cube.index('tar')
		
			

def solveCross(color, cube_in_orig):
	
	# While the cross is unsolved, check each cross edge position
	# If a cross edge is in the incorrect location, solve it, then repeat

	# make copy of original cube
	cube_in = copy.deepcopy(cube_in_orig)
	
	# find cross edges
	edg_pos = findCrossEdges(color, cube_in)
	
	# find corresponding targets
	target = findCrossTargets(edg_pos, cube_in)
	print("target",target)
	
	edg = []
	for i in range(len(edg_pos)):
		edg.append(edg_pos[i][0])

	print("edg", edg)

	while (edg != target):
		
		for i in range(len(edg_pos)):
			if edg_pos[i][0] != target[i]:
				# solve edge piece
				print("solve edge")
				
		# find new current cross edge locations
		edg_pos = findCrossEdges(color, cube_in)
		target = findCrossTargets(edg_pos, cube_in)
		edg = []	
		for i in range(len(edg_pos)):
			edg.append(edg_pos[i][0])
	
	print("cross solved")
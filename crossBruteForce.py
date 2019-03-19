# solves the cross by brute force
# Note: every cross can be solved in 8 moves are less
# while the vast majority can be solved in 6 moves or less

import cubeModule
import cube_info
import copy

poss_turn = ['u','l','f','r','b','d','m','e','s',
			'U','L','F','R','B','D','M','E','S',
			'u2','l2','f2','r2','b2','d2','m2','e2','s2']
			
def forceCross(cube_in):
	cube2 = cubeModule.Cube()
	orig = cubeModule.Cube()
	orig.cube = copy.deepcopy(cube_in.cube)
	cube2.cube = copy.deepcopy(cube_in.cube)
	cube2.show()
	for length in range(5):
		iteration = [i for i in poss_turn]
		for j in range(length):
			iteration = [j+i for i in poss_turn for j in iteration]
		#print(iteration)
		for k in range(len(iteration)):
			cube2.cube = copy.deepcopy(orig.cube)
			#print(iteration[k])
			cube2.perm(iteration[k])
			#print(cube_in.checkState())
			if cube2.checkState():
				return iteration[k]
			
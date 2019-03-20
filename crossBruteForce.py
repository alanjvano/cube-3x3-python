# solves the cross by brute force
# Note: every cross can be solved in 8 moves are less
# while the vast majority can be solved in 6 moves or less

import cubeModule
import cube_info
import copy
import time

poss_turn = ['u','l','f','r','b','d',
			'U','L','F','R','B','D',
			'u2','l2','f2','r2','b2','d2']
			
def forceCross(cube_in):
	
	if checkCross(cube_in.cube):
		return []
	
	start_time = time.time()
	cube2 = cubeModule.Cube()
	orig = cubeModule.Cube()
	orig.cube = copy.deepcopy(cube_in.cube)
	cube2.cube = copy.deepcopy(cube_in.cube)
	#cube2.show()
	for length in range(5):
		iteration = [i for i in poss_turn]
		for j in range(length):
			iteration = [j+i for i in poss_turn for j in iteration]
		#print(iteration)
		for k in range(len(iteration)):
			cube2.cube = copy.deepcopy(orig.cube)
			#print(iteration[k])
			cube2.perm(iteration[k], False)
			#print(cube_in.checkState())
			if checkCross(cube2.cube):
				print("--- %s seconds ---" % (time.time() - start_time))
				return iteration[k]
			
def checkCross(cube):
	for i in [46, 48, 50, 52]:
		if cube[i] != 5:
			return False
	if (cube[16] != 1 or cube[25] != 2 or cube[34] != 3 or cube[43] != 4):
		return False
	return True
			
			
			
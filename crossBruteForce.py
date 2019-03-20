# solves the cross by brute force
# Note: every cross can be solved in 8 moves are less
# while the vast majority can be solved in 6 moves or less

import cubeModule
import cube_info
import copy
import time

poss_turn = ['u','l','f','r','b',
			'U','L','F','R','B',
			'U2','L2','R2','F2','B2']
			
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
			
			# check for any single edge solved
			if [cube2.cube[46], cube2.cube[25]] == [5,2] and 'f' in poss_turn:
				poss_turn.remove('F')
				poss_turn.remove('f')
				poss_turn.remove('F2')
				while cube2.cube[21] == 5 or cube2.cube[14] == 5:
					cube2.perm('luL')
				while cube2.cube[23] == 5 or cube2.cube[30] == 5:
					cube2.perm('Rur')
				orig.cube = copy.deepcopy(cube2.cube)
				print("removed f")
				cube2.show()
			
			if [cube2.cube[48], cube2.cube[16]] == [5,1] and 'l' in poss_turn:
				poss_turn.remove('L')
				poss_turn.remove('l')
				poss_turn.remove('L2')
				while cube2.cube[21] == 5 or cube2.cube[14] == 5:
					cube2.perm('luL')
				while cube2.cube[23] == 5 or cube2.cube[30] == 5:
					cube2.perm('Rur')
				orig.cube = copy.deepcopy(cube2.cube)
				print("removed l")
				cube2.show()
			
			if [cube2.cube[50], cube2.cube[34]] == [5,3] and 'r' in poss_turn:
				poss_turn.remove('R')
				poss_turn.remove('r')
				poss_turn.remove('R2')
				while cube2.cube[21] == 5 or cube2.cube[14] == 5:
					cube2.perm('luL')
				while cube2.cube[23] == 5 or cube2.cube[30] == 5:
					cube2.perm('Rur')
				orig.cube = copy.deepcopy(cube2.cube)
				print("removed r")
				cube2.show()
			
			if [cube2.cube[52], cube2.cube[43]] == [5,4] and 'b' in poss_turn:
				poss_turn.remove('B')
				poss_turn.remove('b')
				poss_turn.remove('B2')
				while cube2.cube[21] == 5 or cube2.cube[14] == 5:
					cube2.perm('luL')
				while cube2.cube[23] == 5 or cube2.cube[30] == 5:
					cube2.perm('Rur')
				orig.cube = copy.deepcopy(cube2.cube)
				print("removed b")
				cube2.show()
			
			print(poss_turn)
			
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
			
			
			
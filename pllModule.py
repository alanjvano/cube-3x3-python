import cube_info
import cubeModule

import copy

# define pll algorithms
oll_alg = ['M2UM2U2M2UM2','R2uruRURURuR','rUrururURUR2','M2MU2M2U2MUM2','rFrB2RfrB2R2',
		'RbRF2rBRF2R2','rUlD2LuRlUrD2RuL','rURuR2fuFURFrfR2','FLU2rkyrUlU2RuL','ruRUdR2UrURuRuR2D',
		'luLULuflulULFuLU2l','Y2RUrF2dLulUldF2U2','lUrU2LuRUlUrU2LuR','RUrfRUrurFR2uru','LuRU2lUrLuRu2lUr',
		'rUlU2RuLrUlU2RuL','RU2rU2bruRURBR2U','rU2RU2rFRUrurfR2','RUrurFR2uruRUrf','rUrubrB2ubUbRBR',
		'FRuruRUrfRUrurFRf']
		
# define positions of upper color pieces to match with oll case
pll_pos = [[[9,11,28],[10,27,29],[18,20,37],[19,36,38]],
		[[9,11,37],[10,27,29],[18,19,20],[28,36,38]],
		[[9,11,28],[18,19,20],[27,29,37],[10,36,38]],
		[[9,11,37],[10,36,38],[18,20,28],[19,27,29]],
		[[9,20,37],[10,11,27],[18,19,29],[28,36,38]],
		[[9,10,29],[11,19,36],[18,20,28],[27,37,38]],
		[[9,29,37],[10,20,36],[11,19,27],[18,28,38]],
		[[9,29,37],[10,27,38],[11,28,36],[18,19,20]],
		[[9,28,29],[10,27,38],[11,19,36],[18,20,37]],
		[[9,11,37],[10,20,36],[18,28,29],[29,27,38]],
		[[9,10,29],[11,28,36],[18,20,37],[19,27,38]],
		[[9,10,20],[11,19,36],[18,28,38],[27,29,37]],
		[[9,10,20],[11,36,37],[18,19,38],[27,28,29]],
		[[9,10,11],[18,28,29],[19,20,36],[27,37,38]],
		[[9,28,29],[10,11,27],[18,37,38],[19,20,36]],
		[[9,10,29],[11,27,28],[18,19,38],[20,36,37]],
		[[9,10,20],[11,19,27],[18,29,37],[28,36,38]],
		[[9,29,37],[10,11,36],[18,20,28],[19,27,38]],
		[[9,11,28],[10,20,37],[18,19,29],[27,37,38]],
		[[9,29,37],[10,11,27],[18,19,38],[20,28,36]],
		[[9,28,29],[10,20,36],[11,27,37],[18,19,38]]]
		
def solveOLL(cube_in):
	print(cube_in)
	tmp_cube = cubeModule.Cube()
	tmp_cube.cube = copy.deepcopy(cube_in.cube)
	print(tmp_cube)
	
	# loop through all possible oll cases for each of the four positions of the top layer
	found = False
	top_color = tmp_cube.cube[4]
	while found == False:
		
		orient = []
		for i in [0,1,2,3,4,5,6,7,8,9,10,11,18,19,20,27,28,29,36,37,38]:
			if tmp_cube.cube[i] == top_color:
				orient.append(i)
		print("orient",orient)
		
		# first check if already solved
		if orient != [0,1,2,3,4,5,6,7,8]:
			for pattern in range(len(oll_pos)):
				print(oll_pos[pattern])
				count = 0
				for each in orient:
					print(each)
					if each in oll_pos[pattern]:
						count += 1
				if count == 9:
					#oll_sol = oll_alg[pattern]
					print("success")
					tmp_cube.perm(oll_alg[pattern], True)
					found = True
					continue
		
		else:
			oll_sol = []
			found = True
		
		if found == False:
			tmp_cube.perm('U', True)
		
	return tmp_cube.sol, tmp_cube
		
		
			
		
		
		#for pattern in range(len(oll_pos)):
		
		

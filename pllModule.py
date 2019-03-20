import cube_info
import cubeModule

import copy
import math

# define pll algorithms
pll_alg = ['M2UM2U2M2UM2','R2uruRURURuR','rUrururURUR2','M2MU2M2U2MUM2','rFrB2RfrB2R2',
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
		[[9,11,19],[10,20,36],[18,29,37],[27,28,38]],
		[[9,10,20],[11,36,37],[18,19,38],[27,28,29]],
		[[9,10,11],[18,28,29],[19,20,36],[27,37,38]],
		[[9,28,29],[10,11,27],[18,37,38],[19,20,36]],
		[[9,10,29],[11,27,28],[18,19,38],[20,36,37]],
		[[9,10,20],[11,19,27],[18,29,37],[28,36,38]],
		[[9,29,37],[10,11,36],[18,20,28],[19,27,38]],
		[[9,11,28],[10,20,37],[18,19,29],[27,37,38]],
		[[9,29,37],[10,11,27],[18,19,38],[20,28,36]],
		[[9,28,29],[10,20,36],[11,27,37],[18,19,38]]]
		
def solvePLL(cube_in):
	#print(cube_in)
	tmp_cube = cubeModule.Cube()
	tmp_cube.cube = copy.deepcopy(cube_in.cube)
	#print(tmp_cube)
	
	# loop through all possible pll cases for each of the four positions of the top layer
	found = False
	top_color = tmp_cube.cube[4]
	while found == False:
	
		#tmp_cube.show()
		
		# create 2-d array to represent current state of top layer
		possible_pos = [9,10,11,18,19,20,27,28,29,36,37,38]
		current = []
		for index in range(len(possible_pos)):
			#print("index",possible_pos[index],"color",tmp_cube.cube[possible_pos[index]])
			current.append(tmp_cube.cube[possible_pos[index]])
		
		#print(current)
			
		# first check is already solved
		if current == [1,1,1,2,2,2,3,3,3,4,4,4]:
			pll_sol = []
			found = True
		
		# see if the corresponding position lists match
		if found == False:
			for index in range(len(pll_pos)):
				#print(pll_pos[index])
				count = 0
				for each in pll_pos[index]:
					#print(each)
					each_color = []
					for j in range(len(each)):
						each_color.append(tmp_cube.cube[each[j]])
					print(each_color)
					
					# check if all elements are equal
					if each_color.count(each_color[0]) == len(each_color):
						count += 1
				
				# see if its a match
				if count == 4:
					print("success")
					print(pll_pos[index])
					tmp_cube.perm(pll_alg[index], True)
					print(pll_alg[index])
					found = True
					continue
	
		print('**********************************')
		
		if found == False:
			tmp_cube.perm('U', True)
		
	print("done 3")
	return tmp_cube.sol, tmp_cube
		
		
			
		
		
		#for pattern in range(len(oll_pos)):
		
		

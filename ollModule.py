import cube_info
import cubeModule

import copy

# define oll algorithms
oll_alg = ['RU2R2FRfU2rFRf','FRUrufFSRUrufs','mUrMU2RmUrUr2rM','rU2XrURuYrurUrF','rMU2RUrURm',
		'LMU2luLulm','FrfRU2RU2r','RU2rU2rFRf','ruRurUrFRfUR','rmU2RUrURURrM',
		'RuruRurU2fUFuRUr','FRUrufUFRUruf','FURuR2fRURur','rFRUrfRyRur','rMuRmruRUrMuRm',
		'LMUlmLUluLMulm','RUrUrFRfU2rFRf','RU2R2FRfU2mURurM','rU2FRUruyR2U2RB','R2U2rF2U2R2fR2U2F2RU2R2u',
		'RUrURurURU2r','RU2R2uR2uR2U2R','R2dRU2rDRU2R','LFrflFRf','rflFRfLF',
		'rULuRUl','RUrURU2r','FRUrufU2FRUruf','MURUrurFRfm','R2UrbRuR2URBr',
		'luBULulbL','RUburURBr','RUrurFRf','RUR2urFRURuf','RU2R2FRfRU2r',
		'ruRurURURYrfR','RbrBUBub','LUlULululBLb','LfluLUFul','rFRUrufUR',
		'RurU2RUYRuryur','ruRUFRUrurURuf','burURB','FSRUrufs','FRUruf',
		'rurFRfUR','fluLUluLUF','FRUruFRruf','RbR2FR2BR2fR','RbRBR2U2FrfR',
		'FURurURurf','ruRurUfUFR','FRUrufRUrurFRf','RmUrURurURu2rM','RU2R2uRurU2FRf',
		'LFlURurURurLfl','RUrumURurM']
		
# define positions of upper color pieces to match with oll case
oll_pos = [[4,37,19,9,10,11,36,37,38],[4,9,10,11,19,20,28,36,37],
		[4,2,37,38,28,19,20,10,11],[4,2,37,27,28,18,19,9,10],
		[4,5,7,8,37,38,28,10,11],[3,4,6,7,9,36,37,27,28],
		[1,3,4,6,38,28,29,19,20],[1,4,5,8,18,19,9,10,36],
		[1,4,5,6,9,10,19,27,36],[1,3,4,8,11,19,28,29,38],
		
		[0,3,4,7,37,28,29,20,11],[2,4,5,7,37,27,18,9,10],
		[3,4,5,6,37,38,29,19,20],[3,4,5,8,36,37,9,18,19],
		[3,4,5,8,9,19,27,36,37],[3,4,5,6,9,19,27,36,37],
		[0,4,8,10,11,19,28,36,37],[2,4,8,9,10,11,19,28,37],
		[0,2,4,10,11,19,27,28,37],[0,2,4,6,8,10,19,28,37],
		
		[1,3,4,5,7,9,11,27,29],[1,3,4,5,7,9,11,20,36],
		[1,3,4,5,6,7,8,36,38],[1,2,3,4,5,7,8,18,38],
		[0,1,3,4,5,7,8,11,36],[1,3,4,5,7,8,9,18,36],
		[1,3,4,5,6,7,20,29,38],[0,1,2,3,4,6,8,19,28],
		[0,2,3,4,7,11,27,28,37],[0,2,4,5,7,10,11,27,37],
		
		[0,3,4,6,7,20,28,36,37],[2,4,5,7,8,10,18,37,38],
		[2,3,4,5,8,18,19,37,38],[3,4,5,6,8,9,19,29,37],
		[0,4,5,7,8,10,18,29,37],[0,3,4,7,8,18,28,29,37],
		[2,3,4,6,7,27,28,37,38],[2,4,5,6,7,9,10,20,37],
		[2,3,4,5,6,19,27,37,38],[0,3,4,5,8,11,19,36,37],
		
		[0,2,4,5,7,10,18,20,37],[0,2,3,4,7,18,20,28,37],
		[0,3,4,6,7,27,28,29,37],[2,4,5,7,8,9,10,11,37],
		[2,3,4,5,8,9,11,19,37],[0,1,4,6,7,10,27,28,29],
		[1,4,5,10,18,19,27,29,38],[1,3,4,9,11,19,20,28,36],
		[3,4,7,18,27,28,29,37,38],[4,5,7,9,10,11,20,36,37],
		
		[3,4,5,18,19,27,29,37,38],[1,4,7,10,18,27,28,29,38],
		[1,3,4,9,11,19,27,28,29],[1,4,5,9,10,11,19,27,29],
		[1,4,7,9,10,11,27,28,29],[3,4,5,9,11,20,27,29,37],
		[0,2,3,4,5,6,8,19,37]]
		
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
				count = 0
				for each in orient:
					if each in oll_pos[pattern]:
						count += 1
				if count == 9:
					#oll_sol = oll_alg[pattern]
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
		
		

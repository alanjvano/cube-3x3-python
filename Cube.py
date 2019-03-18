class Cube:

	def __init__(self):
		# define solved cube as single row matrix
		# white:0, orange:1, green:2, red:3, blue:4, yellow:5
		self.cube = [None] * 54
		self.state = True
		Self.sol = []
		for i in range(0,6):
			for j in range (0,9):
				self.cube[i*9+j] = i
	
	# check state to see if solved
	def checkState():
		self.state = True
		
		for i in range(0,6):
			for j in range(0,9):
				if (self.cube[i*9+j] != i):
					self.state = False
		
		return self.state
		
	
	def scramble(scr_len):
		# randomly select face permutation from valid list
		valid = valid_perm
		scr = []
		
		for i in range(0, scr_len):
			
			# if scramble not empty, remove previous permutation from valid list
			if (len(scr) != 0):
				index = valid.index(prev)
				valid.remove(index)
			
			# choose random valid permutation and add to permutation list
			tmp = random.randint(0,len(scr)-1))
			scr.append(valid[tmp])
			prev = valid[tmp]

			# pick random direction: clockwise, counterclockwise, or double
			tmp = random.randint(0,2)
			if (tmp == 0)
				scr[len(scr)-1] = scr[len(scr)-1].upper()
			elif: (tmp == 1)
				scr[len(scr)-1] = scr[len(scr)-1].upper() += "2"
			else: 
				scr[len(scr)-1] = scr[len(scr)-1].lower()

			# reset permutaion list
			valid = valid_perm			
		}

		scr = ''.join(scr)
		print("scramble", scr)
		return scr
	}

	def reset():
		for i in range(0,6):
			for j in range(0,9):
				self.cube[i*9+j] = i
				

# an inverse operation essentially undoes a permutation
# for example: (XY)^-1 = Y'X'
	def inverse(p_str):
		per = self.splitPerm(p_str)
		inverse = [None]*len(per)
		print("per", per)
		for i in range(len(per),0,-1):
			# reverse order
			print(per[i])
			inverse[len(per)-i] = per[i-1]
			# reverse direction
			inverse[len(per)-i][1] = !(per[i-1][1])
		}
		print('inverse',inverse)
		return inverse
		

# split permutation sequence into individual chars and push them to array
	def splitPerm(p_str):
		p = []
		for i in range(0,len(p_str)):
			
			# if single turn
			if (p_str[i+1] % len(p_str) != '2'):
				# check upper case
				tmp = (p_str[i] == p_str[i].upper())
				
				# output [face, direction (1 = c, 0 = cc), doubleturn (1 yes)]
				p.append([p_str.[i].lower(), tmp, 0])
				
			# if double turn, then add next character as well
			# and increment counter
			else:
				p.append([p_str.[i].lower(), 1, 1])
				i += 1
				
		print('p', p)

		return p
		
		
	def perm(p_str):
	
		p = self.splitPerm(p_str)

		# check for invalid input
		for i in range(0,len(p)):
			if (p[i][0] not in valid_perm and p[i][0] not in valid_rot):
				print("not valid input")
				return false
	
		# implement turn sequence in order	
		for each in p:
		
			print(each)			

			# implement single turn
			if (each[0] in valid_perm):
				self.cube = self.turn(each, self.cube)
			else:
				self.cube = self.rotate(each)
				

	def rotate(dir):
		# def buffer cycle to adjust
		cycle = rots[dir[0]]

		# flip direction if necessary
		if (dir[1] == 0 and dir[2] == 0):
			cycle = self.inverse(cycle)
		else:
			cycle = self.splitPerm(cycle) 

		print("rotation cycle", cycle)

		for i in range(0,dir[2]):
			for each in p:
				self.cube = self.turn(each, self.cube)
				
		return self.cube
		

	def turn(dir, cube):
		current = self.cube
		buffer = current
		cycle = perms[dir[0]]  # choose permutation cycle

		print("current", current)
		
		# for clockwise direction reverse permutation cycles
		if dir[1] == 1:
			for k in range(0,len(cycle)):
				cycle[k] = cycle[k].reverse()

		print("cycle", cycle)
		
		# rotate layer twice if double specified
		for i in range(0, len(cycle)):
			for j in range(0,len(cycle)):
				target = (j+1+dir[2])%4 	# (j == 3) ? 4 : (j+1)%4
				print('cube pos', cycle[i][j], 'target pos', cycle[i][target])
				
				z = current[(cycle[i][target])]
				buffer[cycle[i][j]] = z
					
		print(buffer)
		return buffer
		

	def show():
		

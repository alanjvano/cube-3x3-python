# cube methods
import cubeModule
import crossModule
import cube_info
import crossBruteForce
import f2lModule

import copy

def main():
	cube1 = cubeModule.Cube();
	exit = False;
	
	while (exit == False):
		print("\n\nMenu:")
		print("1 - permutate cube")
		print("2 - solve cube")
		print("3 - scramble cube")
		print("4 - show cube")
		print("5 - reset cube")
		print("6 - exit")
		
		# obtain user input
		sel = input(">> ")
		#os.system('clear')
		try:
			sel = int(sel)
		except ValueError:
			print("Must enter valid option")
			continue
			
		
		if (sel == 1):
			print("\n\nnote: to return to menu, enter invalid permutation")
			print("valid permutation:")
			print(cube_info.valid_perm)
			print("use upper case for clockwise, lower case for counter clockwise")
			print("use 2 for double turn")
			print("e.x.  f2UldSm2")
			seq = input("\n\nenter permutation sequence:")

			if cube1.perm(seq, False) == False:
				perm_exit = True			
				
			
		elif (sel == 2):
			print("solving...")
			cross_sol = crossBruteForce.forceCross(cube1)
			solved_cube = cubeModule.Cube()
			solved_cube = copy.deepcopy(cube1)
			solved_cube.perm(cross_sol, True)
			solved_cube = f2lModule.solveF2l(solved_cube)
			print("cross:", cross_sol)
			#print("solution",solved_cube.sl)
		
		elif (sel == 3):
			scr_length = input("enter scramble length: ")
			try:
				scr_perm = cube1.scramble(int(scr_length))
				cube1.perm(scr_perm, False)
				print("\ncube scrambled...")
				print("\nscramble:",scr_perm,"\n");

			except TypeError:
				print("must enter integer!")
			
		elif (sel == 4):
			if cube1.checkState():
				state = "solved"
			else:
				state = "unsolved"
			print("\ncurrent state: ", state)
			print("note: 0=white, 1=orange, 2=green, 3=red, 4=blue, 5=yellow") 
			cube1.show()
			
		elif (sel == 5):
			cube1.reset()
			print("\ncube reset...")
			
		elif (sel == 6):
			print("exit")
			exit = True;
			
		else:
			print("not valid input")

if __name__ == "__main__":
	main()


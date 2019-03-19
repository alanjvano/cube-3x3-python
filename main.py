# cube methods
import cubeModule
import crossModule
import cube_info

def main():
	cube1 = cubeModule.Cube();
	exit = False;
	
	while (exit == False):
		print("\n\nMenu:")
		print("1 - permutate cube")
		#print("2 - solve cube")
		print("2 - scramble cube")
		print("3 - show cube")
		print("4 - reset cube")
		print("5 - exit")
		
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
			perm_exit = False
			while perm_exit != True:
				seq = input("\n\nenter permutation sequence:")
				print("\n")
				if cube1.perm(seq) == False:
					perm_exit = True
					
				print("\nto exit, enter 1...")
			
				
			
		#elif (sel == 2):
		#	print("solving...")
		#	crossModule.solveCross(5, cube1)
		
		elif (sel == 2):
			scr_length = input("enter scramble length: ")
			try:
				scr_perm = cube1.scramble(int(scr_length))
				cube1.perm(scr_perm)
				print("\ncube scrambled...")
				print("\nscramble:",scr_perm,"\n");

			except TypeError:
				print("must enter integer!")
			
		elif (sel == 3):
			if cube1.checkState():
				state = "solved"
			else:
				state = "unsolved"
			print("\ncurrent state: ", state)
			print("note: 0=white, 1=orange, 2=green, 3=red, 4=blue, 5=yellow") 
			cube1.show()
			
		elif (sel == 4):
			cube1.reset()
			print("\ncube reset...")
			
		elif (sel == 5):
			print("exit")
			exit = True;
			
		else:
			print("not valid input")

if __name__ == "__main__":
	main()


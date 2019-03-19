# cube methods
import cubeModule
import cube_info

def main():
	cube1 = cubeModule.Cube();
	exit = False;
	
	while (exit == False):
		print("\n\nMenu:")
		print("1 - permutate cube")
		print("2 - solve cube")
		print("3 - scramble cube")
		print("4 - show cube")
		print("5 - exit")
		
		# obtain user input
		sel = int(input(">> "))
		#os.system('clear')
		print("")
		
		if (sel == 1):
			print("note: to return to menu, enter invalid permutation")
			perm_exit = False
			while perm_exit != True:
				seq = input("enter permutation sequence:")
				if cube1.perm(seq) == False:
					perm_exit = True
				
			
		elif (sel == 2):
			print("solve")
		
		elif (sel == 3):
			scr_length = input("enter scramble length: ")
			try:
				cube1.scramble(int(scr_length))
				print("\ncube scrambled...\n")

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
			print("exit")
			exit = True;
			
		else:
			print("not valid input")

if __name__ == "__main__":
	main()


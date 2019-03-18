import math

# cube methods
import Cube.py

cols = 12
rows = 9
gridSize = 60
valid_perm = ["u","l","f","r","b","d","m","e","s"]
valid_rot = ["x","y","z"]

# define permutation cycles for face turns
perms = {
	'u': [[0,2,8,6],[1,5,7,3],[38,29,20,11],[37,28,19,10],[36,27,18,9]],
	'l': [[9,11,17,15],[10,14,16,12],[0,18,45,44],[3,21,48,41],[6,24,51,38]],
	'f': [[18,20,26,24],[19,23,25,21],[6,27,47,17],[7,30,46,14],[8,33,45,11]],
	'r': [[27,29,35,33],[28,32,34,30],[8,36,53,26],[5,39,50,23],[2,42,47,20]],
	'b': [[36,38,44,42],[37,41,43,39],[2,9,51,35],[1,12,52,32],[0,15,53,29]],
	'd': [[45,47,53,51],[46,50,52,48],[24,33,42,15],[25,34,43,16],[26,35,44,17]],
	'm': [[22,49,40,4],[19,46,43,1],[25,52,37,7]],
	'e': [[22,31,40,13],[21,30,39,12],[23,32,41,14]],
	's': [[4,31,49,13],[3,28,50,16],[5,34,48,10]]
}

# define permutations to rotate cube
rotations = {
	'x': "Rml",
	'y': "Ued",
	'z': "FSb"
}

# define twelve edge pairs by slice
edges =  [[1,37],[3,10],[5,28],[7,19],      #top slice
	     [12,41],[14,21],[23,30],[32,39],   #middle slice
	     [25,46],[16,48],[34,50],[43,52]]   #bottom slice

# define opposite faces
faces = [[0,5],[1,3],[2,4]]

#define array method to compare two arrays
#will be useful in future solution methods
# based on method proposed by Tomas Zato
#Array.prototype.isEqual = function(arr) {
#	//if array is just false, then return false
#	if (!arr) {
#		return false;
#	}
#
#	//check if lengths are equal
#	if (this.length != arr.length) {
#		return false;
#	}
#
#	//check to see if each index is equal
#	for (let i = 0; i < this.length; i++) {
#		//check for nested array
#		if (this[i] instanceof Array && arr[i] instanceof Array) {
#			for (let j = 0; j < this[i].length; j++) {
#				if (this[i][j] != arr[i][j]) {
#					return false;
#				}
#			}
#		} else if (this[i] != arr[i]) {
#}
#
#	return true;
#}

def main():
	#cube1 = Cube();
	exit = False;
	
	while (exit == False):
		print("Menu:")
		print("1 - permutate cube")
		print("2 - solve cube")
		print("3 - show cube")
		print("4 - exit")
		
		# obtain user input
		sel = int(input(">> "))
		#os.system('clear')
		print("")
		
		if (sel == 1):
			print("permutate")
			
		elif (sel == 2):
			print("solve")
			
		elif (sel == 3):
			print("show")
			
		elif (sel == 4):
			print("exit")
			exit = True;
			
		else:
			print("not valid input")

if __name__ == "__main__":
	main()


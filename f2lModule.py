import cube_info
import cubeModule

# define f2l algorithms
f2l_alg = [
	# Case 1: (1-8) corner and edge on top, cross corner oriented FR, same color on top face
	[URur],[FrfR],[uRUrU2Rur],[ruRFrfR],[uRU2rU2Rur],[rU2RFrfR],[RU2rURUR2FRf],[RurU2fuF],
	
	# Case 2: (9-16 corner and edge on top, cross corner FR, opposite color on top face
	[fuF],[RUr],[uRurUfuF],[uRUrURUr],[uRU2rUfuF],[fUFuRU2R2FRf],[UfUFufuF],[uRurURUr],
	
	# Case 3: (17-24) corner and edge on top, cross cross color facing up
	[RU2ruRUr],[rU2RURU2R2FRf],[URU2R2FRf],[ufU2F2rfR],[RurU2RUr],[FlU2LF],[U2R2U2ruRuR2],[RU2rfU2FU2fUF],
	
	# Case 4: (25-30) corner bottom layer, edge on top
	[URUrufuF],[ufuFURUr],[U2RurfuF],[RUruRUr],[RurURur],[RUruFrfR],
	
	# Case 5: (31-36) corner top layer, edge middle layer
	
	# Case 6: (36-41) corner bottom layer, edge middle layer
	
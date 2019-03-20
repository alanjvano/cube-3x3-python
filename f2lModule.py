import cube_info
import cubeModule

import copy

# define f2l algorithms
f2l_alg = [
	# Case 1: (1-8) corner and edge on top, cross corner oriented FR, same color on top face
	['URur'],['FrfR'],['uRUrU2Rur'],['ruRFrfR'],['uRU2rU2Rur'],['rU2RFrfR'],['RU2rURUR2FRf'],['RurU2fuF'],
	
	# Case 2: (9-16 corner and edge on top, cross corner FR, opposite color on top face
	['fuF'],['RUr'],['uRurUfuF'],['uRUrURUr'],['uRU2rUfuF'],['fUFuRU2R2FRf'],['UfUFufuF'],['uRurURUr'],
	
	# Case 3: (17-24) corner and edge on top, cross cross color facing up
	['RU2ruRUr'],['rU2RURU2R2FRf'],['URU2R2FRf'],['ufU2F2rfR'],['RurU2RUr'],['FlU2LF'],['U2R2U2ruRuR2'],['RU2rfU2FU2fUF'],
	
	# Case 4: (25-30) corner bottom layer, edge on top
	['URUrufuF'],['ufuFURUr'],['U2RurfuF'],['RUruRUr'],['RurURur'],['RUruFrfR'],
	
	# Case 5: (31-36) corner top layer, edge middle layer
        ['uRurU2Rur'],['URUrU2RUr'],['U2RurufuF'],['uRUrU2fuFuFrfR'],['RurfU2F'],['RUruRUruRUr'],
	
	# Case 6: (37-41) corner bottom layer, edge middle layer
        ['RuruRUrU2Rur'],['RUrU2RurURUr'],['fUFU2RUR2FRf'],['RurU2fuF2rfR'],['rFRfRurURurU2Rur']]

# define positions of 47 (corner) and 23 (edge piece) to match with f2l case
f2l_pos = [
        # Case 1
        [20,5],[27,19],[20,1],[27,10],[20,3],[27,37],[20,7],[27,28],
        # Case 2
        [20,10],[27,1],[20,37],[27,3],[20,28],[27,7],[20,19],[27,5],
        # Case 3
        [8,5],[8,19],[8,1],[8,10],[8,3],[8,37],[8,7],[8,28],
        # Case 4
        [47,19],[47,5],[26,19],[33,5],[26,5],[33,19],
        # Case 5
        [20,23],[27,23],[20,30],[27,30],[8,30],[8,23],
        # Case 5
        [26,23],[33,23],[26,30],[33,30],[47,30]]

# for each four corner pairs, find the location of the corresponding edge and corner piece
# then, based on their location implement the correct f2l algorithm
# rotate the cube until complete
def solveF2l(cube_in):
    tmp_cube = cubeModule.Cube()
    tmp_cube.cube = copy.deepcopy(cube_in.cube)
	
    for i in range(4):
        
        # set colors for pair based on cube position
        edge_color = tmp_cube.cube[22]
        side_color = tmp_cube.cube[31]
        corner_color = tmp_cube.cube[49]
        #cross_side1 = tmp_cube.cube[22]
        #cross_side2 = tmp_cube.cube[31]
        
        # find edge piece
        # first loop through all edge locations
        for pair in cube_info.edges:

            # if both colors are in the edge piece, set it to the current edge position
            if side_color in [tmp_cube.cube[pair[0]], tmp_cube.cube[pair[1]]]:
                if edge_color in [tmp_cube.cube[pair[0]], tmp_cube.cube[pair[1]]]:
                    if edge_color == tmp_cube.cube[pair[0]]:
						edge_pos = pair[0]
                    else:
						edge_pos = pair[1]
		
		print(edge_pos)

        for triple in cube_info.corners:

            # define temporary corner triple
            tmp_triple = []
            for j in range(len(triple)):
                tmp_triple.append(tmp_cube.cube[triple[j]])     

            if edge_color in tmp_triple:
                if side_color in tmp_triple:
                    if corner_color in tmp_triple:
                        for color in tmp_triple:

                            # if all three colors of corner are in corner piece, set it to the current corner position
                            if color == corner_color:
                                corner_pos = triple.index(corner_color)

        print("edge_pos",edge_pos,"corner_pos",corner_pos)
                    

        # find corner piece

        # permutate with corresponding algorithm

       

    
    

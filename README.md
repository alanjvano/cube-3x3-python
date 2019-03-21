# cube-3x3-python

The purpose of this project is to develop an algorithm to manipulate and solve a 3x3 Rubiks cube as quickly and efficiently as possible using python.

## Project Plan:
### 1. Implement basic framework.  [COMPLETE]
	* create cube as an object
	* permutate cube given input
	* represent cube in two dimensions
	* check state of cube
	* reset cube
	* scramble cube



### 2. Solve cube using simple method.
	* efficiency and speed not goal here
	* given any random scramble, find permuation sequence which will return cube to solved state

[NOTE]:
The cross method solution is currently unoptimized and only applies for cross solutions with five or less moves.  More detail in method description below.

[IN PROGRESS]

### 3. Optimize solving method
	* modify basic case to emulate Friedrich's Method (CFOP)
	* maybe implement Reduction Method
	* maybe implement Petrus Method

### 4. Implement 3D representation of cube.


## Basic Framework:

At least for the inital implementation of this case, each cube is an object so multiple variations can be followed in future steps.
Each cube is simply represented as a one-dimensional 54 element array in the format: 

> **[ U1, U2, U3... U8, L1,... F1,... R1,... B1, ..., D1,...]**

Here, the faces are represented by
* U = upper face
* L = left face
* F = front face
* R = right face
* B = back face
* D = lower face (down)

The cube visualized as follows, where each values represents the cube object's corresponding array indice:

-|U|-|-
:-----:|:-----:|:-----:|:-----:
L|F|R|B
-|D|-|-

-|-|-|0|1|2|-|-|-|-|-|-
:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:
-|-|-|3|4|5|-|-|-|-|-|-
-|-|-|6|7|8|-|-|-|-|-|-
9|10|11|18|19|20|27|28|29|36|37|38
12|13|14|21|22|23|30|31|32|39|40|41
15|16|17|24|25|26|33|34|35|42|43|44
-|-|-|45|46|47|-|-|-|-|-|-
-|-|-|48|49|50|-|-|-|-|-|-
-|-|-|51|52|53|-|-|-|-|-|-

A canonical cycle notations is used to define each clockwise permutation.  
To turn a face counter-clockwise, the permutation cycle is simply reversed.

Therefore, each face turn can be described by five four-mode cycle permutations of the cube elements:
* u: [[0,2,8,6],     [1,5,7,3],     [38,29,20,11], [37,28,19,10], [36,27,18,9]]
* l: [[9,11,17,15],  [10,14,16,12], [0,18,45,44],  [3,21,48,41],  [6,24,51,38]]
* f: [[18,20,26,24], [19,23,25,21], [6,27,47,17],  [7,30,46,14],  [8,33,45,11]]
* r: [[27,29,35,33], [28,32,34,30], [8,36,53,26],  [5,39,50,23],  [2,42,47,20]]
* b: [[36,38,44,42], [37,41,43,39], [2,9,51,35],   [1,12,52,32],  [0,15,53,29]]
* d: [[45,47,53,51], [46,50,52,51], [24,33,42,15], [25,34,43,16], [26,35,44,17]]

The Cube class is used to define a cube as an object.  This class handle basic cube manipulations including:
* perm() - this method accepts an input permutation sequence from the user and performs the permutations on the cube in order
* checkState() - this method tests to see if the cube is in a solved state
* show() - displays cube in 2d format on canvas
* scramble() - scrambles cube with randomly generated sequence
* reset() - set cube back to solved state
* inverse() - invert a permutation (e.x. (XY)^-1 == (Y^-1)(X^-1)
	    - essentialy just reverse the order and directions of a set of permutations
* splitPerm() - parse user input into usable information for perm
* rotate() - rotate cube along the X,Y,Z axis, behaves the same way as a permutation

## Simple Solution:

The first step of the simple solution is to solve the bottom cross.
Originally, each cross piece's location and its corresponding target location where determined.  Then the the position of the edge piece was matched to a certain 
case where it could be solved most efficiently.  However, the number of cases and permutations to consider led to different approaches.

The second implementation involves iterating through different permutations.  Now, the all the possible permutations up to five are iterated throug on the cube.
However, each time a single cross piece is found to be positioned correctly, that piece is fixed in place and all permutation which would affect that piece are removed from
the list of possible permutations, and then the process will repeat itself.  If the cube get stuck in the case where the last edge or two is positioned incorrectly and cannot
be solved with the available moves, its position on the top layer is switched.

Current solution:
Every cross on a rubiks cube can be solved in 8 moved or less, while most cross can be solved in 5 or 6 moves (around 5.5 moves on average).  Therefore,
the new plan to solved the cross involves simple brute forcing all the possible permutations up to eight moves.  This works well for cases that are five moves or less.
However, if the cross was a seven or eight moves case, with up to 18^8 possible difference cases to permutate and then check, this still needs optimizing.

To solve the first two layers of the cube (F2L), four pairs each consisting of an edge piece and corner piece must be solved.  In this program, these pairs are solved one at a 
time.  The program will first locate the positions of the edge and corner piece for the front right pair.  It will then reposition them so the corner is in the front right column and 
the edge is either on the top slice or front right column.  Then it will rotate through the top layer until its pattern matches one of 46 possible f2l cases.  After implementing
the appropriate algorithm the cube will rotate in the Y direction and repeat the process until all four pairs are solved.

The last two steps of solving the cube, OLL (orient last layer) and PLL (permutate last layer), were the most straitforward to implement.  There exist 57 possible OLL cases
and 21 possible PLL cases.  Therefore, for each step, the top layer is rotated until it matches on the OLL/PLL cases and then the appropriate algorithm is used.  
Given the widespread use of OLL and PLL in speed cubing, there already exits databases of the most efficient possible permutations to solve each case.  The algorithms
used here were found here:
[OLL Algorithms](https://www.speedsolving.com/wiki/index.php/OLL)
[PLL Algorithms](https://www.speedsolving.com/wiki/index.php/PLL)


There exist many ways to improve the efficiency and decrease the average moves per solve.  Currently, the cross solving algorithm has much room for improvement and by implementing
a dynamic method, perhaps the ideal solution could be found in each case.






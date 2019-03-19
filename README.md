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

[IN PROGRESS]

### 2. Solve cube using simple method.
	* efficiency and speed not goal here
	* given any random scramble, find permuation sequence which will return cube to solved state

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

The Cube.js prototype class is used to define a cube as an object.  This class handle basic cube manipulations including:
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
So the locations of the chosen cross edges (based on which color is chosen) are first found - the targets.
Then, the corresponding edges for each target position are found using their correspnding pairs - the current positions.

Basically, while the current positions and the target positions of the edges do not match, the program will loop through them and solve them one at a time.
For each edge piece, there are three possible cases:
1. The edge is located on the bottom slice
2. The edge is located on the middle slice
3. The edge is located on the upper slice









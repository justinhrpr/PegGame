# PegGame

Solve the peg game found at Cracker Barrel.

search.py is from the AIMA repository at https://github.com/aimacode/aima-python. 

PegGame.py will find all possible solutions of the peg game using breadth first search algorithm.

# Sample Output
```
***************starting position 0******************
number of solutions: 4

solution 1
3 jump 1 to 0
5 jump 4 to 3
0 jump 2 to 5
6 jump 3 to 1
9 jump 5 to 2
11 jump 7 to 4
12 jump 8 to 5
1 jump 4 to 8
2 jump 5 to 9
14 jump 9 to 5
5 jump 8 to 12
13 jump 12 to 11
10 jump 11 to 12


solution 2
3 jump 1 to 0
5 jump 4 to 3
0 jump 2 to 5
6 jump 3 to 1
9 jump 5 to 2
11 jump 7 to 4
13 jump 12 to 11
10 jump 11 to 12
12 jump 8 to 5
2 jump 5 to 9
14 jump 9 to 5
5 jump 4 to 3
1 jump 3 to 6


solution 3
3 jump 1 to 0
5 jump 4 to 3
0 jump 2 to 5
6 jump 3 to 1
9 jump 5 to 2
11 jump 7 to 4
13 jump 12 to 11
10 jump 11 to 12
12 jump 8 to 5
2 jump 5 to 9
14 jump 9 to 5
5 jump 4 to 3
3 jump 1 to 0


solution 4
3 jump 1 to 0
5 jump 4 to 3
0 jump 2 to 5
6 jump 3 to 1
9 jump 5 to 2
12 jump 7 to 3
1 jump 3 to 6
10 jump 6 to 3
14 jump 13 to 12
11 jump 12 to 13
13 jump 8 to 4
3 jump 4 to 5
2 jump 5 to 9
```
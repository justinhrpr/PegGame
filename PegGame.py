'''solve the peg game found at cracker barrel'''

import search

class PegGame(search.Problem):
    
    # board has 15 holes, 1 means a peg is in the hole
    init_board = (1,1,1,1,1,1,1,1,1,1,1,1,1,1,1)   
    # goal states are when only one peg remains
    # found a better way. see goal_test()
    # goals = [(1,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
    #          (0,1,0,0,0,0,0,0,0,0,0,0,0,0,0),   
    #          (0,0,1,0,0,0,0,0,0,0,0,0,0,0,0),   
    #          (0,0,0,1,0,0,0,0,0,0,0,0,0,0,0),   
    #          (0,0,0,0,1,0,0,0,0,0,0,0,0,0,0),   
    #          (0,0,0,0,0,1,0,0,0,0,0,0,0,0,0),   
    #          (0,0,0,0,0,0,1,0,0,0,0,0,0,0,0),   
    #          (0,0,0,0,0,0,0,1,0,0,0,0,0,0,0),   
    #          (0,0,0,0,0,0,0,0,1,0,0,0,0,0,0),   
    #          (0,0,0,0,0,0,0,0,0,1,0,0,0,0,0),   
    #          (0,0,0,0,0,0,0,0,0,0,1,0,0,0,0),   
    #          (0,0,0,0,0,0,0,0,0,0,0,1,0,0,0),   
    #          (0,0,0,0,0,0,0,0,0,0,0,0,1,0,0),   
    #          (0,0,0,0,0,0,0,0,0,0,0,0,0,1,0),   
    #          (0,0,0,0,0,0,0,0,0,0,0,0,0,0,1)]

    '''initialize the game. need to know the empty location'''
    def __init__(self, empty):
        # make a list() copy of the state 
        board = list(self.init_board)
        board[empty] = 0
        # update state
        self.board = tuple(board)
        super().__init__(self.board)

    def actions(self,state):
        '''find possible actions for a given state
           three requirements for valid move: 
           1. must be a peg in the hole 
           2. must be a peg next to the hole 
           3. must be open space for peg to land'''
        print('current board: ',state)
        a = [] # actions
        # check for action at every hole
        for hole,peg in enumerate(state):
            # 1. must be a peg in the hole
            if peg:
                # 2. must be a peg next to the hole
                # 3. must be open space for peg to land
                neighbors = self.valid_actions(hole, state)
                for n in neighbors:
                    a.append("%s jump %s to %s" % (hole,n[0],n[1]))
        print('possible actions: ',a,'\n')
        return a

    def valid_actions(self,hole, state):
        '''returns tuple of a hole to be jumped and landing hole'''
        n = []
        if hole == 0:
            if state[1] and not state[3]: n.append((1,3))
            if state[2] and not state[5]: n.append((2,5))
        if hole == 1:
            if state[3] and not state[6]: n.append((3,6))
            if state[4] and not state[8]: n.append((4,8))
        if hole == 2:
            if state[4] and not state[7]: n.append((4,7))
            if state[5] and not state[9]: n.append((5,9))
        if hole == 3:
            if state[1] and not state[0]: n.append((1,0))
            if state[4] and not state[5]: n.append((4,5))
            if state[7] and not state[12]: n.append((7,12))
            if state[6] and not state[10]: n.append((6,10))
        if hole == 4:
            if state[7] and not state[11]: n.append((7,11))
            if state[8] and not state[13]: n.append((8,13))
        if hole == 5:
            if state[4] and not state[3]: n.append((4,3))
            if state[2] and not state[0]: n.append((2,0))
            if state[8] and not state[12]: n.append((8,12))
            if state[9] and not state[14]: n.append((9,14))
        if hole == 6:
            if state[3] and not state[1]: n.append((3,1))
            if state[7] and not state[8]: n.append((7,8))
        if hole == 7:
            if state[4] and not state[2]: n.append((4,2))
            if state[8] and not state[9]: n.append((8,9))
        if hole == 8:
            if state[7] and not state[6]: n.append((7,6))
            if state[4] and not state[1]: n.append((4,1))
        if hole == 9:
            if state[5] and not state[2]: n.append((5,2))
            if state[8] and not state[7]: n.append((8,7))
        if hole == 10:
            if state[6] and not state[3]: n.append((6,3))
            if state[11] and not state[12]: n.append((11,12))
        if hole == 11:
            if state[7] and not state[4]: n.append((7,4))
            if state[12] and not state[13]: n.append((12,13))
        if hole == 12:
            if state[7] and not state[3]: n.append((7,3))
            if state[8] and not state[5]: n.append((8,5))
            if state[11] and not state[10]: n.append((11,10))
            if state[13] and not state[14]: n.append((13,14))
        if hole == 13:
            if state[8] and not state[4]: n.append((8,4))
            if state[12] and not state[11]: n.append((12,11))
        if hole == 14:
            if state[9] and not state[5]: n.append((9,5))
            if state[13] and not state[12]: n.append((13,12))
        return n

    def result(self, state, action):
        '''returns new state after action is applied to current state'''
        initial_hole = int(action.split()[0])
        jumped_peg = int(action.split()[2])
        final_hole = int(action.split()[4])
        # copy state into a list
        board = list(state)
        board[initial_hole] = 0
        board[jumped_peg] = 0
        board[final_hole] = 1
        # return tuple to update state
        return tuple(board)

    def goal_test(self, state):
        '''goal state is reached when the sum of state/board is 1 (only one peg left)'''
        if sum(state) == 1:
            return True
        else:
            return False



def main():
    # setup game
    game = PegGame(10)
    #print('initial board',game.board)
    # solved = search.depth_first_graph_search(game)
    solved = search.breadth_first_graph_search(game)
    [print(action) for action in solved.solution()]


if __name__ == '__main__':
    main()
import numpy as np
from collections import defaultdict
class Puzzle:

    def __init__(self):
        
        self.open = []
        self.closed = []
        self.dict = defaultdict(list)
        self.key_count = 0

    def generate_child(self,data):
        
        zero_location = [x[0] for x in np.where(data[0]==0)] 
        children = []

        # checking for feasible up move
        copy_state = data[0].copy()
        if (zero_location[0] != 0):
            swap_value = data[0][zero_location[0]-1,zero_location[1]]
            copy_state[zero_location[0]-1,zero_location[1]] = 0
            copy_state[zero_location[0],zero_location[1]] = swap_value
            child = [copy_state, data[1]+1, 0]
            children.append(child)

        # checking for feasible down move
        copy_state = data[0].copy()
        if (zero_location[0] != 2):
            swap_value = data[0][zero_location[0]+1,zero_location[1]]
            copy_state[zero_location[0]+1,zero_location[1]] = 0
            copy_state[zero_location[0],zero_location[1]] = swap_value
            child = [copy_state, data[1]+1, 0]
            children.append(child)

        # checking for feasible left move
        copy_state = data[0].copy()
        if (zero_location[1] != 0):
            swap_value = data[0][zero_location[0],zero_location[1]-1]
            copy_state[zero_location[0],zero_location[1]-1] = 0
            copy_state[zero_location[0],zero_location[1]] = swap_value
            child = [copy_state, data[1]+1, 0]
            children.append(child)

        # checking for feasible right move
        copy_state = data[0].copy()
        if (zero_location[1] != 2):
            swap_value = data[0][zero_location[0],zero_location[1]+1]
            copy_state[zero_location[0],zero_location[1]+1] = 0
            copy_state[zero_location[0],zero_location[1]] = swap_value
            child = [copy_state, data[1]+1, 0]
            children.append(child)

        return children

    def display(self,start):
        for i in start:
            for j in i:
                print(j,end=" ")
            print("")
 

    def h_mismatch_cost(self,start,goal):
        cost = np.sum(start[0]!= goal)
        return cost
        

    def a_star_traversal(self):
        start = np.array([0,1,3,4,2,5,7,8,6]).reshape(3,3)   
        goal = np.array([1,2,3,4,5,6,7,8,0]).reshape(3,3)

        self.dict[self.key_count].append(start)
        start = self.dict[self.key_count]
        self.dict[self.key_count].append(0)
        f_value = self.h_mismatch_cost(start,goal)+start[1]
        self.dict[self.key_count].append(f_value)
        
        self.open.append(self.dict[self.key_count])
        print("Initial")
        while True:
            state = self.open[0]
            print("")
            print("  ▲ ")
            print("  | ")
            print("  ▼ \n")
            self.display(state[0])
            
            if(np.array_equal(state[0],goal)):
                print("\nGoal")
                break
            for i in self.generate_child(state):
                i[2] = self.h_mismatch_cost(i,goal) + i[1]
                self.key_count+=1
                self.dict[self.key_count] = i;
                self.open.append(self.dict[self.key_count])
            self.closed.append(state)
            del self.open[0]

            self.open.sort(key = lambda x:x[2],reverse=False)

p = Puzzle()
p.a_star_traversal()

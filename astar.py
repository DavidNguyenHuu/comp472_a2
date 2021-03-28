
class Node:
    def __init__(self, state, parent):
        self.state = state
        self.parent = parent
        self.g = 0
        self.h = 0
        self.f = 0

    # Sort nodes with the lowest cost first
    def __lt__(self, other):
        return self.f < other.f


# If is_admissible is true => use admissible heuristic, if false => use inadmissible heuristic
def a_star_search(start, goal, is_admissible):
    open_list = []
    closed_list = []
    search = []  # Search path
    start_node = Node(start, None)
    goal_node = Node(goal, None)
    open_list.append(start_node)

    # Loop until the open list is empty
    while len(open_list) > 0:
        # Sort the open list to get the node with the lowest cost first
        open_list.sort()
        # Get the node with the lowest cost
        current_node = open_list.pop(0)
        # Add visited node to the closed and search lists
        closed_list.append(current_node)
        search.append(current_node.state)
        # Check if we have reached the goal, return the path
        if current_node.state == goal_node.state:
            path = []
            while current_node.state != start_node.state:
                path.append(current_node.state)
                current_node = current_node.parent
            path.append(start)
            if is_admissible:
                print("Solution path for A* (admissible): ", path[::-1])
                print("Search path for A* (admissible): ", search)
            else:
                print("Solution path for A* (inadmissible): ", path[::-1])
                print("Search path for A* (inadmissible): ", search)
            return path[::-1]
        # Get neighbors of current node
        neighbors = get_neighbors(current_node.state)
        # Loop neighbors
        for state in neighbors:
            neighbor = Node(state, current_node)
            if neighbor in closed_list:
                continue
            # Calculate f(n), g = num of steps from start, h = num of tiles not in goal state
            neighbor.g = current_node.g + 1
            neighbor.h = get_h(state, goal, is_admissible)
            neighbor.f = neighbor.g + neighbor.h
            # Check if neighbor is in open list and if it has a lower f value
            if add_to_open(open_list, neighbor):
                open_list.append(neighbor)
    # No path is found
    print("Solution path for A*: no solution")
    print("Search path for A*: no solution")
    return None


# If is_admissible is true => use admissible heuristic, if false => use inadmissible heuristic
def get_h(state, goal, is_admissible):
    count_h = 0
    if is_admissible:
        for row in range(len(state)):
            for col in range(len(state[row])):
                if state[row][col] != goal[row][col]:
                    count_h += 1
    else:
        for row in range(len(state)):
            for col in range(len(state[row])):
                if state[row][col] != goal[row][col]:
                    count_h += 2
    return count_h


# Get all next possible steps, convert tuple to list to switch values
def get_neighbors(current_state):
    neighbors = []
    for row in range(len(current_state)):
        for col in range(len(current_state[row])):
            # switch up
            if row != 0:
                temp_state = []
                for x in current_state:
                    temp_state.append(list(x))
                temp_state[row][col] = current_state[row - 1][col]
                temp_state[row - 1][col] = current_state[row][col]
                for x in range(len(temp_state)):
                    temp_state[x] = tuple(temp_state[x])
                tuple_temp_state = tuple(temp_state)
                if tuple_temp_state not in neighbors:
                    neighbors.append(tuple_temp_state)
            # switch down
            if row != len(current_state) - 1:
                temp_state = []
                for x in current_state:
                    temp_state.append(list(x))
                temp_state[row][col] = current_state[row + 1][col]
                temp_state[row + 1][col] = current_state[row][col]
                for x in range(len(temp_state)):
                    temp_state[x] = tuple(temp_state[x])
                tuple_temp_state = tuple(temp_state)
                if tuple_temp_state not in neighbors:
                    neighbors.append(tuple_temp_state)
            # switch left
            if col != 0:
                temp_state = []
                for x in current_state:
                    temp_state.append(list(x))
                temp_state[row][col] = current_state[row][col - 1]
                temp_state[row][col - 1] = current_state[row][col]
                for x in range(len(temp_state)):
                    temp_state[x] = tuple(temp_state[x])
                tuple_temp_state = tuple(temp_state)
                if tuple_temp_state not in neighbors:
                    neighbors.append(tuple_temp_state)
            # switch right
            if col != len(current_state) - 1:
                temp_state = []
                for x in current_state:
                    temp_state.append(list(x))
                temp_state[row][col] = current_state[row][col + 1]
                temp_state[row][col + 1] = current_state[row][col]
                for x in range(len(temp_state)):
                    temp_state[x] = tuple(temp_state[x])
                tuple_temp_state = tuple(temp_state)
                if tuple_temp_state not in neighbors:
                    neighbors.append(tuple_temp_state)
    return neighbors


# Check if a neighbor should be added to open list
def add_to_open(open_list, neighbor):
    for node in open_list:
        if neighbor.state == node.state and neighbor.f >= node.f:
            return False
    return True

def dfs(start, goal):
    open_list = []
    closed_list = []
    search = []
    open_list.append(start)
    timer = time.time()+60
    while len(open_list) > 0:
      if time.time() == timer:
         print("no solution, time out")
      test_node = open_list.pop(0)
       # print("the test state :", test_node.state)
        search.append(test_node.state)
        if test_node.state == goal:
            solution_path = []
            while test_node.state != start.state:
                solution_path.append(test_node.state)
                test_node = test_node.parent
            solution_path.append(start.state)
            print(" the solution path for the DFS is:", solution_path[::-1])
            print("the search path for the DFS is :", search)
        neighbors = get_neighbors(test_node.state)
        for state in neighbors:
          #  print("the neighbor state :",state)
            neighbor = Node(state,test_node)
            if neighbor in search:
                continue
            if add_to_open(open_list,neighbor):
                open_list.append(neighbor)
    print("no solution was found using DFS")
   
def IDS(start, goal,maxdepth):
        open_list = []
        closed_list = []
        search = []
        open_list.append(start)
        test_node = start
        timer = time.time() + 60
        while test_node.g <= maxdepth:
            if time.time() == timer:
                print("no solution, time out")
            test_node = open_list.pop(0)
            # print("the test state :", test_node.state)
            search.append(test_node.state)
            if test_node.state == goal:
                solution_path = []
                while test_node.state != start.state:
                    solution_path.append(test_node.state)
                    test_node = test_node.parent
                solution_path.append(start.state)
                print(" the solution path for the IDS is:", solution_path[::-1])
                print("the search path for the IDS is :", search)
            neighbors = get_neighbors(test_node.state)
            for state in neighbors:
                #  print("the neighbor state :",state)
                neighbor = Node(state, test_node)
                if neighbor in search:
                    continue
                neighbor.g = test_node.g + 1
                if add_to_open(open_list, neighbor):
                    open_list.append(neighbor)
        print("no solution was found using IDS")

def main():
    goal_state = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
    initial_state = ((6, 1, 2), (7, 8, 3), (5, 4, 9))
    initial_state2 = ((1, 2, 3), (4, 5, 6), (7, 9, 8))
    goal_state_list = [list(i) for i in goal_state]
    initial_state_list = [list(i) for i in initial_state]
    initial_state_list2 = [list(i) for i in initial_state2]
    start = Node(initial_state_list2, None)
   

if __name__ == '__main__':
    main()

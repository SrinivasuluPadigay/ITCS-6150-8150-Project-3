import time

def is_valid_color(state, color, assignment, australia_map, available_colors):
    for neighbor in australia_map[state]:
        if color == assignment.get(neighbor):
            return False
    return True

def forward_check(state, assignment, australia_map, available_colors):
    for neighbor in australia_map[state]:
        if neighbor not in assignment:
            available_colors[neighbor].discard(assignment[state])
            if len(available_colors[neighbor]) == 0:
                return False
    return True

def restore_colors(state, assignment, australia_map, available_colors):
    for neighbor in australia_map[state]:
        if neighbor not in assignment:
            available_colors[neighbor].add(assignment[state])

def dfs_with_forward_checking(australia_map, colors, state, assignment, available_colors, backtrack_count):
    if state == None:
        return True, backtrack_count

    for color in available_colors[state].copy():
        if is_valid_color(state, color, assignment, australia_map, available_colors):
            assignment[state] = color
            if forward_check(state, assignment, australia_map, available_colors):
                next_state_result, backtrack_count = dfs_with_forward_checking(australia_map, colors, next_state(australia_map, state), assignment, available_colors, backtrack_count)
                if next_state_result:
                    return True, backtrack_count
            restore_colors(state, assignment, australia_map, available_colors)
            assignment[state] = None
            backtrack_count += 1

    return False, backtrack_count

def next_state(australia_map, current_state):
    states = list(australia_map.keys())
    if current_state == states[-1]:
        return None
    return states[states.index(current_state) + 1]

def map_coloring_with_forward_checking(australia_map, colors):
    assignment = {}
    available_colors = {state: set(colors) for state in australia_map}
    start_time = time.time()
    solution, backtrack_count = dfs_with_forward_checking(australia_map, colors, list(australia_map.keys())[0], assignment, available_colors, 0)
    end_time = time.time()
    time_taken = end_time - start_time

    if solution:
        return assignment, backtrack_count, time_taken
    else:
        return None, backtrack_count, time_taken

# Define the map of Australia with adjacency for all states and territories
australia_map = {
    'Western Australia': {'Northern Territory', 'South Australia'},
    'Northern Territory': {'Western Australia', 'South Australia', 'Queensland'},
    'South Australia': {'Western Australia', 'Northern Territory', 'Queensland', 'New South Wales', 'Victoria'},
    'Queensland': {'Northern Territory', 'South Australia', 'New South Wales'},
    'New South Wales': {'Queensland', 'South Australia', 'Victoria'},
    'Victoria': {'South Australia', 'New South Wales', 'Tasmania'},
    'Tasmania': set()
}

# Define the available colors
colors = ['Red', 'Green', 'Blue', 'Yellow']

# Color the map with DFS and forward checking
coloring, backtracks, time_taken = map_coloring_with_forward_checking(australia_map, colors)
print("Color Assignment:", coloring)
print("Number of Backtracks:", backtracks)
print("Time Taken (seconds):", time_taken)

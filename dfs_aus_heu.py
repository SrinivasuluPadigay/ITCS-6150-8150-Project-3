import time

def mrv_selection(australia_map, assignment, available_colors):
    mrv_state = None
    min_colors = float('inf')

    for state in australia_map:
        if state not in assignment and len(available_colors[state]) < min_colors:
            mrv_state = state
            min_colors = len(available_colors[state])

    return mrv_state

def degree_constraint(australia_map, assignment):
    max_degree = -1
    selected_state = None

    for state in australia_map:
        if state not in assignment:
            degree = sum(1 for neighbor in australia_map[state] if neighbor not in assignment)
            if degree > max_degree:
                max_degree = degree
                selected_state = state

    return selected_state

def lcv_order(state, australia_map, available_colors):
    def count_conflicts(color):
        return sum(1 for neighbor in australia_map[state] if color in available_colors[neighbor])

    return sorted(available_colors[state], key=count_conflicts)

def is_valid_assignment(state, color, assignment, australia_map):
    for neighbor in australia_map[state]:
        if assignment.get(neighbor) == color:
            return False
    return True

def dfs_with_heuristics(australia_map, colors, assignment, available_colors, backtrack_count):
    if len(assignment) == len(australia_map):
        return assignment, backtrack_count

    state = mrv_selection(australia_map, assignment, available_colors)
    if not state:
        state = degree_constraint(australia_map, assignment)

    for color in lcv_order(state, australia_map, available_colors):
        if is_valid_assignment(state, color, assignment, australia_map):
            assignment[state] = color
            result, backtrack_count = dfs_with_heuristics(australia_map, colors, assignment, available_colors, backtrack_count)
            if result:
                return result, backtrack_count

            del assignment[state]
            backtrack_count += 1

    return None, backtrack_count

def map_coloring_with_heuristics(australia_map, colors):
    start_time = time.time()
    assignment = {}
    available_colors = {state: set(colors) for state in australia_map}
    solution, backtrack_count = dfs_with_heuristics(australia_map, colors, assignment, available_colors, 0)
    end_time = time.time()
    time_taken = end_time - start_time

    return solution, backtrack_count, time_taken

# Define the map of Australia with adjacency
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

# Color the map with DFS and heuristics
coloring, backtracks, time_taken = map_coloring_with_heuristics(australia_map, colors)
print("Color Assignment:", coloring)
print("Number of Backtracks:", backtracks)
print("Time Taken (seconds):", time_taken)

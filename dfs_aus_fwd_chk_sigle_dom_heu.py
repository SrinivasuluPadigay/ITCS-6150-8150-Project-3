import time

def select_unassigned_variable(australia_map, assignment, available_colors):
    # MRV and Degree Constraint
    mrv_state = None
    min_colors = float('inf')
    max_degree = -1

    for state in australia_map:
        if state not in assignment:
            num_colors = len(available_colors[state])
            degree = sum(1 for neighbor in australia_map[state] if neighbor not in assignment)
            if num_colors < min_colors or (num_colors == min_colors and degree > max_degree):
                mrv_state = state
                min_colors = num_colors
                max_degree = degree

    return mrv_state

def order_domain_values(state, australia_map, available_colors):
    # LCV
    def count_conflicts(color):
        return sum(1 for neighbor in australia_map[state] if color in available_colors[neighbor])
    return sorted(available_colors[state], key=count_conflicts)

def forward_check_and_propagate(state, color, australia_map, available_colors, assignment):
    updates = {}
    for neighbor in australia_map[state]:
        if neighbor not in assignment and color in available_colors[neighbor]:
            available_colors[neighbor].remove(color)
            updates[neighbor] = color
            if len(available_colors[neighbor]) == 0:
                restore_colors(updates, available_colors)
                return False
            if len(available_colors[neighbor]) == 1:
                singleton_color = next(iter(available_colors[neighbor]))
                if not forward_check_and_propagate(neighbor, singleton_color, australia_map, available_colors, assignment):
                    return False

    return True

def restore_colors(updates, available_colors):
    for state, color in updates.items():
        available_colors[state].add(color)

def dfs_with_heuristics_forward_check_and_propagation(australia_map, colors, assignment, available_colors, backtrack_count):
    if len(assignment) == len(australia_map):
        return assignment, backtrack_count

    state = select_unassigned_variable(australia_map, assignment, available_colors)
    for color in order_domain_values(state, australia_map, available_colors):
        if color in available_colors[state]:
            assignment[state] = color
            if forward_check_and_propagate(state, color, australia_map, available_colors, assignment):
                result, backtrack_count = dfs_with_heuristics_forward_check_and_propagation(australia_map, colors, assignment, available_colors, backtrack_count)
                if result is not None:
                    return result, backtrack_count

            del assignment[state]
            restore_colors({state: color}, available_colors)
            backtrack_count += 1

    return None, backtrack_count

def map_coloring_with_heuristics_forward_check_and_propagation(australia_map, colors):
    start_time = time.time()
    assignment = {}
    available_colors = {state: set(colors) for state in australia_map}
    solution, backtrack_count = dfs_with_heuristics_forward_check_and_propagation(australia_map, colors, assignment, available_colors, 0)
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

# Color the map with DFS, heuristics, forward checking, and propagation through singleton domains
coloring, backtracks, time_taken = map_coloring_with_heuristics_forward_check_and_propagation(australia_map, colors)
print("Color Assignment:", coloring)
print("Number of Backtracks:", backtracks)
print("Time Taken (seconds):", time_taken)

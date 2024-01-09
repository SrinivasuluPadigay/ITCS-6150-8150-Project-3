import time

def is_valid_color(state, color, assignment, australia_map, available_colors):
    for neighbor in australia_map[state]:
        if color == assignment.get(neighbor):
            return False
    return True

def forward_check(state, color, australia_map, available_colors, assignment):
    updates = {}
    for neighbor in australia_map[state]:
        if neighbor not in assignment:
            if color in available_colors[neighbor]:
                available_colors[neighbor].remove(color)
                updates[neighbor] = color

            if len(available_colors[neighbor]) == 0:
                restore_colors(updates, available_colors)
                return False
    return True, updates

def propagate_singleton_domains(australia_map, available_colors, assignment, updates):
    singletons = [state for state, colors in available_colors.items() if len(colors) == 1]
    while singletons:
        state = singletons.pop()
        color = next(iter(available_colors[state]))
        assignment[state] = color
        success, new_updates = forward_check(state, color, australia_map, available_colors, assignment)
        if not success:
            return False
        updates.update(new_updates)
        singletons.extend([s for s in new_updates if len(available_colors[s]) == 1])
    return True

def restore_colors(updates, available_colors):
    for state, color in updates.items():
        available_colors[state].add(color)

def dfs_with_forward_check_and_propagation(australia_map, colors, state, assignment, available_colors, backtrack_count):
    if state == None:
        return True, backtrack_count

    for color in available_colors[state].copy():
        if is_valid_color(state, color, assignment, australia_map, available_colors):
            assignment[state] = color
            success, updates = forward_check(state, color, australia_map, available_colors, assignment)
            if success and propagate_singleton_domains(australia_map, available_colors, assignment, updates):
                next_state_result, backtrack_count = dfs_with_forward_check_and_propagation(australia_map, colors, next_state(australia_map, state), assignment, available_colors, backtrack_count)
                if next_state_result:
                    return True, backtrack_count
            restore_colors(updates, available_colors)
            assignment[state] = None
            backtrack_count += 1

    return False, backtrack_count

def next_state(australia_map, current_state):
    states = list(australia_map.keys())
    if current_state == states[-1]:
        return None
    return states[states.index(current_state) + 1]

def map_coloring_with_forward_check_and_propagation(australia_map, colors):
    start_time = time.time()
    assignment = {}
    available_colors = {state: set(colors) for state in australia_map}
    solution, backtrack_count = dfs_with_forward_check_and_propagation(australia_map, colors, list(australia_map.keys())[0], assignment, available_colors, 0)
    end_time = time.time()
    time_taken = end_time - start_time

    if solution:
        return assignment, backtrack_count, time_taken
    else:
        return None, backtrack_count, time_taken

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

# Color the map with DFS, forward checking, and propagation through singleton domains
coloring, backtracks, time_taken = map_coloring_with_forward_check_and_propagation(australia_map, colors)
print("Color Assignment:", coloring)
print("Number of Backtracks:", backtracks)
print("Time Taken (seconds):", time_taken)

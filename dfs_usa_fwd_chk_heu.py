import time

def select_unassigned_variable(usa_map, assignment, available_colors):
    # MRV and Degree Constraint
    mrv_state = None
    min_colors = float('inf')
    max_degree = -1

    for state in usa_map:
        if state not in assignment:
            num_colors = len(available_colors[state])
            degree = sum(1 for neighbor in usa_map[state] if neighbor not in assignment)
            if num_colors < min_colors or (num_colors == min_colors and degree > max_degree):
                mrv_state = state
                min_colors = num_colors
                max_degree = degree

    return mrv_state

def order_domain_values(state, usa_map, available_colors):
    # LCV
    def count_conflicts(color):
        return sum(1 for neighbor in usa_map[state] if color in available_colors[neighbor])
    return sorted(available_colors[state], key=count_conflicts)

def forward_check(state, color, usa_map, available_colors, assignment):
    updates = {}
    for neighbor in usa_map[state]:
        if neighbor not in assignment and color in available_colors[neighbor]:
            available_colors[neighbor].remove(color)
            updates[neighbor] = color

            if len(available_colors[neighbor]) == 0:
                restore_colors(updates, available_colors)
                return False
    return True, updates

def restore_colors(updates, available_colors):
    for state, color in updates.items():
        available_colors[state].add(color)

def dfs_with_heuristics_and_forward_check(usa_map, colors, assignment, available_colors, backtrack_count):
    if len(assignment) == len(usa_map):
        return assignment, backtrack_count

    state = select_unassigned_variable(usa_map, assignment, available_colors)
    for color in order_domain_values(state, usa_map, available_colors):
        if color in available_colors[state]:
            assignment[state] = color
            success, updates = forward_check(state, color, usa_map, available_colors, assignment)
            if success:
                result, backtrack_count = dfs_with_heuristics_and_forward_check(usa_map, colors, assignment, available_colors, backtrack_count)
                if result is not None:
                    return result, backtrack_count

            del assignment[state]
            restore_colors(updates, available_colors)
            backtrack_count += 1

    return None, backtrack_count

def map_coloring_with_heuristics_and_forward_check(usa_map, colors):
    start_time = time.time()
    assignment = {}
    available_colors = {state: set(colors) for state in usa_map}
    solution, backtrack_count = dfs_with_heuristics_and_forward_check(usa_map, colors, assignment, available_colors, 0)
    end_time = time.time()
    time_taken = end_time - start_time

    return solution, backtrack_count, time_taken

# Define the map of the USA with adjacency for all 50 states
usa_map = {
    'Alabama': {'Florida', 'Georgia', 'Mississippi', 'Tennessee'},
    'Alaska': set(),
    'Arizona': {'California', 'Nevada', 'New Mexico', 'Utah'},
    'Arkansas': {'Louisiana', 'Mississippi', 'Missouri', 'Oklahoma', 'Tennessee', 'Texas'},
    'California': {'Arizona', 'Nevada', 'Oregon'},
    'Colorado': {'Kansas', 'Nebraska', 'New Mexico', 'Oklahoma', 'Utah', 'Wyoming'},
    'Connecticut': {'Massachusetts', 'New York', 'Rhode Island'},
    'Delaware': {'Maryland', 'New Jersey', 'Pennsylvania'},
    'Florida': {'Alabama', 'Georgia'},
    'Georgia': {'Alabama', 'Florida', 'North Carolina', 'South Carolina', 'Tennessee'},
    'Hawaii': set(),
    'Idaho': {'Montana', 'Nevada', 'Oregon', 'Utah', 'Washington', 'Wyoming'},
    'Illinois': {'Indiana', 'Iowa', 'Kentucky', 'Missouri', 'Wisconsin'},
    'Indiana': {'Illinois', 'Kentucky', 'Michigan', 'Ohio'},
    'Iowa': {'Illinois', 'Minnesota', 'Missouri', 'Nebraska', 'South Dakota', 'Wisconsin'},
    'Kansas': {'Colorado', 'Missouri', 'Nebraska', 'Oklahoma'},
    'Kentucky': {'Illinois', 'Indiana', 'Missouri', 'Ohio', 'Tennessee', 'Virginia', 'West Virginia'},
    'Louisiana': {'Arkansas', 'Mississippi', 'Texas'},
    'Maine': {'New Hampshire'},
    'Maryland': {'Delaware', 'Pennsylvania', 'Virginia', 'West Virginia'},
    'Massachusetts': {'Connecticut', 'New Hampshire', 'New York', 'Rhode Island', 'Vermont'},
    'Michigan': {'Indiana', 'Ohio', 'Wisconsin'},
    'Minnesota': {'Iowa', 'North Dakota', 'South Dakota', 'Wisconsin'},
    'Mississippi': {'Alabama', 'Arkansas', 'Louisiana', 'Tennessee'},
    'Missouri': {'Arkansas', 'Illinois', 'Iowa', 'Kansas', 'Kentucky', 'Nebraska', 'Oklahoma', 'Tennessee'},
    'Montana': {'Idaho', 'North Dakota', 'South Dakota', 'Wyoming'},
    'Nebraska': {'Colorado', 'Iowa', 'Kansas', 'Missouri', 'South Dakota', 'Wyoming'},
    'Nevada': {'Arizona', 'California', 'Idaho', 'Oregon', 'Utah'},
    'New Hampshire': {'Maine', 'Massachusetts', 'Vermont'},
    'New Jersey': {'Delaware', 'New York', 'Pennsylvania'},
    'New Mexico': {'Arizona', 'Colorado', 'Oklahoma', 'Texas', 'Utah'},
    'New York': {'Connecticut', 'Massachusetts', 'New Jersey', 'Pennsylvania', 'Vermont'},
    'North Carolina': {'Georgia', 'South Carolina', 'Tennessee', 'Virginia'},
    'North Dakota': {'Minnesota', 'Montana', 'South Dakota'},
    'Ohio': {'Indiana', 'Kentucky', 'Michigan', 'Pennsylvania', 'West Virginia'},
    'Oklahoma': {'Arkansas', 'Colorado', 'Kansas', 'Missouri', 'New Mexico', 'Texas'},
    'Oregon': {'California', 'Idaho', 'Nevada', 'Washington'},
    'Pennsylvania': {'Delaware', 'Maryland', 'New Jersey', 'New York', 'Ohio', 'West Virginia'},
    'Rhode Island': {'Connecticut', 'Massachusetts'},
    'South Carolina': {'Georgia', 'North Carolina'},
    'South Dakota': {'Iowa', 'Minnesota', 'Montana', 'Nebraska', 'North Dakota', 'Wyoming'},
    'Tennessee': {'Alabama', 'Arkansas', 'Georgia', 'Kentucky', 'Mississippi', 'Missouri', 'North Carolina', 'Virginia'},
    'Texas': {'Arkansas', 'Louisiana', 'New Mexico', 'Oklahoma'},
    'Utah': {'Arizona', 'Colorado', 'Idaho', 'Nevada', 'New Mexico', 'Wyoming'},
    'Vermont': {'Massachusetts', 'New Hampshire', 'New York'},
    'Virginia': {'Kentucky', 'Maryland', 'North Carolina', 'Tennessee', 'West Virginia'},
    'Washington': {'Idaho', 'Oregon'},
    'West Virginia': {'Kentucky', 'Maryland', 'Ohio', 'Pennsylvania', 'Virginia'},
    'Wisconsin': {'Illinois', 'Iowa', 'Michigan', 'Minnesota'},
    'Wyoming': {'Colorado', 'Idaho', 'Montana', 'Nebraska', 'South Dakota', 'Utah'}
}

# Define the available colors
colors = ['Red', 'Green', 'Blue', 'Yellow']

# Color the map with DFS, heuristics, and forward checking
coloring, backtracks, time_taken = map_coloring_with_heuristics_and_forward_check(usa_map, colors)
print("Color Assignment:", coloring)
print("Number of Backtracks:", backtracks)
print("Time Taken (seconds):", time_taken)

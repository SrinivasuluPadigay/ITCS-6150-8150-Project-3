import time

def is_valid_color(state, color, assignment, usa_map, available_colors):
    for neighbor in usa_map[state]:
        if color == assignment.get(neighbor):
            return False
    return True

def forward_check(state, assignment, usa_map, available_colors):
    for neighbor in usa_map[state]:
        if neighbor not in assignment:
            available_colors[neighbor].discard(assignment[state])
            if len(available_colors[neighbor]) == 0:
                return False
    return True

def restore_colors(state, assignment, usa_map, available_colors):
    for neighbor in usa_map[state]:
        if neighbor not in assignment:
            available_colors[neighbor].add(assignment[state])

def dfs_with_forward_checking(usa_map, colors, state, assignment, available_colors, backtrack_count):
    if state == None:
        return True, backtrack_count

    for color in available_colors[state].copy():
        if is_valid_color(state, color, assignment, usa_map, available_colors):
            assignment[state] = color
            if forward_check(state, assignment, usa_map, available_colors):
                next_state_result, backtrack_count = dfs_with_forward_checking(usa_map, colors, next_state(usa_map, state), assignment, available_colors, backtrack_count)
                if next_state_result:
                    return True, backtrack_count
            restore_colors(state, assignment, usa_map, available_colors)
            assignment[state] = None
            backtrack_count += 1

    return False, backtrack_count

def next_state(usa_map, current_state):
    states = list(usa_map.keys())
    if current_state == states[-1]:
        return None
    return states[states.index(current_state) + 1]

def map_coloring_with_forward_checking(usa_map, colors):
    assignment = {}
    available_colors = {state: set(colors) for state in usa_map}
    start_time = time.time()
    solution, backtrack_count = dfs_with_forward_checking(usa_map, colors, list(usa_map.keys())[0], assignment, available_colors, 0)
    end_time = time.time()
    time_taken = end_time - start_time

    if solution:
        return assignment, backtrack_count, time_taken
    else:
        return None, backtrack_count, time_taken

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

# Color the map with DFS and forward checking
coloring, backtracks, time_taken = map_coloring_with_forward_checking(usa_map, colors)
print("Color Assignment:", coloring)
print("Number of Backtracks:", backtracks)
print("Time Taken (seconds):", time_taken)

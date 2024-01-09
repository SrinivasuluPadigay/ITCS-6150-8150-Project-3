.README.txt

ITCS 6150/8150 - Intelligent Systems
Project-3 - Constraint satisfaction problems (CSP) - Map Coloring 

Submitted By: Srinivasulu Padigay (801330017)
Note: This is a solo project


Description:
------------
The project contains a collection of Python scripts designed to solve the map coloring problem. This problem involves assigning colors to regions on a map such that no adjacent regions share the same color. The repository includes implementations for both Australia and the USA maps, utilizing techniques like Depth-First Search (DFS), forward checking, propagation through singleton domains, and various heuristics.

How to use:
-----------
Each program is a standalone indepentent program which runs and produces the output the functionality of each program is explained below.

Contents:
---------
1. dfs_aus.py - Basic DFS implementation for coloring the map of Australia.
2. dfs_aus_fwd_chk.py - DFS with forward checking for Australia.
3. dfs_aus_fwd_chk_heu.py - DFS, forward checking, and heuristics for Australia.
4. dfs_aus_fwd_chk_sigle_dom.py - DFS with forward checking and singleton domain propagation for Australia.
5. dfs_aus_fwd_chk_sigle_dom_heu.py - Combines DFS, forward checking, singleton domain propagation, and heuristics for Australia.
6. dfs_aus_heu.py - DFS with heuristics for Australia.
7. dfs_usa.py - Basic DFS implementation for coloring the map of the USA.
8. dfs_usa_fwd_chk.py - DFS with forward checking for the USA.
9. dfs_usa_fwd_chk_heu.py - DFS, forward checking, and heuristics for the USA.
10. dfs_usa_fwd_chk_sigle_dom.py - DFS with forward checking and singleton domain propagation for the USA.
11. dfs_usa_fwd_chk_sigle_dom_heu.py - Combines DFS, forward checking, singleton domain propagation, and heuristics for the USA.
12. dfs_usa_heu.py - DFS with heuristics for the USA.

Usage:
------
Each script can be run independently to observe the map coloring solution for either Australia or the USA. The scripts output the color assignment for each state, the number of backtracks (if any), and the time taken to find the solution.

Requirements:
-------------
- Python 3.x
- No external libraries are required.

Acknowledgments:
----------------
- This project is part of an academic exercise in exploring algorithmic solutions to combinatorial problems.
- Special thanks to all contributors and reviewers.


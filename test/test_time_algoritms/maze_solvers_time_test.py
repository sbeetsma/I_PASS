"""script to analyze the solving time of the different solving algorithms and plots the average solving time
    tests every solver algorithm with every generator algorithm (excluding generator algorithms not used in the game)"""
from maze_game.maze_logic.maze import Maze
import time
from maze_game.maze_logic.maze_solvers import depth_first_search, breadth_first_search
import matplotlib.pyplot as plt
rounds = 1000
# for readability in plot (only test with implemented Generate algorithms IN the game)
alg_names = {1:'Depth first search', 2:'Prim', 3:'Wilson & Aldolous Broder'}
results = dict()
bar_width = 0.4
for size in range(10,51,20):
    results_dfs = dict()
    results_bfs = dict()
    for gen_func in alg_names:
        bfs = []
        dfs = []
        for i in range(rounds):
            maze = Maze(size, size, gen_func)

            start = time.time()
            breadth_first_search(maze, maze.start)
            bfs.append(time.time() - start)

            start = time.time()
            depth_first_search(maze, maze.start)
            dfs.append(time.time() - start)

        results_bfs[alg_names[gen_func]] = sum(bfs) / len(bfs)
        results_dfs[alg_names[gen_func]] = sum(dfs) / len(dfs)

    bar_bfs = [i for i in range(len(results_bfs))]
    bar_dfs = [i+bar_width for i in range(len(results_dfs))]

    plt.bar(bar_bfs, results_bfs.values(), bar_width, label='BFS')
    plt.bar(bar_dfs, results_dfs.values(), bar_width, label='DFS')
    plt.title(f'{size}x{size} maze solving')
    plt.xlabel('Maze generated by')
    plt.ylabel(f'Average solve time in seconds over {rounds} rounds')
    plt.xticks(bar_bfs+bar_width/2, alg_names.values())

    plt.xticks(size=8)
    plt.yticks(size=8)

    plt.legend(bbox_to_anchor=(1.1, 1.15))
    plt.show()

"""Script to test and plot data about generation times of maze generation algorithms"""
from maze_game.maze_logic.maze import Maze
import time
import matplotlib.pyplot as plt

rounds = 1000
maze_size = 50
# for readability in plot
alg_names = {1: 'Depth first search', 2: 'Prim', 3: 'Wilson & Aldolous Broder', 4: 'Wilson', 5: 'Aldolous Broder'}

for size in range(10, 51, 20):
    results_gens = dict()
    for gen_func in alg_names:
        time_results = []
        for i in range(rounds):
            start = time.time()
            maze = Maze(size, size, gen_func)
            time_results.append(time.time() - start)
        results_gens[alg_names[gen_func]] = sum(time_results) / len(time_results)

    plt.title(f'{size}x{size} maze generation')
    plt.xlabel('Maze generated by')
    plt.ylabel(f'Average generate time in seconds over {rounds} rounds')

    plt.bar(results_gens.keys(), results_gens.values())
    plt.xticks(fontsize=8, rotation=5)
    plt.yticks(fontsize=8)
    plt.show()
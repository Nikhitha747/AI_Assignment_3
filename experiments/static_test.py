from src.grid import generate_grid
from src.astar import astar

def run():
    grid = generate_grid(20, 0.2)
    start = (0, 0)
    goal = (19, 19)

    parent = astar(grid, start, goal)

    print("Static Path Planning Done")

if __name__ == "__main__":
    run()

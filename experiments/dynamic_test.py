from src.grid import generate_grid
from src.dynamic import add_dynamic_obstacle, replan

def run():
    grid = generate_grid(20, 0.2)
    start = (0, 0)
    goal = (19, 19)

    for step in range(5):
        grid = add_dynamic_obstacle(grid)
        parent = replan(grid, start, goal)
        print(f"Replanning step {step}")

if __name__ == "__main__":
    run()

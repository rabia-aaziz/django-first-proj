import numpy as np

grid_size = 4
goal_position = (3,3)
start_position = (0,0)
grid = np.zeros((grid_size, grid_size))
grid[goal_position] = 1

actions = ['up','down','left','right']
moves ={
    'up'   : (-1,0),
    'down' : (1,0),
    'left' : (0,-1),
    'right': (0,1)
}
def is_valid_move(position):
    return 0<= position[0] < grid_size and 0 <= position[1] < grid_size

def run_episode():
    
    position = list(start_position)
    steps = 0

    print("\nStarting a new episode....\n")
    print(f"Start position: {position}")
    while tuple(position) != goal_position:
        steps += 1
        action = np.random.choice(actions)
        print(f"Step {steps}: Chose action '{action}'")

        new_position = [
            position[0] + moves[action][0],
            position[1] + moves[action][1]
        ]

        if is_valid_move(new_position):
            position = new_position
            print(f"Moved to {position}")
        else:
            print("Hit a wall. Staying at the same position.")
        
        if tuple(position) == goal_position:
            print("\nGoal Reached!")
            break

        print(f"Episode Finished in {steps} steps./n")
        return steps

num_episodes = 5
for episode in range(1, num_episodes + 1):
    print(f"=== Episode {episode} ===")
    steps = run_episode()
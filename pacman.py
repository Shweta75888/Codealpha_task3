import random

# Define the game grid
GRID_SIZE = 10
grid = [[' ' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

# Define Pac-Man's starting position
pacman_x = random.randint(0, GRID_SIZE - 1)
pacman_y = random.randint(0, GRID_SIZE - 1)
grid[pacman_y][pacman_x] = 'P'

# Define ghost's starting position
ghost_x = random.randint(0, GRID_SIZE - 1)
ghost_y = random.randint(0, GRID_SIZE - 1)
grid[ghost_y][ghost_x] = 'G'

# Game loop
while True:
    # Display the grid
    for row in grid:
        print(' '.join(row))
    
    # Get user input
    direction = input("Enter direction (w/a/s/d): ")
    
    # Clear Pac-Man's current position
    grid[pacman_y][pacman_x] = ' '
    
    # Update Pac-Man's position based on input
    if direction == 'w' and pacman_y > 0:
        pacman_y -= 1
    elif direction == 's' and pacman_y < GRID_SIZE - 1:
        pacman_y += 1
    elif direction == 'a' and pacman_x > 0:
        pacman_x -= 1
    elif direction == 'd' and pacman_x < GRID_SIZE - 1:
        pacman_x += 1
    
    # Update Pac-Man's new position
    grid[pacman_y][pacman_x] = 'P'
    
    # Check if Pac-Man and ghost collide
    if pacman_x == ghost_x and pacman_y == ghost_y:
        print("Game Over - Pac-Man got caught by the ghost!")
        break
    
    # Update ghost's position
    ghost_x = random.randint(0, GRID_SIZE - 1)
    ghost_y = random.randint(0, GRID_SIZE - 1)
    grid[ghost_y][ghost_x] = 'G'

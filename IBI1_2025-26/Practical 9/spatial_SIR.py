# Core Process:
# 1. Copy the current population grid to avoid mutual influence during updates.
# 2. Find the coordinates of all infected individuals.
# 3. For each infected individual, check the 8 neighbors.
# 4. If a neighbor is susceptible, they get infected with a probability of beta.
# 5. Infected individuals recover with a probability of gamma.
# 6. Update the population grid and proceed to the next time step.
import numpy as np
import matplotlib.pyplot as plt

# contents
num_total = 10000  # 100x100 
grid_size = 100
beta = 0.3        
gamma = 0.05        
time_steps = 100

# create 100×100 network：0=S，1=I， 2=R
population = np.zeros((grid_size, grid_size), dtype=int)
# Create a 100×100 two-dimensional integer array, with all elements initially set to 0.

# randomly infect one person to start the outbreak
outbreak = np.random.choice(range(grid_size), 2)
# Randomly select two integers from 0 to 99 (the range of grid indices) to represent the row and column indices of the grid respectively, simulating the "random position of the initial infection source".

population[outbreak[0], outbreak[1]] = 1

# visualize initial state
plt.figure(figsize=(6, 4), dpi=150)
plt.imshow(population, cmap='viridis', interpolation='nearest')
plt.title("Spatial SIR Model: Time Step 0")
plt.axis('off')
plt.show()

# 100 time steps simulation 
for t in range(time_steps):
    # copy the population grid to update simultaneously
    new_population = population.copy()
    
    # find all infected points
    infected_points = np.argwhere(population == 1)
    
    for (i, j) in infected_points:
        # check 8 neighbors (Moore neighborhood) for potential infection
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                # escape the center point itself
                if di == 0 and dj == 0:
                    continue
                # check if neighbor is within bounds
                ni, nj = i + di, j + dj
                if 0 <= ni < grid_size and 0 <= nj < grid_size:
                    #  if neighbor is susceptible, it can be infected with probability beta
                    if population[ni, nj] == 0:
                        if np.random.rand() < beta:
                            new_population[ni, nj] = 1
        
        # infected person recovers with probability gamma
        if np.random.rand() < gamma:
            new_population[i, j] = 2
    
    # update population for the next time step
    population = new_population
    
    # visualize every 10 time steps
    if (t + 1) % 10 == 0 or t == time_steps - 1:
        plt.figure(figsize=(6, 4), dpi=150)
        plt.imshow(population, cmap='viridis', interpolation='nearest')
        plt.title(f"Spatial SIR Model: Time Step {t + 1}")
        plt.axis('off')
        plt.show()
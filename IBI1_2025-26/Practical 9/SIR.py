import numpy as np
import matplotlib.pyplot as plt

# contents  
num_total = 10000
I_num = 1
S_num = num_total - I_num
R_num = 0
beta = 0.3
gamma = 0.1
time_steps = 1000

# record history for plotting   
S_history = [S_num]
I_history = [I_num]
R_history = [R_num]

for t in range(time_steps):
    # Infected randomly 
    # The probability of being infected = beta * (I/N)
    infection_prob = beta * (I_num / num_total)
    
    # use binomial distribution to randomly determine how many new infections occur today
    # The probability that each of the S_num individuals was infected is infection_prob, 
    # the total number of people who were infected is new_infected
    new_infected = np.random.binomial(n=S_num, p=infection_prob)

    # Recovered randomly
    new_recovered = np.random.binomial(n=I_num, p=gamma)

    S_num -= new_infected
    I_num += new_infected - new_recovered
    R_num += new_recovered

    S_history.append(S_num)
    I_history.append(I_num)
    R_history.append(R_num)

# draw the results
plt.figure(figsize=(6, 4), dpi=150)
plt.plot(S_history, label="Susceptible", color="#2E86AB")
plt.plot(I_history, label="Infected", color="#A23B72")
plt.plot(R_history, label="Recovered", color="#2ECC71")
plt.xlabel("Time")
plt.ylabel("Number of People")
plt.title("Stochastic SIR Model")
plt.legend()
plt.tight_layout()
plt.show()
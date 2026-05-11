import numpy as np
import matplotlib.pyplot as plt

# contents  
num_total = 10000
I_num_init = 1  
beta = 0.3      
gamma = 0.05 
time_steps = 1000

vaccination_rates = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]  # from 10% to 100% vaccination rates (10 levels)
colors = ["#A23B72", "#F18F01", "#C73E1D", "#2E86AB", "#2ECC71"]

# history records for all vaccination rates 
all_I_history = []
all_S_history = []
all_R_history = []

# for each vaccination rate, run the SIR simulation and record the history
for rate in vaccination_rates:
    vaccinated_num = num_total * rate
    S_num = num_total - I_num_init - vaccinated_num
    I_num = I_num_init
    R_num = vaccinated_num

    # history records for this vaccination rate
    S_history = [S_num]
    I_history = [I_num]
    R_history = [R_num]

    for t in range(time_steps):
        # S_num and I_num should not be negative, ensure they are at least 0 (core fix point 1)
        S_num = max(S_num, 0)
        I_num = max(I_num, 0)
        
        # Infected randomly 
        # The probability of being infected = beta * (I/N)
        # core fix point 2: if I_num is 0, then infection_prob should be 0 to avoid invalid probability
        infection_prob = beta * (I_num / num_total) if I_num > 0 else 0.0
        
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

    all_S_history.append(S_history)
    all_I_history.append(I_history)
    all_R_history.append(R_history)

plt.figure(figsize=(10, 6), dpi=150)
# draw all curves for different vaccination rates
for idx, rate in enumerate(vaccination_rates):
    plt.plot(
        all_I_history[idx],
        label=f"Vaccination Rate {rate*100}%",
        color=colors[idx % len(colors)],  # 补充：避免颜色列表长度不足的潜在问题
        linewidth=1.5
    )

plt.xlabel("Time (Steps)")
plt.ylabel("Number of Infected People")
plt.title("Stochastic SIR Model with Gradient Vaccination Rates")
plt.legend(loc="upper right")
plt.grid(alpha=0.3)  
plt.tight_layout()
plt.show()
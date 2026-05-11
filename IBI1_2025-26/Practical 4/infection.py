"""
Pseudocode:
1. Initialize initial infected count (ID = 5), growth rate (0.4), and day counter (0)
2. While infected count is less than 91 (total class size):
   a. Calculate new infected count by multiplying by (1 + growth rate)
   b. Increment day counter
   c. Print current day and infected count (rounded to integer)
3. Output total days required to infect the whole class
"""
# Initial parameters
initial_infected = 5
growth_rate = 0.4
total_class_size = 91
infected = initial_infected
day = 0

# Simulate infection spread
while infected < total_class_size:
    infected = infected * (1 + growth_rate)
    day += 1
    # Print rounded value for readability
    print(f"Day: {day}, Infected: {round(infected)}")

print(f"\nTotal days to infect the whole class: {day}")
import matplotlib.pyplot as plt

# Population data (in millions)
population_data = {
    'UK': {'2020': 66.7, '2024': 69.2},
    'China': {'2020': 1426, '2024': 1410},
    'Italy': {'2020': 59.4, '2024': 58.9},
    'Brazil': {'2020': 208.6, '2024': 212.0},
    'USA': {'2020': 331.6, '2024': 340.1}
}

# Calculate percentage population change
population_change = {}
for country, data in population_data.items():
    pop_2020 = data['2020']
    pop_2024 = data['2024']
    change_percent = ((pop_2024 - pop_2020) / pop_2020) * 100
    population_change[country] = round(change_percent, 2)

# Print percentage change for each country
print("Population percentage change (2020-2024):")
for country, percent in population_change.items():
    print(f"{country}: {percent}%")

# Sort countries by percentage change in descending order
sorted_countries = sorted(population_change.items(), key=lambda x: x[1], reverse=True)
print("\nCountries sorted by population growth rate (descending):")
for idx, (country, percent) in enumerate(sorted_countries, 1):
    print(f"{idx}. {country}: {percent}%")

# Identify countries with largest increase and decrease
max_growth_country = sorted_countries[0][0]
max_growth_percent = sorted_countries[0][1]
min_growth_country = sorted_countries[-1][0]
min_growth_percent = sorted_countries[-1][1]

print(f"\nCountry with largest population increase: {max_growth_country} ({max_growth_percent}%)")
print(f"Country with largest population decrease: {min_growth_country} ({min_growth_percent}%)")

# Extract data for plotting
sorted_names = [item[0] for item in sorted_countries]
sorted_percents = [item[1] for item in sorted_countries]

# Create bar chart
plt.figure(figsize=(10, 8), dpi=150)
# Green for growth, red for decline
colors = ['#2E8B57' if p >= 0 else '#DC143C' for p in sorted_percents]
bars = plt.bar(sorted_names, sorted_percents, color=colors, edgecolor='black', width=0.6)

plt.title('Population Percentage Change (2020-2024)', fontsize=14, pad=20)
plt.xlabel('Country', fontsize=12, labelpad=10)
plt.ylabel('Population Change (%)', fontsize=12, labelpad=10)
plt.axhline(y=0, color='black', linestyle='-', linewidth=0.8)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
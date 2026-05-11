import matplotlib.pyplot as plt

# Heart rate data
heart_rates = [72, 60, 126, 85, 90, 59, 76, 131, 88, 121, 64]
num_patients = len(heart_rates)
print(f"Number of patients: {num_patients}")

# Calculate mean heart rate
mean_heart_rate = sum(heart_rates) / num_patients
print(f"Mean heart rate: {mean_heart_rate:.2f} bpm")

# Categorize heart rates
low = 0
normal = 0
high = 0

for rate in heart_rates:
    if rate < 60:
        low += 1
    elif 60 <= rate <= 120:  # Fixed: include 60 and 120 in normal category
        normal += 1
    else:
        high += 1

print(f"\nNumber of patients with low heart rate (<60 bpm): {low}")
print(f"Number of patients with normal heart rate (60-120 bpm): {normal}")
print(f"Number of patients with high heart rate (>120 bpm): {high}")

# Determine the largest category
if low > normal and low > high:
    print("\nThe largest category is low heart rate")
elif normal > low and normal > high:
    print("\nThe largest category is normal heart rate")
else:
    print("\nThe largest category is high heart rate")

# Create pie chart
plt.figure(figsize=(8, 8), dpi=150)
labels = ['Low (<60 bpm)', 'Normal (60-120 bpm)', 'High (>120 bpm)']
sizes = [low, normal, high]
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1']
explode = (0.05, 0, 0.05)

wedges, texts, autotexts = plt.pie(
    sizes,
    labels=labels,
    colors=colors,
    explode=explode,
    autopct='%1.1f%%',
    shadow=True,
    startangle=140,
    textprops={'fontsize': 11}
)

# Style percentage text
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(10)
    autotext.set_weight('bold')

plt.title('Heart Rate Category Distribution', fontsize=14, pad=20)
plt.legend(
    wedges,
    [f'{label}: {size} patients' for label, size in zip(labels, sizes)],
    title="Heart Rate Categories",
    loc="center left",
    bbox_to_anchor=(1, 0, 0.5, 1)
)
plt.tight_layout()
plt.show()
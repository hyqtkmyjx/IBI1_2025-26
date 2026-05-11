"""
Calculate creatinine clearance rate using the Cockcroft-Gault formula
Formula:
- Male: CrCl = ((140 - age) * weight) / (72 * serum_creatinine)
- Female: CrCl = ((140 - age) * weight) / (72 * serum_creatinine) * 0.85
"""
# Define valid input ranges
MAX_AGE = 100
MIN_WEIGHT = 20
MAX_WEIGHT = 80
MIN_CREATININE = 0
MAX_CREATININE = 100

# Get user input
age = int(input("Enter your age: "))
weight = int(input("Enter your weight (kg): "))
gender = input("Enter your gender (male/female): ").lower()
serum_creatinine = int(input("Enter your serum creatinine level (μmol/L): "))

# Validate input values
if age > MAX_AGE:
    print("Error: Age exceeds maximum limit of 100 years")
elif weight < MIN_WEIGHT or weight > MAX_WEIGHT:
    print(f"Error: Weight must be between {MIN_WEIGHT} and {MAX_WEIGHT} kg")
elif serum_creatinine < MIN_CREATININE or serum_creatinine > MAX_CREATININE:
    print(f"Error: Serum creatinine must be between {MIN_CREATININE} and {MAX_CREATININE} μmol/L")
elif gender not in ["male", "female"]:
    print("Error: Gender must be either 'male' or 'female'")
else:
    # Calculate creatinine clearance
    if gender == "male":
        crcl = ((140 - age) * weight) / (72 * serum_creatinine)
    else:
        crcl = ((140 - age) * weight) / (72 * serum_creatinine) * 0.85
    
    print(f"Your creatinine clearance is: {crcl:.4f} mL/min")
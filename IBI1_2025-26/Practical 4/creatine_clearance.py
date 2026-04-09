# Start of the program
# Define constants: maximum age, weight range, creatinine range, gender constants
age = 100                     # Maximum age
weightmax = 80                # Maximum weight
weightmin = 20                # Minimum weight
Crmax = 100                   # Maximum serum creatinine level
Crmin = 0                     # Minimum serum creatinine level
gentle1 = "male"              # Male identifier
gentle2 = "female"            # Female identifier

# Input section
# Prompt the user to enter age, weight, gender, and serum creatinine level, then convert to corresponding types
a = int(input("Enter your age: "))
b = int(input("Enter your weight: "))
c = input("Enter your gender: ")
Cr = int(input("Enter your serum creatinine level: "))

# Check if input values are outside the normal range
# If age exceeds the maximum limit, or weight is out of range, or creatinine is out of range, 
# or gender is neither male nor female, prompt an exception
if a > age or b > weightmax or b < weightmin or Cr > Crmax or Cr < Crmin or c != gentle1 and c != gentle2 :
    print("Your creatine clearance is not normal")
else:
    # All input values are within the normal range, start calculating creatinine clearance rate
    if c == gentle1:
        # Male calculation formula: (140 - age) * weight / (72 * serum creatinine)
        CrCl = ((140 - a) * b) / (72 * Cr)
    else:
        # Female calculation formula: male result * 0.85
        CrCl = ((140 - a) * b) / (72 * Cr) * 0.85
    # Output the calculation result, keeping four decimal places
    print("Your creatine clearance is %.4f" % CrCl)
# End of the program
# Objective: Calculate the total mass of the given protein sequence
# Core calculation function (input: protein sequence string):
# a. Initialize the total mass to 0
# b. Traverse each amino acid in the sequence one by one:
# i. If the amino acid is not in the dictionary → Throw an error (message: Unknown amino acid: [the amino acid])
# ii. If the amino acid exists → Add its mass to the total mass
# c. Return the final total mass 
# 3. Running test:
# a. Define the protein sequence to be tested (e.g. 'HYQ')
# b. Call the calculation function to obtain the total mass of this sequence
# c. Print the result (with 2 decimal places)
amino_mass = {
    'G': 57.02, 'A': 71.04, 'S': 87.03, 'P': 97.05, 'V': 99.07,
    'T': 101.05, 'C': 103.01, 'I': 113.08, 'L': 113.08, 'N': 114.04,
    'D': 115.03, 'Q': 128.06, 'K': 128.09, 'E': 129.04, 'M': 131.04,
    'H': 137.06, 'F': 147.07, 'R': 156.10, 'Y': 163.06, 'W': 186.08
}

def protein_mass(protein):
    mass = 0
    for amino in protein:
        if amino not in amino_mass:
            raise ValueError(f"Unknown amino acid: {amino}")
        mass += amino_mass[amino]
    return mass

if __name__ == "__main__":
    protein  = 'HYQ'
    mass = protein_mass(protein)
    print("Protein sequence mass: %.2f" % mass)
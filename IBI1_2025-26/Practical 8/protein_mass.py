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
            raise ValueError(f"未知氨基酸: {amino}")
        mass += amino_mass[amino]
    return mass

if __name__ == "__main__":
    protein  = 'HYQ'
    mass = protein_mass(protein)
    print("蛋白质序列质量: %.2f" % mass)
from Bio import SeqIO
import matplotlib.pyplot as plt
from collections import defaultdict

def read_fasta(fasta_file):
    """Read FASTA file and return a dictionary {gene_name: sequence}"""
    all_genes = {}
    for record in SeqIO.parse(fasta_file, "fasta"):
        gene_name = record.id.split()[0]
        all_genes[gene_name] = str(record.seq)
    return all_genes

def find_longest_orf_with_stop(seq, target_stop):
    """
    Find the longest ORF ending with the specified stop codon
    Returns: list of codons in the longest ORF (excluding the stop codon)
    """
    start_codon = "ATG"
    stop_codons = {"TAA", "TAG", "TGA"}
    longest_codons = []
    
    for i in range(len(seq) - 2):
        if seq[i:i+3] == start_codon:
            current_codons = []
            for j in range(i, len(seq) - 2, 3):
                codon = seq[j:j+3]
                if codon in stop_codons:
                    if codon == target_stop:
                        # Update longest codon list if current ORF is longer
                        if len(current_codons) > len(longest_codons):
                            longest_codons = current_codons.copy()
                    break  # Terminate current ORF
                current_codons.append(codon)
    
    return longest_codons

def main():
    # Get user input for stop codon
    while True:
        target_stop = input("Please enter a stop codon (TAA/TAG/TGA): ").strip().upper()
        if target_stop in {"TAA", "TAG", "TGA"}:
            break
        print("Invalid input! Please enter one of TAA, TAG, TGA.")
    
    # Read FASTA file (absolute path to avoid file not found error)
    fasta_file = "/Users/hyq-mac/Desktop/2026春夏学期资料/IBI/IBI1_2025-26/Practical 7/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
    all_genes = read_fasta(fasta_file)
    print(f"Total genes read: {len(all_genes)}")
    
    # Count frequency of all codons (no merging)
    codon_counts = defaultdict(int)
    total_codons = 0
    
    for gene_name, seq in all_genes.items():
        codons = find_longest_orf_with_stop(seq, target_stop)
        for codon in codons:
            codon_counts[codon] += 1
            total_codons += 1
    
    print(f"\nGenes containing {target_stop} stop codon: {len([c for c in codon_counts.values() if c > 0])}")
    print(f"Total codons counted: {total_codons}")
    
    # Generate full codon frequency pie chart 
    # Sort codons by frequency in descending order
    sorted_codons = sorted(codon_counts.items(), key=lambda x: x[1], reverse=True)
    labels = [codon for codon, _ in sorted_codons]
    sizes = [count for _, count in sorted_codons]
    
    # Optimize pie chart to avoid label overlap
    plt.figure(figsize=(12, 10), dpi=150)
    wedges, texts, autotexts = plt.pie(
        sizes,
        labels=labels,
        autopct='%1.1f%%',
        startangle=90,
        labeldistance=1.05,
        pctdistance=0.85,
        textprops={'fontsize': 7}
    )
    
    # Adjust percentage text style
    for autotext in autotexts:
        autotext.set_fontsize(6)
        autotext.set_color('white')
    
    plt.title(f"Full Codon Frequency Upstream of {target_stop} Stop Codon", fontsize=12, fontweight='bold')
    plt.axis('equal')  # Ensure pie chart is circular
    plt.tight_layout()
    
    # Save high-resolution pie chart to file
    output_file = f"/Users/hyq-mac/Desktop/2026春夏学期资料/IBI/IBI1_2025-26/Practical 7/codon_frequency_{target_stop}_full.png"
    plt.savefig(output_file, dpi=150, bbox_inches='tight')  # Prevent label truncation
    print(f"\nFull codon frequency pie chart saved to: {output_file}")
    plt.show()

if __name__ == "__main__":
    main()
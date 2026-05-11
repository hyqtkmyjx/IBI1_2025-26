from Bio import SeqIO
import matplotlib.pyplot as plt
from collections import defaultdict

def read_fasta(fasta_file):
    "Read the FASTA file and return a dictionary where the keys are gene names and the values are the sequences."
    all_genes = {}
    for record in SeqIO.parse(fasta_file, "fasta"):
        gene_name = record.id.split()[0]
        all_genes[gene_name] = str(record.seq)
    return all_genes

def find_longest_orf_with_stop(seq, target_stop):
    """
    Find the longest ORF in the sequence that ends with the specified stop codon.
    Return: The list of codons of the longest ORF (excluding the stop codon)
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
                        # Find the target termination codon and update the list of the longest codons
                        if len(current_codons) > len(longest_codons):
                            longest_codons = current_codons.copy()
                    break  # Terminate the current ORF
                current_codons.append(codon)
    
    return longest_codons

def main():
    # 1. User inputs termination codon
    while True:
        target_stop = input("Please enter a stop codon (TAA/TAG/TGA): ").strip().upper()
        if target_stop in {"TAA", "TAG", "TGA"}:
            break
        print("Invalid input! Please enter one of TAA, TAG, TGA.")
    # 2. Read FASTA file and get all genes
    fasta_file = "/Users/hyq-mac/Desktop/2026春夏学期资料/IBI/IBI1_2025-26/Practical 7/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
    all_genes = read_fasta(fasta_file)
    print(f"Total genes read: {len(all_genes)}")
    
    # 3. Calculate the frequency of codons
    codon_counts = defaultdict(int)
    total_codons = 0
    
    for gene_name, seq in all_genes.items():
        codons = find_longest_orf_with_stop(seq, target_stop)
        for codon in codons:
            codon_counts[codon] += 1
            total_codons += 1
    
    print(f"\nGenes containing {target_stop} stop codon: {len([c for c in codon_counts.values() if c > 0])}")
    print(f"Total codons counted: {total_codons}")
    
    # 4. Generate pie chart (show only the top 10 most frequent codons, merge the rest as "Others")
    sorted_codons = sorted(codon_counts.items(), key=lambda x: x[1], reverse=True)
    top_10 = sorted_codons[:10]
    others_count = sum(count for _, count in sorted_codons[10:])
    
    labels = [codon for codon, _ in top_10] + ["Others"]
    sizes = [count for _, count in top_10] + [others_count]
    
    plt.figure(figsize=(10, 8), dpi=150)
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.title(f"Codon Frequency Upstream of {target_stop} Stop Codon")
    plt.axis('equal')  # Ensure that the chart is circular
    plt.tight_layout()
    
    # Save pie chart to file
    output_file = f"codon_frequency_{target_stop}.png"
    plt.savefig(output_file, dpi=150)
    print(f"\nPie chart saved to: {output_file}")
    plt.show()

if __name__ == "__main__":
    main()
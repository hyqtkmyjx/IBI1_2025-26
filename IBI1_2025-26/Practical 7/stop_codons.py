from Bio import SeqIO 

def read_fasta(fasta_file):
    "Read the FASTA file and return a dictionary where the keys are gene names and the values are the complete sequences."
    all_genes = {}  # Initialize an empty dictionary
    for record in SeqIO.parse(fasta_file, "fasta"):
        gene_name = record.id  # Extract gene name
        sequence = str(record.seq)  # Extract sequence
        all_genes[gene_name] = sequence  # Store in dictionary
    
    return all_genes

def find_codons(seq):
    start_codon = "ATG"
    stop_codons = {"TAA", "TAG", "TGA"}
    found_stops = set()  # The collection automatically removes duplicates. (Why remove duplicates?)
    
    for i in range(len(seq) - 2):
        if seq[i:i+3] == start_codon:
            for j in range(i, len(seq) - 2, 3):
                codon = seq[j:j+3]
                if codon in stop_codons:
                    found_stops.add(codon)
                    # Once an ORF is found, we can stop this one and move on to the next ATG codon.
                    break
    
    return found_stops

def write_fasta(all_genes, output_fasta):
    # Header Format: >Gene Name, Stop Codon 1, Stop Codon 2,...
    with open(output_fasta, 'w') as f: # Open the file and temporarily name it as "f" for ease of operation
        for gene_name, seq in all_genes.items(): # The returned value is a tuple, containing the gene name and sequence
            stops = find_codons(seq)
            if stops:  # If there is at least one stop codon
            # list(stops) is used to convert the set into a list, and sorted() is used for sorting
                sorted_stops = sorted(list(stops))
                # Write header: >Gene name Stop codon
                f.write(f">{gene_name} {','.join(sorted_stops)}\n")
                for i in range(0, len(seq),80):
                    f.write(f"{seq[i:i+80]}\n")

def main():
    fasta_file = "/Users/hyq-mac/Desktop/2026春夏学期资料/IBI/IBI1_2025-26/Practical 7/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
    output_fasta = "stop_genes.fa"
    all_genes = read_fasta(fasta_file) 
    
    write_fasta(all_genes, output_fasta) 
    
    result_genes = read_fasta(output_fasta)
    print(f"Done! A total of {len(result_genes)} genes containing stop codons within the frame have been filtered out.")
    print(f"The results have been saved to: {output_fasta}")

if __name__ == "__main__":
    main()
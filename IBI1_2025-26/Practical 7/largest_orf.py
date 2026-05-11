seq = 'AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'
start = 'AUG'
stop = ['UAA', 'UAG', 'UGA']
len_ORF = 0
longest_orf_seq = ""  # Store the longest ORF sequence

for i in range(len(seq)-2):
    codon = seq[i:i+3]
    if codon == start:
        for j in range(i+3, len(seq)-2, 3):
            next_codon = seq[j:j+3]
            if next_codon in stop:
                current_orf = seq[i:j+3]  # Extract the current ORF
                current_length = j - i + 3
                if current_length > len_ORF:
                    len_ORF = current_length
                    longest_orf_seq = current_orf  # Update the longest ORF sequence
                break

print('The longest ORF sequence is:', longest_orf_seq)  # Output
print('The length of the longest ORF is:', len_ORF)
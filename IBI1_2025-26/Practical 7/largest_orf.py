seq = 'AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAUAG'
start = 'AUG'
stop = ['UAA', 'UAG', 'UGA']
len_ORF = 0

for i in range(len(seq)-2): #防止超出范围 -2
    codon = seq[i:i+3] #包含start 没有end 三个字符
    if codon == start:
        for j in range(i+3, len(seq)-2, 3): #每次跳过三个字符
            next_codon = seq[j:j+3]
            if next_codon in stop:
                len_ORF = max(len_ORF, j - i + 3) #包含stop
                break

print('The length of the longest ORF is:', len_ORF)

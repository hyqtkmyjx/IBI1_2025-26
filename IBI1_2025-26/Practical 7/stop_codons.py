from Bio import SeqIO #下载Biopython库

def read_fasta(fasta_file):
    """读取FASTA文件,返回字典 {基因名: 完整序列}"""
    all_genes = {}  # 初始化空字典
    for record in SeqIO.parse(fasta_file, "fasta"):
        gene_name = record.id  # 提取基因名
        sequence = str(record.seq)  # 提取序列
        all_genes[gene_name] = sequence  # 存储在字典里
    
    return all_genes

def find_in_frame_stop_codons(seq):
    start_codon = "ATG"
    stop_codons = {"TAA", "TAG", "TGA"}
    found_stops = set()  # 集合自动去重，（为什么要去重？）
    
    for i in range(len(seq) - 2):
        if seq[i:i+3] == start_codon:
            for j in range(i, len(seq) - 2, 3):
                codon = seq[j:j+3]
                if codon in stop_codons:
                    found_stops.add(codon)
                    # 找到一个就可以停这个ORF了，继续找下一个ATG密码子
                    break
    
    return found_stops

def write_stop_genes_fasta(genes_dict, output_filename):
    #表头格式：>基因名 终止密码子1,终止密码子2,...
    with open(output_filename, 'w') as f: #打开文件并且暂时起名字为f，方便操作
        for gene_name, seq in genes_dict.items(): #返回的是一个元组，包含基因名和序列
            # 找这个基因是不是有框内终止密码子
            stops = find_in_frame_stop_codons(seq)
            if stops:  # 如果至少有一个终止密码子
                # list(stops)是为了把集合转换成列表，sorted()是为了排序
                sorted_stops = sorted(list(stops))
                # 写header：>基因名 终止密码子
                f.write(f">{gene_name} {','.join(sorted_stops)}\n")
                # 写序列（为了好看，每行80个碱基）
                for i in range(0, len(seq), 80):
                    f.write(f"{seq[i:i+80]}\n")

def main():
    fasta_file = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
    output_fasta = "stop_genes.fa"
    all_genes = read_fasta(fasta_file) #读取文件，拿到所有基因
    
    write_stop_genes_fasta(all_genes, output_fasta) #写入新文件
    
    # 重新读一下生成的文件，看看有多少个基因
    result_genes = read_fasta(output_fasta)
    print(f"完成！共筛选出 {len(result_genes)} 个包含框内终止密码子的基因")
    print(f"结果已保存到: {output_fasta}")

if __name__ == "__main__":
    main()
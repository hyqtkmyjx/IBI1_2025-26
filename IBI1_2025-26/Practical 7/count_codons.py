from Bio import SeqIO  # 沿用Biopython库处理FASTA

def read_fasta(fasta_file):
    """读取FASTA文件,返回字典 {基因名: 完整序列}"""
    all_genes = {}  # 初始化空字典存储基因名-序列对
    for record in SeqIO.parse(fasta_file, "fasta"):
        gene_name = record.id  # 提取基因ID
        sequence = str(record.seq)  # 提取序列并转为字符串
        all_genes[gene_name] = sequence  # 存入字典
    return all_genes

def find_longest_orf(seq):
    """
    查找序列中最长的ORF（开放阅读框）
    输入：基因序列字符串
    返回：最长ORF的信息字典 {start: 起始位置, end: 结束位置, length: 长度, seq: ORF序列}
    """
    start_codon = "ATG"
    stop_codons = {"TAA", "TAG", "TGA"}
    longest_orf = {"start": -1, "end": -1, "length": 0, "seq": ""}  # 初始化最长ORF
    
    # 遍历序列找所有起始密码子
    for i in range(len(seq) - 2):
        if seq[i:i+3] == start_codon:
            # 从起始密码子后按3个碱基步长找终止密码子
            for j in range(i + 3, len(seq) - 2, 3):
                codon = seq[j:j+3]
                if codon in stop_codons:
                    # 计算当前ORF长度（包含终止密码子）
                    orf_length = j - i + 3
                    orf_seq = seq[i:j+3]
                    # 更新最长ORF
                    if orf_length > longest_orf["length"]:
                        longest_orf = {
                            "start": i,
                            "end": j + 3,  # 切片是左闭右开，结束位置+3
                            "length": orf_length,
                            "seq": orf_seq
                        }
                    break  # 找到第一个终止密码子就停止（ORF结束）
    
    return longest_orf

def write_longest_orf_fasta(all_genes, output_fasta):
    """
    将每个基因的最长ORF信息写入FASTA文件
    表头格式：>基因名 最长ORF起始位置:结束位置 长度:ORF长度
    """
    with open(output_fasta, 'w') as f:
        for gene_name, full_seq in all_genes.items():
            longest_orf = find_longest_orf(full_seq)
            # 只保留有有效ORF的基因（长度>0）
            if longest_orf["length"] > 0:
                # 写入FASTA表头（包含ORF信息）
                header = (f">{gene_name} "
                          f"longest_orf_start:{longest_orf['start']} "
                          f"end:{longest_orf['end']} length:{longest_orf['length']}")
                f.write(f"{header}\n")
                # ORF序列按80字符换行写入（沿用你的格式）
                orf_seq = longest_orf["seq"]
                for i in range(0, len(orf_seq), 80):
                    f.write(f"{orf_seq[i:i+80]}\n")

def main():
    # 输入输出文件路径（沿用你的酵母cDNA文件路径）
    fasta_file = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
    output_fasta = "longest_orf_genes.fa"
    
    # 读取所有基因
    all_genes = read_fasta(fasta_file)
    print(f"共读取到 {len(all_genes)} 个基因")
    
    # 筛选并写入最长ORF的基因
    write_longest_orf_fasta(all_genes, output_fasta)
    
    # 验证输出文件并统计结果
    result_genes = read_fasta(output_fasta)
    print(f"完成！共筛选出 {len(result_genes)} 个包含有效ORF的基因")
    print(f"最长ORF结果已保存到: {output_fasta}")
    
    # 可选：输出前5个基因的最长ORF信息，方便验证
    print("\n前5个基因的最长ORF信息：")
    count = 0
    for gene_name, seq in result_genes.items():
        if count >= 5:
            break
        longest_orf = find_longest_orf(seq)
        print(f"基因 {gene_name}: ORF长度={longest_orf['length']}, 起始位置={longest_orf['start']}")
        count += 1

if __name__ == "__main__":
    main()
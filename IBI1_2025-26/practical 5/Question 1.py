import matplotlib.pyplot as plt

# Initialize gene expression dictionary
gene_expression = {
    'TP53': 12.4,
    'EGFR': 15.1,
    'BRCA1': 8.2,
    'PTEN': 5.3,
    'ESR1': 10.7,
}
print("Initial gene expression data:")
print(gene_expression)

# Add MYC gene to the dictionary
gene_expression['MYC'] = 11.6
print("\nGene expression data after adding MYC:")
print(gene_expression)

# Extract data for plotting
genes = list(gene_expression.keys())
expression_levels = list(gene_expression.values())

# Create bar chart
plt.figure(figsize=(10, 6), dpi=150)
bars = plt.bar(genes, expression_levels, color='skyblue', edgecolor='black')
plt.title('Gene Expression Levels Comparison', fontsize=14, pad=20)
plt.xlabel('Genes', fontsize=12, labelpad=10)
plt.ylabel('Expression Level', fontsize=12, labelpad=10)

# Add value labels on top of bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 0.2,
             f'{height:.1f}', ha='center', va='bottom', fontsize=10)

plt.ylim(0, max(expression_levels) + 2)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Query gene expression
target_gene = "MYC"  # Modify this variable to query different genes
if target_gene in gene_expression:
    expression = gene_expression[target_gene]
    print(f"\nExpression level of {target_gene}: {expression:.1f}")
else:
    print(f"\nError: Gene {target_gene} not found in the dataset")

# Calculate average gene expression
total_expression = sum(expression_levels)
average_expression = total_expression / len(expression_levels)
print(f"\nAverage gene expression level: {average_expression:.2f}")
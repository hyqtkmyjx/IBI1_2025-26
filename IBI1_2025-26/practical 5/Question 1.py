# Import the pyplot submodule from the matplotlib library (required for plotting)
import matplotlib.pyplot as plt

a = dict() # Initialize an empty dictionary to store gene-expression level mappings

a = {
    'TP53': 12.4,
    'EGFR': 15.1,
    'BRCA1': 8.2,
    'PTEN': 5.3,
    'ESR1': 10.7,
}


print(a)


a['MYC'] = 11.6

# Extract x-axis (gene names) and y-axis (expression levels) data from the dictionary
genes = list(a.keys()) 
expressions = list(a.values())  

# Create and configure a bar chart for gene expression levels
# Set figure size (units: inches)
plt.figure(figsize=(10, 6))
bars = plt.bar(genes, expressions, color='skyblue', edgecolor='black')

plt.title('Compare Gene Expression Levels', fontsize=14, pad=20) 
plt.xlabel('Genes', fontsize=12, labelpad=10)   
plt.ylabel('Expression Level', fontsize=12, labelpad=10)     


for bar in bars:
    height = bar.get_height()  
    plt.text(bar.get_x() + bar.get_width()/2., height + 0.2,
             f'{height:.1f}', ha='center', va='bottom', fontsize=10) #f'{height:.1f}' ；
            # ha='center'：，va='bottom'：

plt.ylim(0, max(expressions) + 2)

plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()

plt.show()

x = input("请输入目标基因名称: ") 
if x in a:
    value = a.get(x)
    print("{x}的表达量为: %.1f" %value)  
else:
    print("目标基因不在列表中")



values = list(a.values())
# sum()
total_expression = sum(values)
# len()
gene_num = len(values)
average_expression = total_expression / gene_num

# Print the average expression level 
print(f"所有基因的平均表达量为：{average_expression:.2f}")

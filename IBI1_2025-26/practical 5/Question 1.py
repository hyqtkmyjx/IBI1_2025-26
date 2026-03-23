# 导入matplotlib的pyplot模块（绘图需要）
import matplotlib.pyplot as plt

a = dict() #建立一个字典

# 填充对映
a = {
    'TP53': 12.4,
    'EGFR': 15.1,
    'BRCA1': 8.2,
    'PTEN': 5.3,
    'ESR1': 10.7,
}

# 输出结果
print(a)

#添加一个新的键值对
a['MYC'] = 11.6

# x轴（key）和y轴（value）
genes = list(a.keys())  # 提取所有key作为x轴
expressions = list(a.values())  # 提取对应value作为y轴

# 创建柱状图
# 设置画布大小(单位为英寸)
plt.figure(figsize=(10, 6))
# 颜色设为天蓝色，边框为黑色
bars = plt.bar(genes, expressions, color='skyblue', edgecolor='black')

# 添加清晰的标注（核心：让图表易读）
plt.title('Compare Gene Expression Levels', fontsize=14, pad=20)  # 图表标题，设置字体大小和上间距
plt.xlabel('Genes', fontsize=12, labelpad=10)    # x轴标签，设置字体大小和下间距
plt.ylabel('Expression Level', fontsize=12, labelpad=10)      # y轴标签，设置字体大小和右间距

# 给每个柱子顶部添加数值标签
for bar in bars:
    height = bar.get_height()  # 获取柱子高度（即表达量）
    # 在柱子顶部居中位置添加数值，保留1位小数，字体大小10
    plt.text(bar.get_x() + bar.get_width()/2., height + 0.2,
             f'{height:.1f}', ha='center', va='bottom', fontsize=10) #f'{height:.1f}' ；格式化字符串，保留1位小数
            # ha='center'：水平对齐方式，va='bottom'：垂直对齐方式

# 调整y轴范围，避免数值标签超出图表
plt.ylim(0, max(expressions) + 2)

# 添加网格线
plt.grid(axis='y', linestyle='--', alpha=0.7)

# 自动调整布局，避免标签重叠
plt.tight_layout()

# 显示图表
plt.show()

#定义一个目标基因变量
x = input("请输入目标基因名称: ") #实现了用户输入功能
if x in a:
    value = a.get(x)
    print("{x}的表达量为: %.1f" %value)  #输出目标基因的表达量
else:
    print("目标基因不在列表中") #错误提示


# 提取所有数值，转为列表
values = list(a.values())
# 计算总和：sum()函数求和
total_expression = sum(values)
# 计算数量：len()函数统计基因个数
gene_num = len(values)
# 计算平均值：总和 ÷ 数量（保留2位小数更美观）
average_expression = total_expression / gene_num

# 3. 打印结果（多种格式，按需选择）
# 格式1：简单直接
print(f"所有基因的平均表达量为：{average_expression:.2f}")

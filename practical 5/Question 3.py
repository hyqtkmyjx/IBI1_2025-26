import matplotlib.pyplot as plt


# 定义嵌套字典
population = {
    '英国': {'2020': 66.7, '2024': 69.2},
    '中国': {'2020': 1426, '2024': 1410},
    '意大利': {'2020': 59.4, '2024': 58.9},
    '巴西': {'2020': 208.6, '2024': 212.0},
    '美国': {'2020': 331.6, '2024': 340.1}
}

population_change = {}  # 定义变化百分比的字典
for country, data in population.items():
    p_2020 = data['2020']
    p_2024 = data['2024']
    change_percent = ((p_2024 - p_2020) / p_2020) * 100
    population_change[country] = round(change_percent, 2) #四舍五入保留两位小数

# 每个国家的人口百分比变化
print("各国人口百分比变化")
for country, percent in population_change.items():
    print(f"{country}: {percent}%")
    

# 按百分比变化从大到小排序
sorted_countries = sorted(population_change.items(), key=lambda x: x[1], reverse=True)
# 排序函数 sorted(..., key=lambda x: x[1], reverse=True) x[1]代表取元组的第二个元素作为排序依据
# true代表降序排列

# 打印排序结果
print("\n 按人口增幅从大到小排序 ")
for idx, (country, percent) in enumerate(sorted_countries, 1):
    print(f"{idx}. {country}:{percent}%")
# enumerate(sorted_countries, 1)函数是添加序号函数，1代表从1开始计数

# 查找增幅最大和降幅最大的国家
max_growth_country = sorted_countries[0][0]
max_growth_percent = sorted_countries[0][1]
min_growth_country = sorted_countries[-1][0]
min_growth_percent = sorted_countries[-1][1]

print(f"\n人口增幅最大的国家:{max_growth_country}({max_growth_percent}%)")
print(f"人口降幅最大的国家：{min_growth_country}({min_growth_percent}%)")

# 提取排序后的国家和百分比数据（用于绘图）
sorted_names = [item[0] for item in sorted_countries]
sorted_percents = [item[1] for item in sorted_countries]

# 设置中文字体（避免乱码）
plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# 创建画布
plt.figure(figsize=(10, 8))

# 绘制柱状图（区分增长/下降的柱子颜色）
colors = ['#2E8B57' if p >= 0 else '#DC143C' for p in sorted_percents]  # 增长=深绿，下降=深红
bars = plt.bar(sorted_names, sorted_percents, color=colors, edgecolor='black', width=0.6)

# 添加标注：标题、轴标签
plt.title('2020-2024年各国人口百分比变化', fontsize=14, pad=20)
plt.xlabel('国家', fontsize=12, labelpad=10)
plt.ylabel('人口百分比变化（%）', fontsize=12, labelpad=10)


# 添加水平参考线（0轴），更清晰区分增长/下降
plt.axhline(y=0, color='black', linestyle='-', linewidth=0.8)

# 添加网格线（y轴），提升可读性
plt.grid(axis='y', linestyle='--', alpha=0.7)

# 自动调整布局，避免标签重叠
plt.tight_layout()

# 显示图表
plt.show()
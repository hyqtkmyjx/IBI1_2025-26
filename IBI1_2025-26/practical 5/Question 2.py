import matplotlib.pyplot as plt

a = [72, 60, 126, 85, 90, 59, 76, 131, 88, 121, 64] #定义一个列表
num = len(a) #计算列表的长度
print("患者人数：", num) #输出患者人数
total = sum(a) #计算列表中所有元素的和
average = total / num #计算平均值
print("平均心率：", average) #输出平均心率

low = 0
normal = 0
high = 0

for i in range(num): #遍历列表中的每个元素
    if a[i] < 60:
        low += 1 #统计心率偏低的患者人数
    elif a[i] > 60 and a[i] < 120:
        normal += 1 #统计心率正常的患者人数
    else:
        high += 1 #统计心率偏高的患者人数

print("心率偏低的患者人数：", low) #输出心率偏低的患者人数
print("心率正常的患者人数：", normal) #输出心率正常的患者人数
print("心率偏高的患者人数：", high) #输出心率偏高的患者人数

if low > normal and low > high:
    print("心率偏低的患者人数最多") 
elif normal > low and normal > high:
    print("心率正常的患者人数最多") 
else:    print("心率偏高的患者人数最多") 

import matplotlib.pyplot as plt

# 绘制饼图
plt.figure(figsize=(8, 8))  # 设置饼图画布大小


labels = ['low(<60)', 'normal(60-120)', 'high(>120)']
sizes = [low, normal, high]  # 核心：使用你统计好的变量
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1']  # 自定义颜色（红/青/蓝）
explode = (0.05, 0, 0.05)  # 突出显示偏低/偏高类别，增强视觉效果


# 核心：绘制饼图
# autopct：显示百分比（保留1位小数）
# explode：突出指定扇区
# colors：自定义扇区颜色
# shadow：添加阴影（增强立体感）
# startangle：饼图起始角度（140度更美观）
wedges, texts, autotexts = plt.pie(
    sizes,
    labels=labels,
    colors=colors,
    explode=explode,
    autopct='%1.1f%%',
    shadow=True,
    startangle=140,
    textprops={'fontsize': 11}  # 标签文字大小
)

# 优化百分比文字样式（让百分比更清晰）
for autotext in autotexts:
    autotext.set_color('white')  # 百分比文字颜色
    autotext.set_fontsize(10)    # 百分比文字大小
    autotext.set_weight('bold')  # 百分比文字加粗

# 第六步：添加图表标注（让图表更易理解）
plt.title('figure', fontsize=14, pad=20)  # 图表标题
plt.legend(
    wedges, 
    [f'{label}: {size}people' for label, size in zip(labels, sizes)],
    title="figure",
    loc="center left",
    bbox_to_anchor=(1, 0, 0.5, 1)  # 图例放在饼图右侧
)

# 自动调整布局（避免标签/图例重叠）
plt.tight_layout()

# 显示饼图
plt.show()
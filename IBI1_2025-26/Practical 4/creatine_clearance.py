# 程序开始
# 定义常量：最大年龄、体重范围、肌酐范围、性别常量
age = 100                     # 年龄上限
weightmax = 80                # 体重上限
weightmin = 20                 # 体重下限
Crmax = 100                   # 血清肌酐上限
Crmin = 0                     # 血清肌酐下限
gentle1 = "male"               # 男性标识
gentle2 = "female"             # 女性标识

# 输入部分
# 提示用户输入年龄、体重、性别、血清肌酐值，并转换为相应类型
a = int(input("Enter your age: "))
b = int(input("Enter your weight: "))
c = input("Enter your gender: ")
Cr = int(input("Enter your serum creatinine level: "))

# 判断输入值是否超出正常范围
# 如果年龄超过上限，或体重超出范围，或肌酐超出范围，或性别既不是男性也不是女性，则提示异常
if a > age or b > weightmax or b < weightmin or Cr > Crmax or Cr < Crmin or c != gentle1 and c != gentle2 :
    print("Your creatine clearance is not normal")
else:
    # 输入值均在正常范围内，开始计算肌酐清除率
    if c == gentle1:
        # 男性计算公式：(140 - 年龄) * 体重 / (72 * 血清肌酐)
        CrCl = ((140 - a) * b) / (72 * Cr)
    else:
        # 女性计算公式：男性结果 * 0.85
        CrCl = ((140 - a) * b) / (72 * Cr) * 0.85
    # 输出计算结果，保留四位小数
    print("Your creatine clearance is %.4f" % CrCl)
# 程序结束
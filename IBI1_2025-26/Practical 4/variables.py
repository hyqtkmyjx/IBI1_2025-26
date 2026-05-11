# Calculate differences between consecutive values
num = 10000
a = 508 * num
b = 533 * num
c = 555 * num
d = b - a
e = c - b
# Result comparison: d = 250000, e = 220000 → d > e → decelerating
if d > e:
    print("It is decelerating")
else:
    print("It is accelerating")

# Boolean logic test
x = True
y = False
# Truth table for OR operation:
# x | y | w
# T | T | T
# T | F | T
# F | T | T
# F | F | F
w = x or y
print(w)
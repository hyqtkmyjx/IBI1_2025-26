num = 10000
a = 508 * num
b = 533 * num
c = 555 * num
d = b - a
e = c - b
if d > e:
    print("It is decelerating")
else:    print("It is accelerating")

x = True
y = False
w = x or y
print(w)
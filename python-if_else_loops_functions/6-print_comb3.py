#!/usr/bin/python3
for i in range(0, 89):
    if (i % 10 <= i / 10):
        continue
    print("{:02d}, ".format(i), end="")
print("{}".format(i + 1))

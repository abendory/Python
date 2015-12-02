def increment(y):
    if y == 0:
        return 1
    if y % 2 == 1:
        return 2 * increment(y // 2)
    else:
        return (y + 1)

for i in range(10):
    print(increment(i) == i+1, end=" ")
print()

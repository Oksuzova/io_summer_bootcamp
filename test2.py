l1 = [1, 2, 3]

l2 = [x for x in l1 if x >= 2 for i in range(10) if i > 5]

print(l2)

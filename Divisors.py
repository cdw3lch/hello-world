num = input("Enter an integer number: ")
x = range(1, int(num) + 1)
factors = []
for elem in x:
    if int(num) % elem == 0:
        factors.append(elem)
print(factors)



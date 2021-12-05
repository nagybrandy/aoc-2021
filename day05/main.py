maxint = 10
def printsys(sys):
    for i in range(maxint):
        for j in range(maxint):
            print(sys[i][j], end="")
        print()
numbers = []
f=open("sample.txt","r")
for line in f:
    twopoints = line.split("->")
    twopoints.pop(1)
    for e in twopoints:
        numbers.append(e.split(","))
    numbers = [[int(a) for a in x] for x in numbers]
print(numbers)

csystem = [["." for x in numbers] for a in numbers]
printsys(csystem)
for i in range(maxint):
    for j in range(maxint):
        X
        for k in range(numbers[i][j], numbers[i+1][j]):
            
#for point in numbers:
    
maxint = 1000
def printsys(sys):
    for i in range(maxint):
        for j in range(maxint):
            print(sys[i][j], end="")
        print()
numbers = []
f=open("data.txt","r")

def cordinates(first, second):
  x = []
  for i in range(first, second+1 if first < second else second-1, 1 if first < second else -1):
    x.append(i)
  return x
  
for line in f:
    twopoints = line.split("->")
    for e in twopoints:
        numbers.append(e.split(","))
    numbers = [[int(a) for a in x] for x in numbers]

#print(numbers)

csystem = [["." for x in numbers] for a in numbers]
for i in range(0,maxint,2):
  x = []
  y = []
  cordy1 = numbers[i][0]
  cordy2 = numbers[i+1][0]
  cordx1 =  numbers[i][1]
  cordx2 =  numbers[i+1][1]
  #print(cordx1,cordx2,cordy1,cordy2)
  # print(cordinates(cordx1,cordx2), cordinates(cordy1,cordy2))
  x = cordinates(cordx1,cordx2)
  y = cordinates(cordy1,cordy2)
  horizontal = True if len(x) == 1 else False
  vertical = True if len(y) == 1 else False
  if horizontal:
    for i in range(len(y)):
      if csystem[x[0]][y[i]] == ".":
        csystem[x[0]][y[i]] = 1
      else:
        csystem[x[0]][y[i]] += 1
  if vertical:
    for i in range(len(x)):
      if csystem[x[i]][y[0]] == ".":
        csystem[x[i]][y[0]] = 1
      else:
        csystem[x[i]][y[0]] += 1
  if not vertical and not horizontal:
    for i in range(len(x)):
      if csystem[x[i]][y[i]] == ".":
        csystem[x[i]][y[i]] = 1
      else:
        csystem[x[i]][y[i]] += 1
  #for i in range(len(x)):
#printsys(csystem)
counter = 0
for i in range(maxint):
  for j in range(maxint):
    if csystem[i][j] != "." and int(csystem[i][j]) > 1:
      counter += 1

print(counter)
#for point in numbers:
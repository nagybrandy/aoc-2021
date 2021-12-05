numbers = []
f=open("sample.txt","r")
numbers = [int(i) for i in f.readline().split(",")]
tables = []
for line in f:
  if line != "\n":
    tables.append([int(i) for i in line.split()])
 
bingocounter = []
tcount = len(tables) // 5
for i in range(tcount):
  bingocounter.append(False)
def bingochecker(number):
  
  # verybingo = False
  
  # every table
  for i in range(tcount):
    # rows
    for j in range(5):
      if tables[i*5 + j].count(True) == 5:
        #verybingo = True
        bingocounter[i] = True
    # cols
    for j in range(5):
      column = []
      for k in range(5):
        column.append(tables[i*5 + k][j])
      if column.count(True) == 5:
        #verybingo = True
        bingocounter[i] = True
    if bingocounter.count(True) == tcount:
      unmarkeds = []
      for u in range(5):
        for t in range(5):
         if not isinstance(tables[i*5+u][t],bool):
           unmarkeds.append(tables[i*5+u][t])
      print(sum(unmarkeds)*number)
      print(number)
      print(unmarkeds, sum(unmarkeds))
      print(i)
      print(tables[i*5],tables[i*5+1],tables[i*5+2],tables[i*5+3],tables[i*5+4])
      exit(0)
  

for number in numbers:
  for i in range(len(tables)):
    for j in range(len(tables[0])):
      if number == tables[i][j]:
        tables[i][j] = True
        #print(number)
        bingochecker(number)
        
print(numbers)
print(tables[0].count(True))
print(tables)
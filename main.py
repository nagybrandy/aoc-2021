lines = []
numbers = []
f=open("data.txt","r")

for line in f:
    numbers.append(int(line))

print(numbers)
counter = 0
for i in range(0, len(numbers)-2):
  if numbers[i+1] > numbers[i]:
    counter += 1
    
print(counter)
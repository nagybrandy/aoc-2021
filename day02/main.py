numbers=[]
f=open("data.txt","r")
for data in f:
    numbers.append(data.split())

depth = 0;
horizontal = 0
aim = 0
for i in range(0, len(numbers)):
  if numbers[i][0] == "down":
  #  depth -= int(numbers[i][1])
    aim += int(numbers[i][1])
  elif numbers[i][0] == "up":
   # depth += int(numbers[i][1])
    aim -= int(numbers[i][1])
  elif numbers[i][0] == "forward":
    horizontal += int(numbers[i][1])
    depth += aim * int(numbers[i][1])

print(horizontal*depth)
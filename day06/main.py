fish = [int(i) for i in open("data.txt","r").readline().split(",")]
fc = []
for i in range(9):
  fc.append(fish.count(i))

for i in range(256):
  new=fc[0]
  fc[7] += new
  fc.append(new)
  fc.pop(0)
print(sum(fc))
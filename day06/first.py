fishes = [line.strip().split(",") for line in open("sample.txt")]
fishes = [int(a) for a in fishes[0]]

daycounter = 0
for j in range(256):
  for i in range(len(fishes)):
    fishes[i] -= 1
    if fishes[i] == -1:
      fishes[i] = 6
      fishes.append(8)
  daycounter += 1
  fishes.sort()
  #print("After day", daycounter, ":" , fishes)

print(len(fishes))
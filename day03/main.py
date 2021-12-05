numbers = []
f=open("sample.txt","r")
for line in f:
    numbers.append(line)
bitlength = 5
gamma = ""
epsilon = ""

def common(numbers, most):
  gamma = ""
  epsilon = ""
  count01 = []
  for i in range(0,bitlength):
    temp = []
    counter0 = 0
    counter1 = 0
    for j in range(0, len(numbers)-1):   
      if numbers[j][i] == "0":
        counter0 += 1
      else:
        counter1 += 1
    temp.append(counter0)
    temp.append(counter1)
    count01.append(temp)

  for e in count01:
    if e[0] > e[1]:
      gamma += "0"
      epsilon += "1"
    elif e[0] < e[1]:
      gamma += "1"
      epsilon += "0"
    elif e[0] == e[1]:
      if gamma:
        gamma += "1"
      else:
        epsilon += "1"
  if most:
    return gamma
  else:
    return epsilon


# first
gamma = common(numbers, True)
epsilon = common(numbers, False)

print(int(gamma,2) * int(epsilon,2))
# print(type(gamma), epsilon, type(numbers[0]))
result = numbers.copy()

for i in range(bitlength):
  gamma = common(result, True)
  result = [a for a in result if a[i] == gamma[i]]
  if len(result) == 1:
    first = result[0]

result = numbers.copy()
for i in range(bitlength):
  epsilon = common(result, False)
  result = [a for a in result if a[i] == epsilon[i]]
  print(epsilon)
  print(result)
  if len(result) == 1:
    second = result[0]

print(gamma, epsilon)
print(int(first,2), int(second,2))
print(int(first,2) * int(second,2))
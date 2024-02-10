target = int(input())

value = 0
for number in range(2, target + 1, 2):
  #print(value)
  value += number

print(value)
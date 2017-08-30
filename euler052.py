# Problem 52: Permuted multiples
# It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.
# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
i=1
while True:
  i+=1
  si = ''.join(sorted(str(i)))
  found=True
  for j in range(6,1,-1):
    sj = ''.join(sorted(str(j*i)))
    if len(si)<len(sj):
      i=10**(len(si)+1)-1
      found=False
      break
    if si!=sj:
      found=False
      break
  if found:
    print(i)
    break
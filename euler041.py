# Problem 41: Pandigital prime
#We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital 
#and is also prime.
# What is the largest n-digit pandigital prime that exists?

# Generate all pandigital numbers
pandigitals = []
for maxnum in range(3,11):
  L = list(range(1,maxnum))
  pandigitals.append(int(''.join(map(str,L))))
  while True:
    for x in range(len(L)-2,-1,-1):
      if L[x]<L[x+1]:
        break
    if x==0 and L[x]>L[x+1]:
      break
    for y in range(len(L)-1,-1,-1):
      if y==x: 
        continue
      if L[x]<L[y]:
        break
    L[x],L[y]=L[y],L[x]
    tmp = L[x+1:]
    L[x+1:] = tmp[::-1]
    pandigitals.append(int(''.join(map(str,L))))
N = max(pandigitals)
pandigitals = sorted(pandigitals)
# Check for primality the simple way
while pandigitals:
  p = pandigitals.pop()
  for d in range(2,p//2+1):
    if p%d==0:
      break
  if p%d!=0:
    break
print(p)
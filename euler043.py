# Problem 43: Substring divisibility
# The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting 
# sub-string divisibility property.
# Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:
# d2d3d4=406 is divisible by 2
# d3d4d5=063 is divisible by 3
# d4d5d6=635 is divisible by 5
# d5d6d7=357 is divisible by 7
# d6d7d8=572 is divisible by 11
# d7d8d9=728 is divisible by 13
# d8d9d10=289 is divisible by 17
# Find the sum of all 0 to 9 pandigital numbers with this property.

# Generate all pandigital numbers
pan = [[0,1,2,3,4,5,6,7,8,9]]
L = list(range(10))
while True:
  L = list(pan[-1])
  for x in range(len(L)-2,-1,-1):
    if L[x]<L[x+1]:
      break
  if x==0 and L[x]>=L[x+1]:
    break
  for y in range(len(L)-1,-1,-1):
    if y==x: 
      continue
    if L[x]<L[y]:
      break
  L[x],L[y]=L[y],L[x]
  tmp = L[x+1:]
  L[x+1:] = tmp[::-1]
  pan.append(L)
pan = [''.join(map(str,p)) for p in pan]
S = 0
N = [2,3,5,7,11,13,17]
for p in pan:
  S += int(p)
  for i,n in enumerate(N):
    if int(p[i+1:i+4])%n!=0:
      S-=int(p)
      break
print(S)
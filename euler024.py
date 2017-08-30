# Problem 24: Lexicographic permutations
# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are 
# listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
# 012   021   102   120   201   210
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
L = list(range(10))
for _ in range(1000000-1):
  for x in range(len(L)-2,-1,-1):
    if L[x]<L[x+1]:
      break
  for y in range(len(L)-1,-1,-1):
    if y==x: 
      continue
    if L[x]<L[y]:
      break
  L[x],L[y]=L[y],L[x]
  tmp = L[x+1:]
  L[x+1:] = tmp[::-1]
print(''.join(map(str,L)))
    
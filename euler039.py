# Problem 39: Integer right triangles
# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.
# {20,48,52}, {24,45,51}, {30,40,50}
# For which value of p ≤ 1000, is the number of solutions maximised?
pmax = 1000
maxnum,maxp = 0,0
for p in range(2,pmax+1):
  num = 0
  for a in range(1,p//2):
    b = (p**2-2*p*a)/(2*p-2*a)
    if b!=int(b) or b<0:
      continue
    b = int(b)
    c = p-a-b
    if c**2==a**2+b**2:
      num += 1
  if num>maxnum:
    maxnum = num
    maxp = p
print(maxp)
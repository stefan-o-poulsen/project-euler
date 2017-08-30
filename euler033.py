# Problem 33: Digit cancelling fractions
# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that #
# 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
# There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator 
# and denominator.
# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
frac = []
for denom in range(10,100):
  d = [int(s) for s in str(denom)]
  if d[0]==0 or d[1]==0:
    continue
  for num in range(10,denom):
    n = [int(s) for s in str(num)]
    if n[0]==0 or n[1]==0:
      continue
    t = num/denom
    if (n[0]==d[0] and t==n[1]/d[1]) or (n[1]==d[1] and t==n[0]/d[0]) or (n[0]==d[1] and t==n[1]/d[0]) or (n[1]==d[0] and t==n[0]/d[1]): 
      frac.append((num,denom))
n,d=frac[0][0],frac[0][1]     
for i in range(1,len(frac)):
  n *= frac[i][0]
  d *= frac[i][1]
i = 2
while i<=n:
  if n%i==0 and d%i==0:
    n//=i
    d//=i
  else:
    i+=1
print(d)    
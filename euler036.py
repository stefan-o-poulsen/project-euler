# Problem 36: Double-base palindromes
# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
# (Please note that the palindromic number, in either base, may not include leading zeros.)
def ispalin(s):
  s = str(s)
  for i in range(len(s)//2+1):
    if s[i]!=s[-i-1]:
      return False
  return True
def tobin(s):
  d = []
  while s!=0:
    d.append(s%2)
    s//=2
  return ''.join(map(str,d))
print(sum([i for i in range(1,1000000) if ispalin(i) and ispalin(tobin(i))]))
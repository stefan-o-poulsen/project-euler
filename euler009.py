# Problem 9: Special Pythagorean triplet
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
target = 1000
def solve():
  for a in range(1,target):
    for b in range(a+1,target):
      c = target - a - b
      if c <= b:
        break
      if a**2+b**2 == c**2:
        return a*b*c
print(solve())
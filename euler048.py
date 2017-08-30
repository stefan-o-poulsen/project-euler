# Problem 48: Self powers
# The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
S = 1
for s in range(2,1001):
  S += s**s
print(str(S)[-10:])
# Problem 4: Largest palindrome product
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
N = sorted([i*j for i in range(100,1000) for j in range(100,i+1)],key=lambda x:-x)
for n in N:
  s = str(n)
  if s[:len(s)//2] == s[:-len(s)//2-1:-1]:
    print(s)
    break
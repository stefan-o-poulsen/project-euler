# Solution to Project Euler question 205
# Stefan Othmar Poulsen, 2017
# Tested in Python 3.5.2
import math

def factorial(N):
  if N<=1: return 1
  else: return factorial(N-1)*N

def nchoosek(n,k):
  return factorial(n)/(factorial(n-k)*factorial(k))

def prob(p,n,s):
  """Probability is taken from Mathworld, dice page. p is roll, n is number of dice and s is sides to each dice"""
  P = 0
  lim = math.floor((p-n)/s)
  for k in range(lim+1):
    P += ((-1.0)**k)*nchoosek(n,k)*nchoosek(p-s*k-1,n-1)
  P = P/s**n
  return P

pdfP = [0]*(37)
pdfC = [0]*(37)
for i in range(37):
  pdfP[i] = prob(i,9,4)
  pdfC[i] = prob(i,6,6) 
  
P = 0.0
# Sum over independent probabilities where i>j
for i in range(9,len(pdfP)):
  for j in range(i):
    P += pdfP[i]*pdfC[j]
    
print("Probability that Pete wins is",P)
  
  
  
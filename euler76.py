# Solves Project Euler question 76
# Stefan Othmar Poulsen, 2017
# Tested in Python 3.5.2

import math

def count(N,M,Nlast):
	"""Counts number of ways to uniquely distribute N identical items in up to M identical slots.
	Nlast is the number in last slot."""
	S = 0
	# Edge cases: last bin  
	if M==1:
		if N<=Nlast: return 1
		else: return 0
	# All items distributed
	if N == 0: return 1
	nmax = min(Nlast,N)
	#print(N,M,nmax)
	# Place this number in first bin
	for num in range(nmax,0,-1):
		s = count(N-num,M-1,num)
		if s==0:
			return S
		S += s
	return S

def main():
  N = 100

  S = 0
  for M in range(2,N+1):
    S += count(N-M,M,N-M)
  print("Number of ways to write",N,"as the sum of two or more integers is",S)

if __name__ == '__main__':
  main()
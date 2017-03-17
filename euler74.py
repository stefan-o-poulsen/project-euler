# Solves Project Euler question 74
# Stefan Othmar Poulsen, 2017
# Tested in Python 3.5.2

def getdigits(N):
  """Returns digits of number in reverse order"""
  digits = []
  while N > 0:
    d = N % 10
    N = (N-d) // 10
    digits.append(d)
  return digits

def factorial(N):
  if N<=1: return 1
  else: return factorial(N-1)*N

# Setup required factorials
fac = [factorial(n) for n in range(10)]

def getchain(N):
  chain = {N:True}
  while True:
    s = 0
    d = getdigits(N)
    while d: s += fac[d.pop()]
    if chain.get(s):
      return chain
    else:
      chain[s] = True
      N = s
      
def main():
  Nmax = 1000000
  target = 60

  count = 0
  for i in range(1,Nmax):
    if len(getchain(i))==target:
      count += 1 
  print("Number of chains of length",target,"is",count)

if __name__ == '__main__':
  main()

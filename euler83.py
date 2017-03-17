# Solution to Project Euler question 83
# Stefan Othmar Poulsen, 2017
# Tested in Python 3.5.2
# Variant of Dijkstras algorithm, very inefficient implementation
import numpy as np

def read_matrix():
  fn = 'matrix_pe83.txt'
  f = open(fn,'r')
  lines = [line.rstrip('\n') for line in f]
  f.close()
  M = []
  for line in lines:
    M += map(int,line.split(','))
  M = np.array(M)  
  M = np.reshape(M,(80,80))
  return M

M = read_matrix()
N = np.zeros(M.shape)

num = 0
m = []
for col in range(M.shape[1]):
  for row in range(M.shape[0]):
    N[row,col] = num
    m.append(M[row,col])
    num += 1
    
ledge = []
redge = []
for col in range(M.shape[1]):
  for row in range(M.shape[0]):
    conn = []
    if row<M.shape[0]-1:
      ledge.append(int(N[row,col]))
      redge.append(int(N[row+1,col]))
    if col<M.shape[1]-1:
      ledge.append(int(N[row,col]))
      redge.append(int(N[row,col+1]))

# Sum vector
s = [0]*len(m)
s[0] = m[0]

# Add first vertex to list
P = [0]
aledge = []
aredge = []

while s[-1]==0.0:
  # Transfer edges to list of active edges
  for i in range(len(ledge)-1,-1,-1):
    if P[-1] == ledge[i] or P[-1] == redge[i]:
      aledge.append(ledge.pop(i))
      aredge.append(redge.pop(i))
  
  I=S=np.inf
  for i in range(len(aledge)):
    if s[aledge[i]]==0.0:
      ss = m[aledge[i]]+s[aredge[i]]
      toadd = aledge[i]
    else:
      ss = s[aledge[i]]+m[aredge[i]]
      toadd = aredge[i]
    if ss<S:
      S = ss
      I = toadd
  # Mark value and transfer vertex
  s[I] = S
  P.append(I)    

  # Remove inactive edges
  for i in range(len(ledge)-1,-1,-1):
    if s[ledge[i]]>0.0 and s[redge[i]]>0.0:
      ledge.pop(i)
      redge.pop(i)
  for i in range(len(aledge)-1,-1,-1):
    if s[aledge[i]]>0.0 and s[aredge[i]]>0.0:
      aledge.pop(i)
      aredge.pop(i)    
    
print("Shortest path is ",s[-1])
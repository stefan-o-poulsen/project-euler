# Problem 31: Coin sums
# In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:
# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
# It is possible to make £2 in the following way:
# 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# How many different ways can £2 be made using any number of coins?

values = [200,100,50,20,10,5,2]
target = 200
# Use recursive function to determine number
def count(target,denominations):
  if not denominations:
    return 1
  s = 0
  for d in range(target//denominations[0]+1):
    s += count(target-d*denominations[0],denominations[1:])
  return s
print(count(target,values))  
# Problem 17: Number letter counts
# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in # total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

def num_to_str(n):
  nums = {1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten",11:"eleven",12:"twelve",
        13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen",20:"twenty",
        30:"thirty",40:"forty",50:"fifty",60:"sixty",70:"seventy",80:"eighty",90:"ninety"}
  suffix = {3:"",2:"",1:"hundred",0:"thousand"}
  numlist = [int(s) for s in str(n)]
  while len(numlist)<4:
    numlist = [0] + numlist
  numlist[2] = 10*numlist[2]
  if numlist[2]==10:
    numlist[2] += numlist[3]
    numlist[3] = 0
  s = []
  for i in range(len(numlist)):
    if numlist[i]==0: continue
    if s and (i==2 or (i==3 and numlist[2]==0)):
      s.append("and")
    s.extend([nums[numlist[i]],suffix[i]])
  s = [x for x in s if x]
  return " ".join(s)

n = 0
for num in range(1,1001):
  s = num_to_str(num)
  n += len(s) - s.count(' ')
print(n)
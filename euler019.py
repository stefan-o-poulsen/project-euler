# Problem 19: Counting Sundays
# You are given the following information, but you may prefer to do some research for yourself.
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
dim = list(days_in_month)
day = 0
date = [0,0,1900]
n = 0
while date[2]<2001:
  day = (day+1)%7
  date[0]+=1
  if date[0]==dim[date[1]]:
    date[0]=0
    date[1]+=1
  if date[1]==12:
    date[1]=0
    date[2]+=1
    dim = list(days_in_month)
    if date[2]%4==0 and (date[2]%100!=0 or date[2]%400==0):
      dim[1]+=1
  if date[2]>1900 and day==6 and date[0]==0:
    n+=1
print(n)
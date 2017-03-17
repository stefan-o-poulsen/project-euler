# Solves Project Euler question 493
# Stefan Othmar Poulsen, 2017
# Tested in Python 3.5.2

import math

num_colors = 7
num_in_colors = 10
num_draw = 20
num_balls = num_colors*num_in_colors

def main():
  # Linearity of expectation with indicator random variables.
  # Probability could be written with factorials, but this works too.
  P = 1.0
  for i in range(20):
    P *= (num_balls-num_in_colors-i)/(num_balls-i)
  E = num_colors*(1.0-P)
  print("Expected value is",E)

if __name__ == '__main__':
  main()
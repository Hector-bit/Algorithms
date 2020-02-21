#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  if n < 0:
    return []
  elif n == 0: 
    return []
  else:
    value = [rock_paper_scissors(n - 1)], [rock_paper_scissors(n - 2)]
    return value



if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')
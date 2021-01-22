import sys

# set a and d to the 1st and 2nd command-line argument values
a = int(sys.argv[1])
d = int(sys.argv[2])

# the divistion algorithm on slide 49
r = a; q = 0
while r >= d:
  r = r - d
  q = q + 1

print('--------', q,r)


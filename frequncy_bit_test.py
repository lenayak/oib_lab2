import math

from info import sequence, N


sequence1 = sequence
sequence2 = []
for i in sequence:
    if i == 1:
        sequence2.append(i)
    elif i == 0:
        sequence2.append(-1)

# print(sequence2)
# [1, 1, 1, 1, 1, 1, 1, -1, -1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, -1, -1, 1, 1, -1, 1, -1, 1, -1, 1, -1, -1, 1, 1, 1, 1, 1, 1, -1, 1, -1, 1, 1, 1, -1, 1, -1, 1, -1, -1, -1, 1, -1, 1, 1, -1, -1, -1, 1, -1, 1, 1, -1, -1, 1, 1, 1, 1, -1, -1, -1, -1, 1, 1, 1, 1, -1, -1, 1, 1, 1, 1, 1, -1, 1, -1, -1, -1, 1, -1, -1, 1, 1, 1, -1, 1, -1, 1, -1, -1, 1, 1, -1, 1, -1, 1, 1, -1, -1, -1, -1, 1, 1, -1, 1, 1, 1, -1, 1, 1, -1, -1, 1, 1, 1, 1, 1, 1, -1]

s = sum(sequence2)/math.sqrt(N)
print(s)
# 2.2980970388562794
P = math.erfc(s/math.sqrt(2))
print(P)
# 0.021556266760016346 > 0.01
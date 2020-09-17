import math
PV = 10000


i = 0.10
n = 30.0 * 12
PMT = 120.0

FVA = PMT * ((math.pow(1 + i, n) - 1) / (i / n))
print(FVA)

#120 * (((1 + 0.1)^30 - 1) / 0.1)
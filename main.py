import ecurve as ec

E = ec.ECurve(p=31, a=-3, b=1)

P = E.point(19, 18)
Q = E.point(25, 19)

R, m = P + Q
print(f'P + Q\t= {-R}, m = {m}') # P + Q = (12, 9), m = 26

R, m = P ** 2
print(f'P ** 2\t= {-R}, m = {m}') # P ** 2 = (25, 19), m = 30

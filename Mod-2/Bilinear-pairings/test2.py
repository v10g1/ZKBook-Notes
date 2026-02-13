from py_ecc.bn128 import G1, G2, eq, curve_order, multiply, eq, curve_order, add

x = 10 # chosen randomly
assert eq(multiply(G2, x + curve_order), multiply(G2, x))
assert eq(multiply(G1, x + curve_order), multiply(G1, x))
print(eq(add(G1, G1), multiply(G1, 2)))
# True
print(eq(add(G2, G2), multiply(G2, 2)))
# True
print(G1+G1+G1== G1*3)
print(eq(add(add(G1, G1), G1), multiply(G1, 3)))
# aiger circuit
# aiger SAT solver
# aiger CNF Convertor

import aiger
from aiger_sat import SolverWrapper
from aiger_cnf import aig2cnf
from pysat.formula import CNF

# Input Variable 
a = []
b = []
for i in range(4):
    a.append(aiger.atom("a" + str(i)))
    b.append(aiger.atom("b" + str(i)))
c = [aiger.atom("c0")] + [None] * 4


# RCA[4:1]
RCA = [None] * 5
# RCA Equation:
for i in range(4):
    c[i + 1] = (a[i] & b[i]) | (c[i] & (a[i] ^ b[i]))
RCA = c

"""
CLA Circuits
"""
CLA = [None] * 5
p = [None] * 4
g = [None] * 4

# CLA Equations:
# Bit propagate and generate equations:
for i in range(4):
    p[i] = a[i] | b[i]
    g[i] = a[i] & b[i]
# Group propagate and generate equations:
P_1_0 = p[1] & p[0]
P_3_2 = p[3] & p[2]
P_3_0 = P_3_2 & P_1_0
G_1_0 = g[1] | (p[1] & g[0])
G_3_2 = g[3] | (p[3] & p[2])
G_3_0 = G_3_2 | (P_3_2 & G_1_0)
# Carry equations
CLA[1] = g[0] | (p[0] & c[0])
CLA[2] = G_1_0 | (P_1_0 & c[0])
CLA[3] = g[2] | (p[2] & CLA[2])
CLA[4] = G_3_0 | (P_3_0 & c[0])

# RCA xor CLA 
xor = RCA[1] ^ CLA[1]
xor = xor & (RCA[2] ^ CLA[2])
xor = xor & (RCA[3] ^ CLA[3])
xor = xor & (RCA[4] ^ CLA[4])

# Convert AIG circuits into CNF
cnf = aig2cnf(xor.aig)

# output cnf file
f = CNF(from_clauses=cnf.clauses)
f.to_file("h4p1.cnf")

# Aig Solver wrapper for PySAT solver
solver = SolverWrapper()  # defaults to Glucose4
solver.add_expr(xor)

if solver.is_sat():
    print("The CNF formula is SAT. The two designs are not equivalent.")
else:
    print("The CNF formula is UNSAT. The two designs are equivalent.")
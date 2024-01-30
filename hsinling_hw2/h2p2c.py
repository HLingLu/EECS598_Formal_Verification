# repycudd demo1: basic BDD manipulation

import repycudd	# Python wrapper for CUDD
import sym_dot	# Utility to map variable numbers to their names (fragile: written by FA2020 EECS598 student)
import os

# Access to BDD operations must be through a so-called BDD manager.
# The following instruction creates a manager called mgr.
mgr = repycudd.DdManager()

s0 = mgr.IthVar(0)
s1 = mgr.IthVar(1)
s2 = mgr.IthVar(2)
t0 = mgr.IthVar(3)
t1 = mgr.IthVar(4)
t2 = mgr.IthVar(5)

var_names = ["s0", "s1", "s2", "t0", "t1", "t2"]

# function
def AndAll(*args):
    symbols = [e for e in args]
    while len(symbols) > 1:
        symbols.append(mgr.And(symbols.pop(), symbols.pop()))
    return symbols.pop()

def OrAll(*args):
    symbols = [e for e in args]
    while len(symbols) > 1:
        symbols.append(mgr.Or(symbols.pop(), symbols.pop()))
    return symbols.pop()

E1 = AndAll(mgr.Not(s2), mgr.Not(s1), mgr.Not(s0), mgr.Not(t2), t0)     # s2' s1' s0' t2' t0
E2 = AndAll(mgr.Not(s2), mgr.Not(s1), s0, mgr.Not(t2))                  # s2' s1' s0  t2'
E3 = AndAll(s1, mgr.Not(s0), t1, t0)                                    # s1  s0' t1  t0
E4 = AndAll(s2, mgr.Not(s1), mgr.Not(t2), t1, t0)                       # s2  s1' t2' t1  t0
E5 = AndAll(s2, mgr.Not(s1), s0, t2, mgr.Not(t0))                       # s2  s1' s0  t2  t0'
E6 = AndAll(s2, mgr.Not(s1), mgr.Not(s0), t2, mgr.Not(t1), t0)          # s2  s1' s0' t2  t1' t0

E = OrAll(E1, E2, E3, E4, E5, E6)

# Symbolic Reachability
Source_Vertices = AndAll(s0, s1, s2)
Source_array = repycudd.DdArray(mgr, 3)
Target_array = repycudd.DdArray(mgr, 3)
Source_array.Push(s2)
Source_array.Push(s1)
Source_array.Push(s0)
Target_array.Push(t2)
Target_array.Push(t1)
Target_array.Push(t0)

R1 = mgr.Not(s2)
R2 = mgr.And(s0, mgr.Or(s2, s1))

N = R1
# Forward image iteration for R1
while(N != mgr.Zero()):
	C = N
	Img = mgr.AndAbstract(C, E, Source_Vertices)
	Img = mgr.SwapVariables(Img, Source_array, Target_array, 3)
	N = mgr.And(Img, mgr.Not(R1))
	R1 = mgr.Or(R1, Img)
     
N = R2
# Forward image iteration for R2
while(N != mgr.Zero()):
	C = N
	Img = mgr.AndAbstract(C, E, Source_Vertices)
	Img = mgr.SwapVariables(Img, Source_array, Target_array, 3)
	N = mgr.And(Img, mgr.Not(R2))
	R2 = mgr.Or(R2, Img)


farray = repycudd.DdArray(mgr,2)
farray.Push(mgr.BddToAdd(R1))
farray.Push(mgr.BddToAdd(R2))
fcn_names = ["R1", "R2"]

mgr.DumpDotArray(farray, "h2p2c.dot")
sym_dot.sym_dot_manager("h2p2c.dot", var_names, fcn_names).add_syms()
# os.system("dot -Tpng {0} -o {1}".format("h2p2c.dot", "h2p2c.png"))
os.system("dot -Tpdf {0} -o {1}".format("h2p2c.dot", "h2p2c.pdf"))
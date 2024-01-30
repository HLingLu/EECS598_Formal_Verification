# repycudd demo1: basic BDD manipulation

import repycudd	# Python wrapper for CUDD
import sym_dot	# Utility to map variable numbers to their names (fragile: written by FA2020 EECS598 student)
import os

# Access to BDD operations must be through a so-called BDD manager.
# The following instruction creates a manager called mgr.
mgr = repycudd.DdManager()

a = mgr.IthVar(0)
b = mgr.IthVar(1)
c = mgr.IthVar(2)

var_names = ["a", "b", "c"]

# function
def AndAll(*args):
    symbols = [e for e in args]
    while len(symbols) > 1:
        symbols.append(mgr.And(symbols.pop(), symbols.pop()))
    return symbols.pop()

# f1 = (a+b)(as+bt)+cst
s = mgr.Not(mgr.And(a, c))  # (ac)'
t = mgr.Not(mgr.And(b, c))  # (bc)'
f1 = mgr.Or(mgr.And(mgr.Or(a, b),                           # (a+b)
                    mgr.Or(mgr.And(a, s), mgr.And(b, t))),  # (as+bt)
            mgr.And(mgr.And(c, s), t))                      # cst

# f2 = u(av+bw)+cvw
u = mgr.Not(mgr.And(a, b))    # (ab)'
v = mgr.Not(AndAll(a, c, u))  # (acu)'
w = mgr.Not(AndAll(b, c, u))  # (bcu)'
f2 = mgr.Or(mgr.And(u,                                      
                    mgr.Or(mgr.And(a, v), mgr.And(b, w))),  # u(av+bw)
            AndAll(c, v, w))                      # cvw

# f = a xor b xor c
f = mgr.Xor(mgr.Xor(a, b), c)

# determine which of these two functions is a correct implementation of f
f1_xor_f = mgr.Xor(f1, f)
f2_xor_f = mgr.Xor(f2, f)

farray = repycudd.DdArray(mgr,2)
farray.Push(mgr.BddToAdd(f1_xor_f))
farray.Push(mgr.BddToAdd(f2_xor_f))
fcn_names = ["f1_xor_f", "f2_xor_f"]

mgr.DumpDotArray(farray, "h2p1.dot")
sym_dot.sym_dot_manager("h2p1.dot", var_names, fcn_names).add_syms()
# os.system("dot -Tpng {0} -o {1}".format("h2p1.dot", "h2p1.png"))
os.system("dot -Tpdf {0} -o {1}".format("h2p1.dot", "h2p1.pdf"))
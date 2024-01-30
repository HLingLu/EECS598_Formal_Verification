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


farray = repycudd.DdArray(mgr,1)
farray.Push(mgr.BddToAdd(E))
fcn_names = ["E"]

mgr.DumpDotArray(farray, "h2p2b.dot")
sym_dot.sym_dot_manager("h2p2b.dot", var_names, fcn_names).add_syms()
# os.system("dot -Tpng {0} -o {1}".format("h2p2b.dot", "h2p2b.png"))
os.system("dot -Tpdf {0} -o {1}".format("h2p2b.dot", "h2p2b.pdf"))
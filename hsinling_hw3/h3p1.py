
import repycudd  # Python wrapper for CUDD
import sym_dot  # Utility to map variable numbers to their names (fragile: written by FA2020 EECS598 student)
import os

# Access to BDD operations must be through a so-called BDD manager.
# The following instruction creates a manager called mgr.
mgr = repycudd.DdManager()


a = mgr.IthVar(0)
b = mgr.IthVar(1)
c = mgr.IthVar(2)
d = mgr.IthVar(3)
e = mgr.IthVar(4)

# Create array to map variable numbers to their names (needed for printing BDD)
var_names = ["a", "b", "c","d","e"]

# Curcuit 1
x1 = mgr.Nand(b,d)
x2 = mgr.Or(b,d)
x3 = mgr.Nand(a,x2)
x4 = mgr.And(c,e)
x5 = mgr.Nor(c,e)
x6 = mgr.Nand(x1,x3)
x7 = mgr.Nor(x4,x6)
x8 = mgr.Nor(x5,x7)

# Curcuit
y1 = mgr.And(c,e)
y2 = mgr.Or(c,e)
y3 = mgr.And(b,y2)
y4 = mgr.And(d,y2)
y5 = mgr.Or(y1,y3)
y6 = mgr.Or(y1,y4)
y7 = mgr.And(y5,y6)
y8 = mgr.Or(y5,y6)
y9 = mgr.And(a,y8)
y10 = mgr.Nor(y7,y9)

# Equivalence

not_equal = mgr.Xor(x8, y10)

farray = repycudd.DdArray(mgr,3)
farray.Push(mgr.BddToAdd(x8))
farray.Push(mgr.BddToAdd(y10))
farray.Push(mgr.BddToAdd(not_equal))
fcn_names = ["circuit_1","circuit_2","not_equal"]

"""
Generate BDD
* DumpDotArray creates a dot file that labels variables and functions with numbers.
* sym_dot.sym_dot_manager reads the dot file and replaces variable and
  function numbers with the specified names
"""
mgr.DumpDotArray(farray, "h3p1.dot")
sym_dot.sym_dot_manager("h3p1.dot", var_names, fcn_names).add_syms()
os.system("dot -Tpdf {0} -o {1}".format("h3p1.dot", "h3p1.pdf"))

# repycudd demo1: basic BDD manipulation

import repycudd	# Python wrapper for CUDD
import sym_dot	# Utility to map variable numbers to their names (fragile: written by FA2020 EECS598 student)
import os

# Access to BDD operations must be through a so-called BDD manager.
# The following instruction creates a manager called mgr.
mgr = repycudd.DdManager()

"""
(a)  f(x0,x1,x2) = x0 ~x1 x2
"""

x0 = mgr.IthVar(0)
x1 = mgr.IthVar(1)
x2 = mgr.IthVar(2)

# Create array to map variable numbers to their names (needed for printing BDD)
var_names = ["x0", "x1", "x2"]

f = mgr.And(mgr.And(x0, mgr.Not(x1)), x2)

farray = repycudd.DdArray(mgr,1)
farray.Push(mgr.BddToAdd(f))
fcn_names = ["f"]

mgr.DumpDotArray(farray, "h1p1a.dot")
sym_dot.sym_dot_manager("h1p1a.dot", var_names, fcn_names).add_syms()
os.system("dot -Tpdf {0} -o {1}".format("h1p1a.dot", "h1p1a.pdf"))

"""
(b) 3-input majority function
    f(x0,x1,x2) = x0 x1 + x1 x2 + x0 x2
"""
f = mgr.Or(mgr.Or(mgr.And(x0, x1), mgr.And(x1, x2)), mgr.And(x0, x2))
farray = repycudd.DdArray(mgr,1)
farray.Push(mgr.BddToAdd(f))
fcn_names = ["f"]

mgr.DumpDotArray(farray, "h1p1b.dot")
sym_dot.sym_dot_manager("h1p1b.dot", var_names, fcn_names).add_syms()
os.system("dot -Tpdf {0} -o {1}".format("h1p1b.dot", "h1p1b.pdf"))

"""
(c) function that is 1 if exactly 2 of the variables are 1
"""
x3 = mgr.IthVar(3)

# Create array to map variable numbers to their names (needed for printing BDD)
var_names = ["x0", "x1", "x2", "x3"]
f1 = mgr.And(mgr.And(x0, x1), mgr.And(mgr.Not(x2), mgr.Not(x3)))
f2 = mgr.And(mgr.And(mgr.Not(x0), x1), mgr.And(x2, mgr.Not(x3)))
f3 = mgr.And(mgr.And(mgr.Not(x0), mgr.Not(x1)), mgr.And(x2, x3))
f4 = mgr.And(mgr.And(x0, mgr.Not(x1)), mgr.And(mgr.Not(x2), x3))
f5 = mgr.And(mgr.And(mgr.Not(x0), x1), mgr.And(mgr.Not(x2), x3))
f6 = mgr.And(mgr.And(x0, mgr.Not(x1)), mgr.And(x2, mgr.Not(x3)))
f = mgr.Or(mgr.Or(mgr.Or(f1, f2), mgr.Or(f3, f4)), mgr.Or(f5, f6))


farray = repycudd.DdArray(mgr,1)
farray.Push(mgr.BddToAdd(f))
fcn_names = ["f"]

mgr.DumpDotArray(farray, "h1p1c.dot")
sym_dot.sym_dot_manager("h1p1c.dot", var_names, fcn_names).add_syms()
os.system("dot -Tpdf {0} -o {1}".format("h1p1c.dot", "h1p1c.pdf"))

"""
(d) x0 xor x1 xor x2 xor x3
"""
f = mgr.Xor(mgr.Xor(x0, x1), mgr.Xor(x2, x3))

farray = repycudd.DdArray(mgr,1)
farray.Push(mgr.BddToAdd(f))
fcn_names = ["f"]

mgr.DumpDotArray(farray, "h1p1d.dot")
sym_dot.sym_dot_manager("h1p1d.dot", var_names, fcn_names).add_syms()
os.system("dot -Tpdf {0} -o {1}".format("h1p1d.dot", "h1p1d.pdf"))

"""
(e) Reorder variable x0 xor x1 xor x2 xor x3
"""
x0 = mgr.IthVar(3)
x1 = mgr.IthVar(2)
x2 = mgr.IthVar(1)
x3 = mgr.IthVar(0)

var_names = ["x3", "x2", "x1", "x0"]

f = mgr.Xor(mgr.Xor(x0, x1), mgr.Xor(x2, x3))

farray = repycudd.DdArray(mgr,1)
farray.Push(mgr.BddToAdd(f))
fcn_names = ["f"]

mgr.DumpDotArray(farray, "h1p1e.dot")
sym_dot.sym_dot_manager("h1p1e.dot", var_names, fcn_names).add_syms()
os.system("dot -Tpdf {0} -o {1}".format("h1p1e.dot", "h1p1e.pdf"))

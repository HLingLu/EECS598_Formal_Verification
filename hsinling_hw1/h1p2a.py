# repycudd demo1: basic BDD manipulation

import repycudd	# Python wrapper for CUDD
import sym_dot	# Utility to map variable numbers to their names (fragile: written by FA2020 EECS598 student)
import os

# Access to BDD operations must be through a so-called BDD manager.
# The following instruction creates a manager called mgr.
mgr = repycudd.DdManager()

"""
Create variables
Variables should be numbered sequentially starting from 0
Variable names can be arbitrary strings that start with a letter.
"""
x1 = mgr.IthVar(0)
x2 = mgr.IthVar(1)
x3 = mgr.IthVar(2)
x4 = mgr.IthVar(3)
x5 = mgr.IthVar(4)
x6 = mgr.IthVar(5)
x7 = mgr.IthVar(6)
x8 = mgr.IthVar(7)

# Create array to map variable numbers to their names (needed for printing BDD)
var_names = ["x1", "x2", "x3", "x4", "x5", "x6", "x7", "x8"]

"""
f =x1x2 +x3x4 +x5x6 +x7x8
"""

f = mgr.Or(mgr.Or(mgr.And(x1, x2), mgr.And(x3, x4)), mgr.Or(mgr.And(x5, x6), mgr.And(x7, x8)))

farray = repycudd.DdArray(mgr,1)
farray.Push(mgr.BddToAdd(f))
fcn_names = ["f"]

mgr.DumpDotArray(farray, "h1p2a.dot")
sym_dot.sym_dot_manager("h1p2a.dot", var_names, fcn_names).add_syms()
os.system("dot -Tpdf {0} -o {1}".format("h1p2a.dot", "h1p2a.pdf"))
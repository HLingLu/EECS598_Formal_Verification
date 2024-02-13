# repycudd demo1: basic BDD manipulation

import repycudd	# Python wrapper for CUDD
import sym_dot	# Utility to map variable numbers to their names (fragile: written by FA2020 EECS598 student)
import os

# Access to BDD operations must be through a so-called BDD manager.
# The following instruction creates a manager called mgr.
mgr = repycudd.DdManager()

x = mgr.IthVar(0)       # Input
y1 = mgr.IthVar(1)      # Present- and next-state variables of circuit 1
y2 = mgr.IthVar(2)
y1_next = mgr.IthVar(3)
y2_next = mgr.IthVar(4)
z1 = mgr.IthVar(5)      # Output variable of circuit 1
z2 = mgr.IthVar(6)

y3 = mgr.IthVar(7)      # Present- and next-state variables of circuit 2
y4 = mgr.IthVar(8)
y3_next = mgr.IthVar(9)
y4_next = mgr.IthVar(10)
z3 = mgr.IthVar(11)     # Output variable of circuit 2
z4 = mgr.IthVar(12)

y5 = mgr.IthVar(13)     # Present- and next-state variables of circuit 1
y6 = mgr.IthVar(14)
y5_next = mgr.IthVar(15)
y6_next = mgr.IthVar(16)
z5 = mgr.IthVar(17)     # Output variable of circuit 1
z6 = mgr.IthVar(18)

var_names = ["x", "y1", "y2", "y1_next", "y2_next", "z1", "z2",
             "y3", "y4", "y3_next", "y4_next", "z3", "z4",
             "y5", "y6", "y5_next", "y6_next", "z5", "z6"]

# # "Internal" (gate) variables of circuit 1
s1 = mgr.NewVar()
t1 = mgr.NewVar()
u1 = mgr.NewVar()
v1 = mgr.NewVar()
# "Internal" (gate) variables of circuit 2
s2 = mgr.NewVar()
t2 = mgr.NewVar()
u2 = mgr.NewVar()
v2 = mgr.NewVar()
# "Internal" (gate) variables of circuit 3
s3 = mgr.NewVar()
t3 = mgr.NewVar()
u3 = mgr.NewVar()

"""
Compare circuit 1 and circuit 2
"""

# Transition relation (consistency Function of the combined circuit)
T = mgr.One()
# Circuit 1
T = mgr.And(T, mgr.Xnor(s1, mgr.Or(y1, y2)))
T = mgr.And(T, mgr.Xnor(t1, mgr.Not(s1)))
T = mgr.And(T, mgr.Xnor(u1, mgr.And(x, s1)))
T = mgr.And(T, mgr.Xnor(v1, mgr.And(x, t1)))
T = mgr.And(T, mgr.Xnor(z1, y1))
T = mgr.And(T, mgr.Xnor(z2, y2))
# Circuit 2
T = mgr.And(T, mgr.Xnor(s2, mgr.Or(u2, v2)))
T = mgr.And(T, mgr.Xnor(t2, mgr.Not(y4)))
T = mgr.And(T, mgr.Xnor(u2, mgr.And(y3, y4)))
T = mgr.And(T, mgr.Xnor(v2, mgr.And(y3, t2)))
T = mgr.And(T, mgr.Xnor(z3, u2))
T = mgr.And(T, mgr.Xnor(z4, v2))

# Connect next-state variables
# Circuit 1
T = mgr.And(T, mgr.Xnor(y1_next, u1))
T = mgr.And(T, mgr.Xnor(y2_next, v1))
# Circuit 2
T = mgr.And(T, mgr.Xnor(y3_next, x))
T = mgr.And(T, mgr.Xnor(y4_next, s2))

# Create sets of variables for existential elimination
# All vars except state variables
Non_State_Vars = mgr.One()
Non_State_Vars = mgr.And(Non_State_Vars, x)
Non_State_Vars = mgr.And(Non_State_Vars, s1)
Non_State_Vars = mgr.And(Non_State_Vars, t1)
Non_State_Vars = mgr.And(Non_State_Vars, u1)
Non_State_Vars = mgr.And(Non_State_Vars, v1)
Non_State_Vars = mgr.And(Non_State_Vars, z1)
Non_State_Vars = mgr.And(Non_State_Vars, z2)

Non_State_Vars = mgr.And(Non_State_Vars, s2)
Non_State_Vars = mgr.And(Non_State_Vars, t2)
Non_State_Vars = mgr.And(Non_State_Vars, u2)
Non_State_Vars = mgr.And(Non_State_Vars, v2)
Non_State_Vars = mgr.And(Non_State_Vars, z3)
Non_State_Vars = mgr.And(Non_State_Vars, z4)


# All vars except next-state
All_But_Next_State_Vars = Non_State_Vars
All_But_Next_State_Vars = mgr.And(All_But_Next_State_Vars, y1)
All_But_Next_State_Vars = mgr.And(All_But_Next_State_Vars, y2)
All_But_Next_State_Vars = mgr.And(All_But_Next_State_Vars, y3)
All_But_Next_State_Vars = mgr.And(All_But_Next_State_Vars, y4)


# All vars except present-state
All_But_Present_State_Vars = Non_State_Vars
All_But_Present_State_Vars = mgr.And(All_But_Present_State_Vars, y1_next)
All_But_Present_State_Vars = mgr.And(All_But_Present_State_Vars, y2_next)
All_But_Present_State_Vars = mgr.And(All_But_Present_State_Vars, y3_next)
All_But_Present_State_Vars = mgr.And(All_But_Present_State_Vars, y4_next)


Present_State_DDarray = repycudd.DdArray(mgr,4)
Next_State_DDarray = repycudd.DdArray(mgr, 4)
Present_State_DDarray.Push(y1)
Present_State_DDarray.Push(y2)
Present_State_DDarray.Push(y3)
Present_State_DDarray.Push(y4)
Next_State_DDarray.Push(y1_next)
Next_State_DDarray.Push(y2_next)
Next_State_DDarray.Push(y3_next)
Next_State_DDarray.Push(y4_next)

# R: Reachable states from I = ~y1 & ~y2 & ~y3 & ~y4
R = mgr.One()
R = mgr.And(R, mgr.Not(y1))
R = mgr.And(R, mgr.Not(y2))
R = mgr.And(R, mgr.Not(y3))
R = mgr.And(R, mgr.Not(y4))

# Forward image iteration
N = R
while(N != mgr.Zero()):
	C = N
	Img = mgr.AndAbstract(C, T, All_But_Next_State_Vars)
	Img = mgr.SwapVariables(Img, Present_State_DDarray, Next_State_DDarray, 4)
	N = mgr.And(Img, mgr.Not(R))
	R = mgr.Or(R, Img)

P = mgr.And(T, mgr.Xnor(mgr.Xnor(z1, z2), mgr.Xnor(z3, z4)))

P = mgr.ExistAbstract(P, All_But_Present_State_Vars)
c1_not_equiv_c2 = mgr.And(R, mgr.Not(P))	# R & ~P must be unsatisfiable


"""
Compare circuit 1 and circuit 3
"""

# Transition relation (consistency Function of the combined circuit)
T = mgr.One()
# Circuit 1
T = mgr.And(T, mgr.Xnor(s1, mgr.Or(y1, y2)))
T = mgr.And(T, mgr.Xnor(t1, mgr.Not(s1)))
T = mgr.And(T, mgr.Xnor(u1, mgr.And(x, s1)))
T = mgr.And(T, mgr.Xnor(v1, mgr.And(x, t1)))
T = mgr.And(T, mgr.Xnor(z1, y1))
T = mgr.And(T, mgr.Xnor(z2, y2))
# Circuit 3
T = mgr.And(T, mgr.Xnor(s3, mgr.Or(y5, y6)))
T = mgr.And(T, mgr.Xnor(u3, mgr.And(x, s3)))
T = mgr.And(T, mgr.Xnor(t3, mgr.Not(t3)))
T = mgr.And(T, mgr.Xnor(z5, mgr.And(x, y5)))
T = mgr.And(T, mgr.Xnor(z6, mgr.And(x, y6)))

# Connect next-state variables
# Circuit 1
T = mgr.And(T, mgr.Xnor(y1_next, u1))
T = mgr.And(T, mgr.Xnor(y2_next, v1))
# Circuit 3
T = mgr.And(T, mgr.Xnor(y5_next, t3))
T = mgr.And(T, mgr.Xnor(y6_next, u3))

# Create sets of variables for existential elimination
# All vars except state variables
Non_State_Vars = mgr.One()
Non_State_Vars = mgr.And(Non_State_Vars, x)
Non_State_Vars = mgr.And(Non_State_Vars, s1)
Non_State_Vars = mgr.And(Non_State_Vars, t1)
Non_State_Vars = mgr.And(Non_State_Vars, u1)
Non_State_Vars = mgr.And(Non_State_Vars, v1)
Non_State_Vars = mgr.And(Non_State_Vars, z1)
Non_State_Vars = mgr.And(Non_State_Vars, z2)

Non_State_Vars = mgr.And(Non_State_Vars, s3)
Non_State_Vars = mgr.And(Non_State_Vars, y3)
Non_State_Vars = mgr.And(Non_State_Vars, u3)
Non_State_Vars = mgr.And(Non_State_Vars, z5)
Non_State_Vars = mgr.And(Non_State_Vars, z6)


# All vars except next-state
All_But_Next_State_Vars = Non_State_Vars
All_But_Next_State_Vars = mgr.And(All_But_Next_State_Vars, y1)
All_But_Next_State_Vars = mgr.And(All_But_Next_State_Vars, y2)
All_But_Next_State_Vars = mgr.And(All_But_Next_State_Vars, y5)
All_But_Next_State_Vars = mgr.And(All_But_Next_State_Vars, y6)


# All vars except present-state
All_But_Present_State_Vars = Non_State_Vars
All_But_Present_State_Vars = mgr.And(All_But_Present_State_Vars, y1_next)
All_But_Present_State_Vars = mgr.And(All_But_Present_State_Vars, y2_next)
All_But_Present_State_Vars = mgr.And(All_But_Present_State_Vars, y5_next)
All_But_Present_State_Vars = mgr.And(All_But_Present_State_Vars, y6_next)


Present_State_DDarray = repycudd.DdArray(mgr,4)
Next_State_DDarray = repycudd.DdArray(mgr, 4)
Present_State_DDarray.Push(y1)
Present_State_DDarray.Push(y2)
Present_State_DDarray.Push(y5)
Present_State_DDarray.Push(y6)
Next_State_DDarray.Push(y1_next)
Next_State_DDarray.Push(y2_next)
Next_State_DDarray.Push(y5_next)
Next_State_DDarray.Push(y6_next)

# R: Reachable states from I = ~y1 & ~y2 & ~y5 & y6
R = mgr.One()
R = mgr.And(R, mgr.Not(y1))
R = mgr.And(R, mgr.Not(y2))
R = mgr.And(R, mgr.Not(y5))
R = mgr.And(R, y6)

# Forward image iteration
N = R
while(N != mgr.Zero()):
	C = N
	Img = mgr.AndAbstract(C, T, All_But_Next_State_Vars)
	Img = mgr.SwapVariables(Img, Present_State_DDarray, Next_State_DDarray, 4)
	N = mgr.And(Img, mgr.Not(R))
	R = mgr.Or(R, Img)

P = mgr.And(T, mgr.Xnor(mgr.Xnor(z1, z2), mgr.Xnor(z5, z6)))

P = mgr.ExistAbstract(P, All_But_Present_State_Vars)
c1_not_equiv_c3 = mgr.And(R, mgr.Not(P))	# R & ~P must be unsatisfiable

"""
Compare circuit 2 and circuit 3
"""

# Transition relation (consistency Function of the combined circuit)
T = mgr.One()
# Circuit 2
T = mgr.And(T, mgr.Xnor(s2, mgr.Or(u2, v2)))
T = mgr.And(T, mgr.Xnor(t2, mgr.Not(y4)))
T = mgr.And(T, mgr.Xnor(u2, mgr.And(y3, y4)))
T = mgr.And(T, mgr.Xnor(v2, mgr.And(y3, t2)))
T = mgr.And(T, mgr.Xnor(z3, u2))
T = mgr.And(T, mgr.Xnor(z4, v2))
# Circuit 3
T = mgr.And(T, mgr.Xnor(s3, mgr.Or(y5, y6)))
T = mgr.And(T, mgr.Xnor(u3, mgr.And(x, s3)))
T = mgr.And(T, mgr.Xnor(t3, mgr.Not(t3)))
T = mgr.And(T, mgr.Xnor(z5, mgr.And(x, y5)))
T = mgr.And(T, mgr.Xnor(z6, mgr.And(x, y6)))

# Connect next-state variables
# Circuit 2
T = mgr.And(T, mgr.Xnor(y1_next, u1))
T = mgr.And(T, mgr.Xnor(y2_next, v1))
# Circuit 3
T = mgr.And(T, mgr.Xnor(y3_next, x))
T = mgr.And(T, mgr.Xnor(y4_next, s2))


# Create sets of variables for existential elimination
# All vars except state variables
Non_State_Vars = mgr.One()
Non_State_Vars = mgr.And(Non_State_Vars, x)
Non_State_Vars = mgr.And(Non_State_Vars, s2)
Non_State_Vars = mgr.And(Non_State_Vars, t2)
Non_State_Vars = mgr.And(Non_State_Vars, u2)
Non_State_Vars = mgr.And(Non_State_Vars, v2)
Non_State_Vars = mgr.And(Non_State_Vars, z3)
Non_State_Vars = mgr.And(Non_State_Vars, z4)

Non_State_Vars = mgr.And(Non_State_Vars, s3)
Non_State_Vars = mgr.And(Non_State_Vars, y3)
Non_State_Vars = mgr.And(Non_State_Vars, u3)
Non_State_Vars = mgr.And(Non_State_Vars, z5)
Non_State_Vars = mgr.And(Non_State_Vars, z6)


# All vars except next-state
All_But_Next_State_Vars = Non_State_Vars
All_But_Next_State_Vars = mgr.And(All_But_Next_State_Vars, y3)
All_But_Next_State_Vars = mgr.And(All_But_Next_State_Vars, y4)
All_But_Next_State_Vars = mgr.And(All_But_Next_State_Vars, y5)
All_But_Next_State_Vars = mgr.And(All_But_Next_State_Vars, y6)


# All vars except present-state
All_But_Present_State_Vars = Non_State_Vars
All_But_Present_State_Vars = mgr.And(All_But_Present_State_Vars, y3_next)
All_But_Present_State_Vars = mgr.And(All_But_Present_State_Vars, y4_next)
All_But_Present_State_Vars = mgr.And(All_But_Present_State_Vars, y5_next)
All_But_Present_State_Vars = mgr.And(All_But_Present_State_Vars, y6_next)


Present_State_DDarray = repycudd.DdArray(mgr,4)
Next_State_DDarray = repycudd.DdArray(mgr, 4)
Present_State_DDarray.Push(y3)
Present_State_DDarray.Push(y4)
Present_State_DDarray.Push(y5)
Present_State_DDarray.Push(y6)
Next_State_DDarray.Push(y3_next)
Next_State_DDarray.Push(y4_next)
Next_State_DDarray.Push(y5_next)
Next_State_DDarray.Push(y6_next)

# R: Reachable states from I = ~y3 & ~y4 & ~y5 & y6
R = mgr.One()
R = mgr.And(R, mgr.Not(y3))
R = mgr.And(R, mgr.Not(y4))
R = mgr.And(R, mgr.Not(y5))
R = mgr.And(R, y6)

# Forward image iteration
N = R
while(N != mgr.Zero()):
	C = N
	Img = mgr.AndAbstract(C, T, All_But_Next_State_Vars)
	Img = mgr.SwapVariables(Img, Present_State_DDarray, Next_State_DDarray, 4)
	N = mgr.And(Img, mgr.Not(R))
	R = mgr.Or(R, Img)

P = mgr.And(T, mgr.Xnor(mgr.Xnor(z3, z4), mgr.Xnor(z5, z6)))

P = mgr.ExistAbstract(P, All_But_Present_State_Vars)
c2_not_equiv_c3 = mgr.And(R, mgr.Not(P))	# R & ~P must be unsatisfiable


farray = repycudd.DdArray(mgr,3)
farray.Push(mgr.BddToAdd(mgr.BddToAdd(c1_not_equiv_c2)))
farray.Push(mgr.BddToAdd(mgr.BddToAdd(c1_not_equiv_c3)))
farray.Push(mgr.BddToAdd(mgr.BddToAdd(c2_not_equiv_c3)))
fcn_names = ["c1_not_equiv_c2", "c1_not_equiv_c3", "c2_not_equiv_c3"]

mgr.DumpDotArray(farray, "h3p2.dot")
sym_dot.sym_dot_manager("h3p2.dot", var_names, fcn_names).add_syms()
os.system("dot -Tpdf {0} -o {1}".format("h3p2.dot", "h3p2.pdf"))
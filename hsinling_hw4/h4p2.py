import warnings # eliminate an annoying warning message about bidict.
warnings.filterwarnings("ignore", message="Python 2 support will be dropped in a future release.")


from pysat.formula import CNF			    # Load the CNF module
from pysat.solvers import Solver			# Load the Solver module
from threading import Timer				# To set time-outs

f = CNF(from_file = 'h4p2f.cnf')			# Read CNF file
not_f = f.negate()
g = CNF(from_file = 'h4p2g.cnf')			# Read CNF file
not_g = g.negate()

# f xor g = f'g + fg' 
# same: 0, diff: 1
nf_g = CNF()
nf_g.extend(not_f)
nf_g.extend(g)

f_ng = CNF()
f_ng.extend(f)
f_ng.extend(not_g)

print("------- Solve f xor g -------")
print("f ^ g = f'g + fg'\n")

# Solver
# f'g
print("Solve f'g")
print(' Solver: Minisat22 solver')
s = Solver(name='m22', use_timer=True)			# Create Minisat22 solver
s.append_formula(nf_g.clauses)
print(' #Vars: {0:d}'.format(s.nof_vars()))		# Number of variables
print(' #Clauses: {0:d}'.format(s.nof_clauses()))	# Number of clauses

nf_g_solve = s.solve()
if nf_g_solve:
    print(" f'g is satisfiable")
else:
    print(" f'g is unsatisfiable")
print(' Stats: {0:s}'.format(s.accum_stats()))		# Statistics
print(' Time: {}s\n'.format(s.time()))		# Runtime
s.delete()

# fg'
print("Solve fg'")
print(' Solver: Minisat22 solver')
s = Solver(name='m22', use_timer=True)			# Create Minisat22 solver
s.append_formula(f_ng.clauses)
print(' #Vars: {0:d}'.format(s.nof_vars()))		# Number of variables
print(' #Clauses: {0:d}'.format(s.nof_clauses()))	# Number of clauses

f_ng_solve = s.solve()
if f_ng_solve:
    print(" fg' is satisfiable")
else:
    print(" fg' is unsatisfiable")
print(' Stats: {0:s}'.format(s.accum_stats()))		# Statistics
print(' Time: {}s\n'.format(s.time()))		# Runtime
s.delete()

if ~f_ng_solve and ~nf_g_solve:
    print("f and g are equivalent")
else:
    print("f and g are not equivalent")



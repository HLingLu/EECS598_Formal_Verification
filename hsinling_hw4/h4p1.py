# pysat demo4: combinational equivalence checking


from pysat.formula import CNF				# Load the CNF module
from pysat.solvers import Solver			# Load the Solver module
from threading import Timer				# To set time-outs

s = Solver(name='m22', use_timer=True)			# Create Minisat22 solver
print(' Solver: Minisat22 solver')
def interrupt(s):					# Define interrupt
	s.interrupt()
timer = Timer(120, interrupt, [s])			# Set 2-minute time-out


f = CNF(from_file = 'h4p1.cnf')			# Read CNF file
s.append_formula(f.clauses)				# Load f into the solver
print(' #Vars: {0:d}'.format(s.nof_vars()))		# Number of variables
print(' #Clauses: {0:d}'.format(s.nof_clauses()))	# Number of clauses
timer.start()						# Start the timer
if s.solve():						# Solve
	print(' The formula is satisfiable. These two adder designs are not equivalent.')
else:
	print(' The formula is unsatisfiable. These two adder designs are equivalent.')
timer.cancel()						# Stop the timer		
print(' Model: {0:s}'.format(s.get_model()))		# Satisfying assignment
print(' Stats: {0:s}'.format(s.accum_stats()))		# Statistics
print(' Time: {}s\n'.format(s.time()))		# Runtime
s.delete()						# Clean up

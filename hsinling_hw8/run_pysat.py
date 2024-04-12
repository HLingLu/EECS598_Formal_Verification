

from pysat.formula import CNF				# Load the CNF module
from pysat.solvers import Solver			# Load the Solver module



for i in range(10):
	s = Solver(name='cd', use_timer=True)				# Create CaDiCal solver
	print(' Solver: CaDiCal solver')
	def interrupt(s):									# Define interrupt
		s.interrupt()

	# Run original cnf files
	# fileName = "cnf_files/fdmus_b14_" + str(132+i) + ".cnf"
	# Run symmetry cnf files
	fileName = "shatter_cnf/fdmus_b14_" + str(132+i) + ".cnf"
	f = CNF(from_file = fileName)						# Read CNF file

	s.append_formula(f.clauses)							# Load f into the solver
	print('------------ ' + fileName + ' ------------')
	print(' #Vars: {0:d}'.format(s.nof_vars()))			# Number of variables
	print(' #Clauses: {0:d}'.format(s.nof_clauses()))	# Number of clauses

	if s.solve():										# Solve
		print(' The formula is satisfiable.')
	else:
		print(' The formula is unsatisfiable.')

	print(' Model: {0:s}'.format(s.get_model()))		# Satisfying assignment
	print(' Stats: {0:s}'.format(s.accum_stats()))		# Statistics
	print(' Time: {}s\n'.format(s.time()))				# Runtime
	print('')
	s.delete()											# Clean up

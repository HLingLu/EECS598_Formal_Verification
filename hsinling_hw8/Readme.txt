// Folder
cnf_files             -> Provided original cnf files
shatter_cnf           -> Shatter output cnf files
shatter_result        -> Shatter output messages
saucy_result          -> Symmetry output messages with files in shatter_cnf
saucy_output          -> Symmetry output by saucy with files in cnf_files
saucy_sym_output      -> Symmetry output by saucy with files in shatter_cnf
Figures               -> Figures from hw8_plot.m

// Log files
saucy_output.log      -> Integrate files in saucy_result
saucy_sym_output.log  -> Integrate files in saucy_sym_output
shatter_output.log    -> Integrate files in shatter_result

// text files
pysat_result.txt      -> PySAT result with files in cnf_files
pysat_sym_result.txt  -> PySAT result with files in shatter_cnf

// Python
run_pysat.py          -> Run PySAT with python, needs to modify inside to choosewhich cnf files to run

// Script 
### When running script, must check inside to see if you're running with correct files.
run_saucy.sh          -> Run saucy automatically and write into files
run_shatter.sh        -> Run shatter automatically and write into files
hw8.sh		      -> Run saucy, shatter, and pysat automatically and write into files

// Other
hsinling_hw8.pdf      -> Report
hw8_plot.m            -> Plot figures
hw8.xlsx              -> Excel file with statistics table


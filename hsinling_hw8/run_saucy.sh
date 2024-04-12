# save result to separate files
# run script by ./run_saucy.sh

# save result to a log file, have to remove "2>......"
# run script by ./run_saucy.sh 2>&1 | tee saucy_output.log

# $file -> path and name.cnf
# fileName=$(basename "$file") -> name.cnf
# "${fileName%.*}" -> name

# saucy --cnf -s shatter_cnf/b14_132.cnf > saucy_result/b14_132.txt

for file in shatter_cnf/*; do
    echo "Running $file"
    fileName=$(basename "$file")
    saucy --cnf -s $file > saucy_output/${fileName%.*}.txt 2> saucy_result/${fileName%.*}.txt
    echo ""
done
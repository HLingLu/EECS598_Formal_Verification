# save result to separate files
# run script by ./run_shatter.sh

# save result to a log file, have to remove "2>......"
# run script by ./run_shatter.sh 2>&1 | tee shatter_output.log

# $file -> path and name.cnf
# fileName=$(basename "$file") -> name.cnf
# "${fileName%.*}" -> name
# shatter -s cnf_files/fdmus_b14_132.cnf > shatter_cnf/b14_132.cnf

for file in cnf_files/*; do
    echo "Running $file"
    fileName=$(basename "$file")
    shatter -s $file > shatter_cnf/$(basename $file) 2> shatter_result/shatter_${fileName%.*}.txt
    echo ""
done
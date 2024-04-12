for file in cnf_files/*; do
    echo "Running $file"
    fileName=$(basename "$file")
    shatter -s $file > shatter_cnf/$(basename $file) 2> shatter_result/shatter_${fileName%.*}.txt
    echo ""
done

for file in shatter_cnf/*; do
    echo "Running $file"
    fileName=$(basename "$file")
    saucy --cnf -s $file > saucy_output/${fileName%.*}.txt 2> saucy_result/${fileName%.*}.txt
    echo ""
done

python run_pysat.py > pysat_result.txt
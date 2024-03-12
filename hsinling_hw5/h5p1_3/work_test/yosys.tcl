yosys read_verilog -noopt -nolatches -I . -sv h5p1_3/work_test/SeqEqvMiter.v;
yosys hierarchy -auto-top;
yosys hierarchy -libdir h5p1_3/work_test;
yosys hierarchy -check;
yosys rename -top main;
yosys delete -output main;
yosys expose main/prop_neg;
yosys proc;
yosys clean;
yosys splitnets -driver;
yosys clean;
yosys pmuxtree;
yosys clean;
yosys memory;
yosys clean;
yosys flatten;
yosys clean -purge;
yosys setundef -undriven -expose -undef;
yosys clean;
yosys check;
yosys write_ilang h5p1_3/work_test/test.ilang;
yosys write_verilog -attr2comment h5p1_3/work_test/test_y.v;
yosys write_btor h5p1_3/work_test/test.btor2;

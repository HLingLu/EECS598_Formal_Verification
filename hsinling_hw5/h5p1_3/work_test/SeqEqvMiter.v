module Miter(Clock, X, NotEqv);
	input Clock, X;
	output NotEqv;

	wire Z1, Z2;

// Instantiate the two Circuits
	Circuit1 Ckt1(Clock, X, Z1);
	Circuit2 Ckt2(Clock, X, Z2);

// Miter Logic
	assign NotEqv = Z1 ^ Z2;

// Equivalnce Check
	assert property (~NotEqv);
endmodule // Miter

module Circuit1(Clock, X, Z);
	input X, Clock;
	output Z;

  reg [2:0] Y;
  wire [2:0] Y_Next;

	initial Y = 0;

// Next-State logic
  assign Y_Next[2] = (~X & Y[2]) | (Y[2] & ~Y[1]) | (Y[2] & ~Y[0]) | (X & ~Y[2] & Y[1] & Y[0]);
  assign Y_Next[1] = (~X & Y[1]) | (Y[1] & ~Y[0]) | (X & ~Y[1] & Y[0]);
  assign Y_Next[0] = (~X & Y[0]) | (X & ~Y[0]);

// State Update
	always @(posedge Clock)
    Y <= Y_Next;

// Output Logic
	assign Z = (Y == 7);
endmodule // Circuit1

module Circuit2(Clock, X, Z);
	input X, Clock;
	output Z;

	reg [7:0] W;
	wire [7:0] W_Next;

	initial W = 'b10000000;

// Next-State logic
  assign W_Next[7] = ~W[6] & ~W[5] & ~W[4] & ~W[3] & ~W[2] & ~W[1] & (X | W[7]) & (~W[7] | ~W[0]) & (~X | W[0]);
  assign W_Next[6] = ~W[5] & ~W[4] & ~W[3] & ~W[2] & ~W[1] & ~W[0] & (~X | W[7]) & (~W[7] | ~W[6]) & (X | W[6]);
  assign W_Next[5] = ~W[7] & ~W[4] & ~W[3] & ~W[2] & ~W[1] & ~W[0] & (~X | W[6]) & (~W[6] | ~W[5]) & (X | W[5]);
  assign W_Next[4] = ~W[7] & ~W[6] & ~W[3] & ~W[2] & ~W[1] & ~W[0] & (~X | W[5]) & (~W[5] | ~W[4]) & (X | W[4]);
  assign W_Next[3] = ~W[7] & ~W[6] & ~W[5] & ~W[2] & ~W[1] & ~W[0] & (~X | W[4]) & (~W[4] | ~W[3]) & (X | W[3]);
  assign W_Next[2] = ~W[7] & ~W[6] & ~W[5] & ~W[4] & ~W[1] & ~W[0] & (~X | W[3]) & (~W[3] | ~W[2]) & (X | W[2]);
  assign W_Next[1] = ~W[7] & ~W[6] & ~W[5] & ~W[4] & ~W[3] & ~W[0] & (~X | W[2]) & (~W[2] | ~W[1]) & (X | W[1]);
  assign W_Next[0] = ~W[7] & ~W[6] & ~W[5] & ~W[4] & ~W[3] & ~W[2] & (~X | W[1]) & (~W[1] | ~W[0]) & (X | W[0]);

// State Update
	always @(posedge Clock)
    W <= W_Next;

// Output Logic
	// Q1
	// assign Z = W[0];
	// Q2
	assign Z = W[1];
endmodule // Circuit2


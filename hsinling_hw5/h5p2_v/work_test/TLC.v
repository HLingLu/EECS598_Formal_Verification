module TLC(Clock, Reset, E, NL, EL, W, ETL, NLTL, ELTL, WTL, RemainingTime);
	input Clock;
	input Reset;
	input E, NL, EL, W;			// Sensors
	output [6:0] ETL, NLTL, ELTL, WTL;	// Lights
	output [3:0] RemainingTime;
	
	reg [2:0] State;
	wire [2:0] Next_State;
	
	wire NC;				// No cars
	reg StartTimer;	// 10 second timer
	wire TO;				// Time-out

// State Assignments
	parameter EGWG	= 3'b000;
	parameter EGWY	= 3'b001;
	parameter EGNG	= 3'b010;
	parameter EGNY	= 3'b011;
	parameter EYWY	= 3'b100;
	parameter EYNY	= 3'b101;
	parameter ELG	= 3'b110;
	parameter ELY	= 3'b111;
	
// Traffic Light Color Assignments
	parameter Green		= 7'b0010000;		// Lower case g
	parameter Yellow	= 7'b0010001;		// Lower case y
	parameter Red		= 7'b0101111;	    // Lower case r
	
// Initial state
	initial State = EGWG;
	
	assign NC = ~E & ~W & ~NL & ~EL;  // No Cars
	
// State Transitions
	always @*
	begin
		case(State)
			EGWG:	if (TO & (NC | NL))
				      Next_State <= EGWY;
						else if (TO & EL & ~NC & ~NL)
								Next_State <= EYWY;
						else
								Next_State <= EGWG;

			EGWY:	Next_State <= EGNG;
							
			EGNG:	if (TO & (NC | EL))
								Next_State = EYNY;
						else if (TO & W & ~NC & ~EL)
								Next_State = EGNY;
						else
								Next_State <= EGNG;

      EGNY: Next_Stata <= EGWG;
								
			EYWY:	Next_State <= ELG;
			
			EYNY:	Next_State <= ELG;
							
			ELG:	if (TO & (NC | E | W | NL))
								Next_State = ELY;
						else
								Next_State <= ELG;
								
			ELY:	if (E | W | ~NL)
								Next_State <= EGWG;
							else
								Next_State <= EGNG;
		endcase
	end
	
// State Update
	always @(posedge Clock)
		if (Reset)
			State <= EGWG;
		else
			State <= Next_State;

// Output logic
	always @*
	begin
		case(State)
			EGWG:
			begin
				ETL		<= Green;
				NLTL	<= Red;
				ELTL	<= Red;
				WTL		<= Green;
				StartTimer <= 1'b0;
			end
			
			EGWY:
			begin
				ETL		<= Green;
				NLTL	<= Red;
				ELTL	<= Red;
				WTL		<= Yellow;
				StartTimer <= 1'b1;
			end
			
			EGNG:
			begin
				ETL		<= Green;
				NLTL	<= Green;
				ELTL	<= Red;
				WTL		<= Red;
				StartTimer <= 1'b0;
			end

			EGNY:
			begin
				ETL		<= Green;
				NLTL	<= Yellow;
				ELTL	<= Red;
				WTL		<= Red;
				StartTimer <= 1'b0;
			end

			EYWY:
			begin
				ETL		<= Yellow;
				NLTL	<= Red;
				ELTL	<= Red;
				WTL		<= Yellow;
				StartTimer <= 1'b1;
			end

			EYNY:
			begin
				ETL		<= Yellow;
				NLTL	<= Yellow;
				ELTL	<= Red;
				WTL		<= Red;
				StartTimer <= 1'b1;
			end

			ELG:
			begin
				ETL		<= Red;
				NLTL	<= Green; // error
				// NLTL	<= Red; 
				ELTL	<= Green;
				WTL		<= Red;
				StartTimer <= 1'b0;
			end
			
			ELY:
			begin
				ETL		<= Red;
				NLTL	<= Red;
				ELTL	<= Yellow;
				WTL		<= Red;
				StartTimer <= 1'b1;
			end
		endcase
	end
	
	Timer T(Clock, StartTimer, RemainingTime, TO);

// Safety
// Write expression to capture unsafe traffic signal combinations, and
// add assertion to check for safe operation
  wire collision; 
  assign collision = ((ELTL == Green) & (WTL == Green)) |
					 ((NLTL == Green) & (ELTL == Green)) |
					 ((NLTL == Green) & (WTL == Green));
  assert property (~collision);

endmodule // TLC

// Timer
module Timer(Clock, Start, Time, TimeOut);
	input Clock;
	input Start;
	output [3:0] Time;
	output TimeOut;

	reg [3:0] Q;
	wire [3:0] Q_Next;

	parameter ZERO	= 4'b0000;
	parameter ONE		= 4'b0001;
	parameter TWO		= 4'b0010;
	parameter THREE	= 4'b0011;
	parameter FOUR	= 4'b0100;
	parameter FIVE	= 4'b0101;
	parameter SIX		= 4'b0110;
	parameter SEVEN	= 4'b0111;
	parameter EIGHT	= 4'b1000;
	parameter NINE	= 4'b1001;
	parameter TEN		= 4'b1010;

	
// Initial state
	initial Q = TEN;
	
// State Transitions
	always @(Q[3], Q[2], Q[1], Q[0])
	begin
		case(Q)
			TEN:		Q_Next = NINE;
			NINE:		Q_Next = EIGHT;
			EIGHT:	Q_Next = SEVEN;
			SEVEN:	Q_Next = SIX;
			SIX:		Q_Next = FIVE;
			FIVE:		Q_Next = FOUR;
			FOUR:		Q_Next = THREE;
			THREE:	Q_Next = TWO;
			TWO:		Q_Next = ONE;
			ONE:		Q_Next = ZERO;
			ZERO:		Q_Next = ZERO;
		endcase
	end

// State Update
	always @(negedge Clock)
	begin
		if (Start)
			Q <= NINE;
		else
			Q <= Q_Next;
	end

// Output Logic
	assign Time = Q;
	assign TimeOut = (Q == ZERO);

endmodule // Timer


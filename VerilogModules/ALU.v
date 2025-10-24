module ALU(
    input [15:0] A,
    input [15:0] B,
    input [3:0] ALUControl,  // 0000=ADD, 0001=SUB, 0010=AND, 0011=OR
    output reg [15:0] Result,
    output reg Zero,
    output reg Carry
);

always @(*) begin
    Carry = 0;
    case(ALUControl)
        4'b0000: {Carry, Result} = A + B;
        4'b0001: {Carry, Result} = A - B;
        4'b0010: Result = A & B;
        4'b0011: Result = A | B;
        default: Result = 0;
    endcase
    Zero = (Result == 0);
end

endmodule

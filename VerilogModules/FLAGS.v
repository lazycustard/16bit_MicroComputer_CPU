module FLAGS(
    input Zero_in,
    input Carry_in,
    output reg Zero,
    output reg Carry
);

always @(*) begin
    Zero  = Zero_in;
    Carry = Carry_in;
end

endmodule

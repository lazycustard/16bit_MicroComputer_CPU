module RAM(
    input [15:0] addr,
    output reg [15:0] data
);
reg [15:0] mem [0:31];

initial begin
$readmemb("C:\\Users\\Amit Gupta\\Desktop\\16bit_micro\\Assembler\\binary.txt", mem);
    $display("RAM initialized from binary.txt");
    $display("mem[0] = %b", mem[0]);
    $display("mem[1] = %b", mem[1]);

end

always @(*) begin
    data = mem[addr];
end

endmodule

module IR(
    input clk,
    input reset,
    input [15:0] D,
    output reg [15:0] Q
);

always @(posedge clk or posedge reset) begin
    if(reset) Q <= 16'b0;
    else Q <= D;
end

endmodule

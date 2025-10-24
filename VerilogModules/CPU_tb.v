`timescale 1ns/1ps
module CPU_tb();

reg clk;
reg reset;
reg [15:0] in_data;

// wires for exposed signals
wire [15:0] in_reg_out;
wire [15:0] out_led;
wire [15:0] ALU_out;
wire [15:0] REG_A_out;
wire [15:0] REG_B_out;
wire [15:0] PC_out;
wire [15:0] IR_out;
wire Zero;
wire Carry;

// Read numbers from external file
reg [15:0] user_num1, user_num2;
integer file;

// instantiate IO_REG (input)
IO_REG in_reg(
    .clk(clk),
    .D(in_data),
    .Q(in_reg_out)
);

// instantiate CPU
CPU cpu(
    .clk(clk),
    .reset(reset),
    .IN_REG_out(in_reg_out),
    .out_led(out_led),
    .ALU_out(ALU_out),
    .REG_A_out(REG_A_out),
    .REG_B_out(REG_B_out),
    .PC_out(PC_out),
    .IR_out(IR_out),
    .Zero(Zero),
    .Carry(Carry)
);

// clock generation
initial clk = 0;
always #5 clk = ~clk;

// Read user numbers from file
initial begin
    file = $fopen("user_inputs.txt", "r");
    if (file) begin
        $fscanf(file, "%d %d", user_num1, user_num2);
        $fclose(file);
        $display("================================================");
        $display("USER CALCULATOR: %d and %d", user_num1, user_num2);
        $display("================================================");
    end else begin
        $display("Using default numbers: 20 and 6");
        user_num1 = 20;
        user_num2 = 6;
    end
end

// Test sequence with user numbers
initial begin
    reset = 1;
    in_data = 16'd0;
    
    #15 reset = 0;
    
    // ADDITION
    #40 in_data = user_num1;
    #40 in_data = user_num2;
    #40 in_data = 16'b0011000000000000; // ADD
    #40 in_data = 16'b0100000000000000; // OUTA
    #100;
    
    // SUBTRACTION
    #40 in_data = user_num1;
    #40 in_data = user_num2;
    #40 in_data = 16'b0101000000000000; // SUB
    #40 in_data = 16'b0100000000000000; // OUTA
    #100;
    
    // MULTIPLICATION
    #40 in_data = user_num1;
    #40 in_data = user_num2;
    #40 in_data = 16'b0110000000000000; // MUL
    #40 in_data = 16'b0100000000000000; // OUTA
    #100;
    
    // DIVISION
    #40 in_data = user_num1;
    #40 in_data = user_num2;
    #40 in_data = 16'b0111000000000000; // DIV
    #40 in_data = 16'b0100000000000000; // OUTA
    #100;
    
    // MODULO
    #40 in_data = user_num1;
    #40 in_data = user_num2;
    #40 in_data = 16'b1000000000000000; // MOD
    #40 in_data = 16'b0100000000000000; // OUTA
    #100;
    
    // HALT
    #40 in_data = 16'b1111000000000000; // HALT
    
    #100;
    $display("================================================");
    $display("CALCULATION COMPLETE");
    $display("================================================");
    $finish;
end

// Monitor only the important outputs (clean output)
always @(out_led) begin
    if (out_led != 0) begin
        $display("RESULT: %d", out_led);
    end
end

// waveform dump
initial begin
    $dumpfile("../OutputFiles/dump.vcd");
    $dumpvars(0, CPU_tb);
    #2000 $finish;
end

endmodule
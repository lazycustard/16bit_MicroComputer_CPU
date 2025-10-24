`timescale 1ns/1ps
module CPU(
    input clk,
    input reset,
    input [15:0] IN_REG_out,  // input register
    output reg [15:0] out_led,
    output [15:0] ALU_out,
    output [15:0] REG_A_out,
    output [15:0] REG_B_out,
    output [15:0] PC_out,
    output [15:0] IR_out,
    output Zero,
    output Carry
);

// internal registers
reg [15:0] REG_A, REG_B;
reg [15:0] PC;
reg [15:0] IR;
reg [15:0] ALU_result;
reg Zero_flag, Carry_flag;

wire [15:0] RAM_data;
reg [15:0] RAM_addr;

// continuous assignments to outputs
assign ALU_out   = ALU_result;
assign REG_A_out = REG_A;
assign REG_B_out = REG_B;
assign PC_out    = PC;
assign IR_out    = IR;
assign Zero      = Zero_flag;
assign Carry     = Carry_flag;

// RAM instantiation
RAM ram_inst(
    .addr(RAM_addr),
    .data(RAM_data)
);

// main CPU logic
always @(posedge clk or posedge reset) begin
    if(reset) begin
        PC <= 0;
        RAM_addr <= 0;
        REG_A <= 0;
        REG_B <= 0;
        ALU_result <= 0;
        IR <= 0;
        out_led <= 0;
        Zero_flag <= 0;
        Carry_flag <= 0;
    end else begin
        RAM_addr <= PC;       // set RAM address
        IR <= RAM_data;       // fetch instruction
        PC <= PC + 1;         // increment PC

        case(IR[15:12])
            4'b0001: REG_A <= IN_REG_out;           // LOADA_IN
            4'b0010: REG_B <= IN_REG_out;           // LOADB_IN
            4'b0011: begin                          // ADD
                        ALU_result <= REG_A + REG_B;
                        Zero_flag <= (REG_A + REG_B == 0);
                        Carry_flag <= (REG_A + REG_B > 16'hFFFF);
                     end
            4'b0101: begin                          // SUB
                        ALU_result <= REG_A - REG_B;
                        Zero_flag <= (REG_A - REG_B == 0);
                        Carry_flag <= (REG_B > REG_A);
                     end
            4'b0110: begin                          // MUL
                        ALU_result <= REG_A * REG_B;
                        Zero_flag <= (REG_A * REG_B == 0);
                        Carry_flag <= 0;
                     end
            4'b0111: begin                          // DIV
                        if (REG_B != 0) begin
                            ALU_result <= REG_A / REG_B;
                            Zero_flag <= (REG_A / REG_B == 0);
                        end else begin
                            ALU_result <= 0;  // Division by zero
                            Zero_flag <= 1;
                        end
                        Carry_flag <= 0;
                     end
            4'b1000: begin                          // MOD
                        if (REG_B != 0) begin
                            ALU_result <= REG_A % REG_B;
                            Zero_flag <= (REG_A % REG_B == 0);
                        end else begin
                            ALU_result <= 0;  // Modulo by zero
                            Zero_flag <= 1;
                        end
                        Carry_flag <= 0;
                     end
            4'b0100: begin                          // OUTA
                        out_led <= REG_A;
                        $display("LED_OUTPUT=%h (decimal: %d)", REG_A, REG_A);
                     end
            4'b1111: $stop;                         // HALT
            default: ;                              // NOP
        endcase
    end
end

endmodule
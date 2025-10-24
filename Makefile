# Makefile for 16-bit CPU project

VERILOG_DIR = VerilogModules
TB = $(VERILOG_DIR)/CPU_tb.v
OUT = CPU_tb.out
WAVE = OutputFiles/dump.vcd

all: sim

sim:
	iverilog -o $(OUT) $(TB)
	vvp $(OUT)
	gtkwave $(WAVE)

clean:
	rm -f $(OUT) $(WAVE)

# 16-Bit MicroComputer CPU

![Verilog](https://img.shields.io/badge/Verilog-FF0000?style=for-the-badge\&logo=verilog\&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![Arduino](https://img.shields.io/badge/Arduino-00979D?style=for-the-badge\&logo=arduino\&logoColor=white)

### The 16bit_MicroComputer_CPU is a 16-bit processor based on the Von Neumann architecture, meticulously implemented using Verilog HDL. It comes equipped with a Python-based assembler for streamlined program development and leverages an ALU for efficient arithmetic and logical operations. The processor supports memory-mapped I/O, enabling seamless interaction with external devices. Additionally, an Arduino-controlled LED interface provides real-time visualization of instruction execution, data movement, and low-level hardware computations, making it an ideal platform for both learning and experimenting with processor design and embedded systems.
---

## Table of contents

* [Overview](#overview)
* [Features](#features)
* [Demo Programs](#demo-programs)
* [Project Structure](#project-structure)
* [Instruction Set](#instruction-set)
* [Quick start](#quick-start)


  * [Prerequisites](#prerequisites)

  * [Running the Calculator](#running-the-calculator)
  * [Simulation Ouput](#simulation-output)
  * [Running the LED Demo](#running-the-led-demo)
  * [With Arduino Hardware](#with-arduino-hardware)
* [Simulation output](#simulation-output)
* [Customizing and extending](#customizing-and-extending)

* [Future enhancements](#future-enhancements)

* [License](#license)

---

## Overview

This repository contains a learning-oriented implementation of a 16-bit microcomputer with a Von Neumann-style CPU, assembled and simulated using open-source tools. It is intended for education, experimentation, and hobbyist projects in computer architecture, digital design, and embedded systems integration.

The project includes:

* A synthesizable Verilog CPU design suitable for simulation with Icarus Verilog.
* A Python assembler and small toolchain for converting assembly programs into machine code.
* Demo programs: an interactive arithmetic calculator and LED visualization programs.
* Bridge code to connect simulation output to Arduino hardware for physical LED displays.
* Waveform output compatible with GTKWave for step-by-step debugging.

## Features

* Custom 16-bit CPU implemented in Verilog
* Python-based assembler and interactive tools
* Arithmetic calculator with addition, subtraction, multiplication, division and modulo
* Memory-mapped I/O and LED visualization
* Waveform generation (VCD) for GTKWave analysis
* Simple Arduino integration for real hardware visualization

## Demo Programs

**Calculator Demo**

* Supports: addition, subtraction, multiplication, division, modulo
* Interactive input via Python tool
* Waveform output for detailed tracing and debugging
* Step-by-step instruction execution visible in GTKWave

**LED Demo**

* Sequential and binary lighting patterns
* Hardware-ready sequences that can be sent to an Arduino
* Easy to extend with new assembly programs

## Project Structure

```
16bit_MicroComputer_CPU/
├── Assembler/                 # Custom assembler and Python tools
│   ├── Assembler_v2.py       # Main assembler program
│   ├── Calculator.asm        # Calculator demo program
│   ├── LEDDemo.asm           # LED demonstration program
│   ├── interactive_calculator.py  # Interactive calculator
│   └── led_bridge.py         # Arduino communication bridge
├── VerilogModules/           # CPU hardware design
│   ├── CPU.v                # Main CPU module
│   ├── ALU.v                # Arithmetic Logic Unit
│   ├── REG.v                # Register file
│   ├── RAM.v                # Memory module
│   ├── PC.v                 # Program Counter
│   ├── IR.v                 # Instruction Register
│   ├── FLAGS.v              # Status flags
│   ├── IO_REG.v             # Input/Output registers
│   └── CPU_tb.v             # Testbench for simulation
├── 16bit/                   # PlatformIO Arduino code
│   └── src/
│       └── main.cpp         # LED controller for Arduino
├── OutputFiles/             # Simulation outputs
│   └── dump.vcd            # Waveform data for GTKWave
└── Documentation/           # Project documentation
```

## Instruction Set

This minimal instruction set is designed to demonstrate arithmetic and I/O operations in the CPU.

| Instruction | Opcode | Description                          |
| ----------- | ------ | ------------------------------------ |
| LOADA_IN    | 0x1000 | Load immediate value into Register A |
| LOADB_IN    | 0x2000 | Load immediate value into Register B |
| ADD         | 0x3000 | Add Register A + Register B → A      |
| OUTA        | 0x4000 | Output Register A to LEDs            |
| SUB         | 0x5000 | Subtract Register A - Register B → A |
| MUL         | 0x6000 | Multiply Register A * Register B → A |
| DIV         | 0x7000 | Divide Register A / Register B → A   |
| MOD         | 0x8000 | Modulo Register A % Register B → A   |
| HALT        | 0xF000 | Stop program execution               |

> Note: To add more instructions, update the opcode dictionary in `Assembler/Assembler_v2.py` and implement the corresponding logic in `VerilogModules/CPU.v`.

## Quick start

### Prerequisites

Install the following tools before running the simulations and assembler:

* Python 3.x
* Icarus Verilog (iverilog, vvp)
* GTKWave (optional, for waveform viewing)
* Arduino IDE or PlatformIO (optional, for hardware integration)

### Running the Calculator (recommended)

1. Open a terminal and change to the `Assembler` folder:

```bash
cd Assembler
python interactive_calculator.py
```

2. Follow the prompts to enter two numbers and choose which operations to run. The assembler will generate machine code and optionally produce a VCD waveform file for GTKWave.
## 📊 Simulation Output

During simulation you will see real-time CPU execution with the following outputs:

### **Console Display**
```
CPU internal state updates (PC, registers, flags)
ALU inputs and outputs  
Memory and I/O register values
LED output values in hex/decimal
```

### **GTKWave Signals**
When viewing `OutputFiles/dump.vcd` in GTKWave, observe these signals:

**CPU Control:**
- `clk` - System clock
- `reset` - Reset signal

**Program Execution:**
- `PC_out [15:0]` - Program Counter (current instruction address)
- `IR_out [15:0]` - Instruction Register (current opcode)

**Data Processing:**
- `REG_A_out [15:0]` - Register A value
- `REG_B_out [15:0]` - Register B value
- `ALU_out [15:0]` - Arithmetic Logic Unit result
- `Zero` - Zero status flag
- `Carry` - Carry status flag

**Input/Output:**
- `in_data [15:0]` - Input data to CPU
- `in_reg_out [15:0]` - Input register output
- `out_led [15:0]` - LED output values (final results)

### **Waveform Analysis**
The VCD waveform file (`OutputFiles/dump.vcd`) provides detailed inspection capabilities in GTKWave, allowing you to track the complete execution pipeline and data flow through your CPU.

### Running the LED Demo

Assemble and simulate the LED demo the same way as the calculator demo:

````bash
```powershell
cd Assembler
python Assembler_v2.py LEDDemo.asm
python led_bridge.py
````

### With Arduino Hardware
- Open the `16bit` folder in VS Code with the PlatformIO extension and press the **Upload** button in the PlatformIO toolbar. If command-line PlatformIO fails, try specifying the environment: `pio run -e <env> -t upload`.

Hardware: LED circuit (breadboard)

**Components**

- USB cable and Arduino board (Uno / ATmega328P assumed)
- 10 LEDs
- 10 resistors (220–470 Ω; 330 Ω recommended)
- Breadboard and jumper wires

**Wiring steps**

1. Connect the Arduino GND to the breadboard ground rail.
2. Map 10 digital pins on the Arduino to the LEDs (example mapping below). You can change pins in `16bit/src/main.cpp` if needed.

| LED   | Arduino pin |
|-------|-------------|
| LED1  | D2          |
| LED2  | D3          |
| LED3  | D4          |
| LED4  | D5          |
| LED5  | D6          |
| LED6  | D7          |
| LED7  | D8          |
| LED8  | D9          |
| LED9  | D10         |
| LED10 | D11         |

3. For each LED: place the LED on the breadboard with the long leg (anode) connected to the Arduino digital pin through a resistor, and the short leg (cathode) connected to the ground rail.
4. Use a 220–470 Ω resistor in series with each LED (330 Ω is a good default).
5. Power the Arduino via the USB cable. The board will supply 5 V to the digital pins while running.

**Safety and notes**

- Never drive an LED without a series resistor.
- Verify the pin assignment in `16bit/src/main.cpp` matches the wiring before uploading.

After the firmware is uploaded, run the Python bridge to stream LED data to the Arduino.

Notes and troubleshooting:

* Make sure the serial port configured in `led_bridge.py` matches the port your Arduino uses (e.g., `COM3`).
* Close the Arduino IDE Serial Monitor before running `led_bridge.py`, since only one program can open the serial port at a time.
* On Windows, install the appropriate USB drivers if the board is not detected.


## Customizing and extending

### Adding new instructions

1. Add the new opcode to `Assembler/Assembler_v2.py` to make the assembler generate the correct machine word.
2. Implement the instruction decoding and behavior in `VerilogModules/CPU.v` and any affected modules (ALU, FLAGS, IO_REG).
3. Add test assembly programs and update the testbench if necessary.

### Creating new programs

1. Write assembly code in a `.asm` file using the instruction set.
2. Assemble with `python Assembler_v2.py your_program.asm`.
3. Simulate the design as shown above and verify output.

## Future enhancements

Planned features that would make the architecture more complete:

* Jump/branch instructions and richer program flow control
* Interrupt handling and basic interrupt controller
* Stack operations and subroutine calls
* Serial communication peripherals and UART driver
* Expanded memory and addressing modes
* A small runtime or bootloader to run more complex programs
* Integration with FPGA toolchains for synthesis


## License

This project is released under the MIT License. See the `LICENSE` file for full terms.









#!/usr/bin/env python3
import serial
import time
import sys
import os

class LEDBridge:
    def __init__(self, port=None, baudrate=115200):
        self.port = port
        self.baudrate = baudrate
        self.ser = None
        
    def connect(self):
        """Auto-detect and connect to Arduino"""
        if self.port:
            ports = [self.port]
        else:
            # Common Arduino ports
            if sys.platform.startswith('win'):
                ports = [f'COM{i}' for i in range(1, 10)]
            elif sys.platform.startswith('linux'):
                ports = ['/dev/ttyUSB0', '/dev/ttyUSB1', '/dev/ttyACM0', '/dev/ttyACM1']
            elif sys.platform.startswith('darwin'):  # macOS
                ports = ['/dev/cu.usbmodem', '/dev/cu.usbserial']
            else:
                ports = []
        
        for port in ports:
            try:
                print(f"Trying {port}...")
                self.ser = serial.Serial(port, self.baudrate, timeout=1)
                time.sleep(2)  # Wait for Arduino reset
                print(f"Connected to Arduino on {port}")
                return True
            except (serial.SerialException, OSError) as e:
                print(f"Failed to connect to {port}: {e}")
                continue
        
        print("Could not connect to Arduino")
        return False
    
    def send_led_value(self, value):
        """Send 16-bit value to Arduino"""
        if not self.ser:
            print("Not connected to Arduino")
            return False
            
        try:
            # Send as little-endian
            data = bytes([value & 0xFF, (value >> 8) & 0xFF])
            self.ser.write(data)
            print(f"Sent: {value} (binary: {value:016b})")
            
            # Wait for acknowledgment
            ack = self.ser.read(1)
            return ack == b'\xAA'
        except Exception as e:
            print(f"Error sending data: {e}")
            return False
    
    def close(self):
        if self.ser and self.ser.is_open:
            self.ser.close()

class CPUSimulator:
    def __init__(self):
        self.reg_a = 0
        self.reg_b = 0
        self.bridge = LEDBridge()
        
    def execute_instruction(self, instruction):
        """Execute a single instruction and return True if OUTPUT occurred"""
        # Remove any comments and whitespace
        instruction = instruction.split(';')[0].strip()
        if not instruction:
            return False
            
        opcode = instruction[0:4]
        
        if opcode == "0001":  # LOADA_IN
            value = int(instruction[4:], 2)
            self.reg_a = value
            print(f"LOADA_IN: Register A = {self.reg_a}")
            return False
            
        elif opcode == "0010":  # LOADB_IN
            value = int(instruction[4:], 2)
            self.reg_b = value
            print(f"LOADB_IN: Register B = {self.reg_b}")
            return False
            
        elif opcode == "0100":  # OUTA
            # Send reg_a to LEDs
            print(f"OUTA: OUTPUT to LEDs = {self.reg_a} (binary: {self.reg_a:016b})")
            success = self.bridge.send_led_value(self.reg_a)
            return True
            
        elif opcode == "0101":  # SUBA_B
            result = self.reg_a - self.reg_b
            print(f"SUBA_B: {self.reg_a} - {self.reg_b} = {result}")
            self.reg_a = result
            return False
            
        elif opcode == "1111":  # HALT
            print("HALT: Program stopped")
            return True
            
        else:
            print(f"Unknown opcode: {opcode} - Instruction: {instruction}")
            return False
    
    def run_from_assembler_output(self, filename='binary.txt'):
        """Run a program from assembler output file"""
        if not self.bridge.connect():
            print("Failed to connect to Arduino")
            return False
            
        try:
            with open(filename, 'r') as f:
                instructions = f.readlines()
            
            print("=" * 50)
            print("STARTING CPU SIMULATION")
            print("=" * 50)
            print("Running from assembler output:", filename)
            print("=" * 50)
            
            instruction_count = 0
            output_count = 0
            
            for i, instruction_line in enumerate(instructions):
                instruction_line = instruction_line.strip()
                
                if self.execute_instruction(instruction_line):
                    output_count += 1
                    time.sleep(1)  # Delay after OUTPUT so humans can see it
                else:
                    time.sleep(0.1)  # Small delay between instructions
                    
                instruction_count += 1
            
            print("=" * 50)
            print(f"SIMULATION COMPLETE")
            print(f"Instructions executed: {instruction_count}")
            print(f"LED outputs sent: {output_count}")
            print("=" * 50)
            return True
            
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
            print("Please assemble your ASM file first: python Assembler_v2.py LEDDemo.asm")
            return False
        except Exception as e:
            print(f"Error during simulation: {e}")
            return False
        finally:
            self.bridge.close()

if __name__ == "__main__":
    # Run CPU simulation directly with binary.txt
    cpu = CPUSimulator()
    filename = "binary.txt"
    
    print("16-BIT MICROCOMPUTER CPU SIMULATOR")
    print("Running LED Demo from assembler output...")
    
    success = cpu.run_from_assembler_output(filename)
    
    if success:
        print("🎉 Simulation finished successfully!")
    else:
        print("❌ Simulation failed. Check the error messages above.")
    
    input("Press Enter to exit...")
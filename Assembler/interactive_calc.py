#!/usr/bin/env python3
import os
import subprocess

class InteractiveCalculator:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0
    
    def run(self):
        """Main calculator function"""
        print(" 16-BIT CPU INTERACTIVE CALCULATOR")
        print("=" * 50)
        
        self.get_user_input()
        self.save_user_inputs()
        self.run_simulation()
        self.show_results()
        self.ask_for_waveform()
    
    def get_user_input(self):
        """Get numbers from user"""
        try:
            self.num1 = int(input("Enter first number (0-255): "))
            self.num2 = int(input("Enter second number (0-255): "))
            
            if self.num1 < 0 or self.num1 > 255 or self.num2 < 0 or self.num2 > 255:
                print("Numbers must be between 0-255")
                return False
            return True
        except ValueError:
            print("Please enter valid numbers")
            return False
    
    def save_user_inputs(self):
        """Save user numbers to file for Verilog to read"""
        with open("user_inputs.txt", "w") as f:
            f.write(f"{self.num1} {self.num2}")
        print(f" Numbers saved: {self.num1} and {self.num2}")
    
    def run_simulation(self):
        """Run the simulation with user numbers"""
        print(" Running simulation...")
        
        os.chdir("../VerilogModules")
        
        
        result = subprocess.run([
            "iverilog", "-o", "CPU_tb.out", "*.v"
        ], capture_output=True, text=True)
        
        if result.returncode != 0:
            print(f" Compilation failed: {result.stderr}")
            return False
        
        result = subprocess.run(["vvp", "CPU_tb.out"], capture_output=True, text=True)
        
        print("\n" + "=" * 50)
        print("SIMULATION RESULTS")
        print("=" * 50)
        
        for line in result.stdout.split('\n'):
            if "USER CALCULATOR:" in line:
                print(line)
            elif "RESULT:" in line:
                print(line)
            elif "CALCULATION COMPLETE" in line:
                print(line)
        
        return True
    
    def show_results(self):
        """Show calculation results"""
        print("\n" + "=" * 50)
        print(" CALCULATION SUMMARY")
        print("=" * 50)
        print(f"Input Numbers: {self.num1} and {self.num2}")
        print("-" * 30)
        print(f" ADD: {self.num1} + {self.num2} = {self.num1 + self.num2}")
        print(f" SUB: {self.num1} - {self.num2} = {self.num1 - self.num2}")
        print(f"  MUL: {self.num1} * {self.num2} = {self.num1 * self.num2}")
        if self.num2 != 0:
            print(f" DIV: {self.num1} / {self.num2} = {self.num1 // self.num2}")
            print(f" MOD: {self.num1} % {self.num2} = {self.num1 % self.num2}")
        else:
            print(f" DIV: {self.num1} / {self.num2} = Error (division by zero)")
            print(f" MOD: {self.num1} % {self.num2} = Error (modulo by zero)")
        print("=" * 50)
    
    def ask_for_waveform(self):
        """Ask user if they want to see waveform"""
        choice = input("\n📊 Would you like to see the waveform in GTKWave? (y/n): ").lower()
        
        if choice == 'y' or choice == 'yes':
            print("🔄 Opening GTKWave...")
            gtkwave_path = "C:/iverilog/gtkwave/bin/gtkwave.exe"
            dump_path = "C:/Users/Amit Gupta/Desktop/16bit_micro/OutputFiles/dump.vcd"
            
            try:
                subprocess.Popen([gtkwave_path, dump_path])
                print(" GTKWave launched!")
                print(" Look for:")
                print("   - in_data: Your input numbers")
                print("   - out_led: Calculation results")
                print("   - ALU_out: ALU outputs")
                print("   - REG_A_out, REG_B_out: Registers")
            except Exception as e:
                print(f" Error: {e}")
        else:
            print(" Calculator session complete!")

if __name__ == "__main__":
    calculator = InteractiveCalculator()
    calculator.run()

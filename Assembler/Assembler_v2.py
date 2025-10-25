import sys

OPCODES = {
    'NOP'      : 0x0000,
    'LOADA_IN' : 0x1000,
    'LOADB_IN' : 0x2000,
    'ADD'      : 0x3000,
    'OUTA'     : 0x4000,
    'SUB'      : 0x5000,
    'HALT'     : 0xF000,
    'MULT'      : 0x6000,  
    'DIV'      : 0x7000,   
    'MOD'      : 0x8000,   
    'LOADA'    : 0x9000,   # For LED demo (LOADA immediate)
}

def assemble(filename):
    output_lines = []
    with open(filename, 'r') as f:
        lines = f.readlines()

    for line_num, line in enumerate(lines, start=1):
        line = line.strip()
        if not line:
            continue  # skip empty

        if ';' in line:
            line = line.split(';')[0].strip()

        if not line:
            continue

        parts = line.split()
        op = parts[0].upper()

        if op not in OPCODES:
            print(f"Error (line {line_num}): Unknown instruction '{op}'")
            sys.exit(1)

        if len(parts) > 1:
            try:
                operand = int(parts[1], 0) 
            except ValueError:
                print(f"Error (line {line_num}): Invalid operand '{parts[1]}' in line: {line}")
                sys.exit(1)
        else:
            operand = 0

        instr = OPCODES[op] | (operand & 0x0FFF)
        bin_str = format(instr, '016b')  
        output_lines.append(bin_str)

    # Write output
    with open('binary.txt', 'w') as f:
        for line in output_lines:
            f.write(line + '\n')

    print("✅ Assembly successful! Created 'binary.txt'.")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python Assembler_v2.py <inputfile.asm>")
    else:
        assemble(sys.argv[1])


# The index into the memory array is also called location, address, or pointer

# 1 PRINT_NATALIE
# 2 - HALT
# 3 - SAVE_REG store a value in a register

## pc points to instructin and skips executables

memory = [ # think of as a big array of bytes, 8-bits per byte
    # one byte instruction (increment pc by 1)
    
    1, # PRINT_NATALIE
    ## two byte instruction ( increment pc by 2)

    3, # SAVE_REG R4 37, instruction itself is also called "opcode"
    4, # 4 and 37 are arguments to SAVE_REG, also called "operands"
    37, # value to be assigned to register

    ## two byte instruction ( increment pc by 2)
    4, # PRINT_REG R4
    4,

    2 # HALT
]

"""
registers[3] = 37
"""

registers = [0] * 8

running = True

pc = 0 # Program Counter, the inddex into memory of the currently-executing instruction

while running:
    ir = memory[pc] # ir is Instruction Register - an internal part of CPU that holds a value (currently-executing instruction) that is not RA
    if ir == 1: # PRINT_NATALIE
        print("Natalie!")
        pc += 1

    elif ir == 2: # HALT
        running = False
        pc += 1

    elif ir == 3: # SAVE_REG
        reg_num = memory[pc + 1]
        value = registers[pc + 2] 
        registers[reg_num] = value
        # print(f"{registers[reg_num]} = {value}")
        pc += 3

    elif ir == 4: # PRINT_REG
        reg_num = memory[pc + 1]
        print(registers[reg_num])
        pc += 2
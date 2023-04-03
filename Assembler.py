tag_dic = {}

opcodes = {
    'ADDI': '000000',
    'SUBI': '000001',
    'ANDI' : '000010',
    'ORI'  : '000011',
    'XORI' : '000100',
    'SLLI' : '000101',
    'SRLI' : '000110',
    'ROLI' : '000111',
    'RORI' : '001000',
    'SLTI' : '001001',
    'SGTI' : '001010',
    'SLEI' : '001011',
    'SGEI' : '001100',
    'UGTI' : '001101',
    'ULTI' : '001110',
    'ULEI' : '001111',
    'UGEI' : '010000',
    'SRAI' : '010001',
    'LHI' :  '010010',
    'J'   :  '010011',
    'JAL' :  '010100',
    'BEZ' :  '010101',
    'BNEZ':  '010110',
    'SB'  :  '010111',
    'SW'  :  '011000',
    'SWH' :  '011001',
    'LB'  :  '011010',
    'LW'  :  '011011',
    'LWH' :  '011100',
    'JR'  :  '011101',
    'JALR':  '011110'


}

funct_codes = {

     'ADD' : '000000',
     'SUB' : '000001',
     'AND' : 'b000010',
     'OR'  : 'b000011',
     'XOR' : 'b000100',
     'SLL' : 'b000101',
     'SRL' : 'b000110',
     'ROL' : 'b000111',
     'ROR' : 'b001000',
     'SLT' : 'b001001',
     'SGT' : 'b001010',
     'SLE' : 'b001011',
     'SGE' : 'b001100',
     'UGT' : 'b001101',
     'ULT' : 'b001110',
     'ULE' : 'b001111',
     'UGE' : 'b010000',
     'SRA' : 'b010001'
}

Rtriadic_funcode = [     'ADD',
     'SUB',
     'AND',
     'OR',
     'XOR',
     'SLL',
     'SRL',
     'ROL',
     'ROR',
     'SLT',
     'SGT',
     'SLE',
     'SGE',
     'UGT',
     'ULT',
     'ULE',
     'UGE',
     'SRA']

RItriadic_opcode = ['ADDI',
    'SUBI',
    'ANDI' ,
    'ORI'  ,
    'XORI' ,
    'SLLI' ,
    'SRLI' ,
    'ROLI' ,
    'RORI' ,
    'SLTI' ,
    'SGTI' ,
    'SLEI' ,
    'SGEI' ,
    'UGTI' ,
    'ULTI' ,
    'ULEI' ,
    'UGEI' ,
    'SRAI' ,
    ]

RItriadic_LS = ['LHI'  ,
    'SB'   ,
    'SW'   ,
    'SWH' ,
    'LB'  ,
    'LW'  ,
    'LWH']

Rdiadic_opcode = ['BEZ',
    'BNEZ','JR',
    'JALR']

Jtype_opcode = ['J','JAL']


# Define a function to assemble an R-type triadic instruction
def assemble_Rtriadic(instruction, count):
    if(count == 4):
        t, opcode, rs, rt, rd = instruction.split(' ')
    else:
        opcode, rs, rt, rd = instruction.split(' ')
    opcode_binary = '000000'
    funct_binary = funct_codes[opcode]
    
    # Convert the opcode and funct code to binary
    opcode_binary = '000000'
    funct_binary = funct_codes[opcode]
    
    # Convert the register numbers to binary
    rs_binary = format(int(rs[1:]), '05b')
    rt_binary = format(int(rt[1:]), '05b')
    rd_binary = format(int(rd[1:]), '05b')
    
    # Build the 32-bit machine code instruction
    machine_code = opcode_binary + rs_binary + rt_binary + rd_binary + '00000' + funct_binary
    
    # Return the machine code as a string
    return machine_code


def assemble_RItriadic(instruction, count):
    if(count == 4):
        t, opcode, rs, rd, imm = instruction.split(' ')
    else:
        opcode, rs, rd, imm = instruction.split(' ')
    opcode_binary = opcodes[opcode]
    funct_binary = '000000'

    rs_binary = format(int(rs[1:]), '05b')
    rd_binary = format(int(rd[1:]), '05b')
    imm_binary = format(int(imm), '016b')

    machine_code = opcode_binary + rs_binary + rd_binary + imm_binary 

    return machine_code

def assemble_RItriadic_LR(instruction, count):
    if(count == 4):
        t, opcode, rd, imm = instruction.split(' ')
    else:
        opcode, rd, imm = instruction.split(' ')
    imm, rs = imm.split('(')
    rs, x = rs.split(')')
    opcode_binary = opcodes[opcode]
    funct_binary = '000000'

    rs_binary = format(int(rs[1:]), '05b')
    rd_binary = format(int(rd[1:]), '05b')
    imm_binary = format(int(imm), '016b')

    machine_code = opcode_binary + rs_binary + rd_binary + imm_binary 

    return machine_code


def assemble_Rdiadic(instruction, count):
    if(count == 4):
        t, opcode, rs, imm, rd = instruction.split(' ')
    else:
        opcode, rs, imm, rd = instruction.split(' ')


    opcode_binary = opcodes[opcode]
    funct_binary = '000000'

    rs_binary = format(int(rs[1:]), '05b')
    rd_binary = format(int(rd[1:]), '05b')
    imm_binary = format(int(imm), '016b')

    machine_code = opcode_binary + rs_binary + '00000' + imm_binary 


    return machine_code


def assemble_J(instruction):

    opcode, label = instruction.split(' ')
  
    opcode_binary = opcodes[opcode]
    target_address = tag_dic[label]

    target_address_binary = format(target_address, '026b')
    machine_code = opcode_binary + target_address_binary

    return machine_code

def assembler_line(instruction, j):
    count=0
    
    for i in range(0,len(instruction)):
         if instruction[i]==" ":
              count+=1
     
  
    if(count == 3):
        opcode, rs, rt, rd = instruction.split(' ')
    elif(count == 4):
        tag, opcode, rs, rt, rd = instruction.split(' ')
        tag, y = tag.split(':')
        tag_dic[tag] = j

    elif(count == 1):
        opcode, imm = instruction.split(' ')
    else:
        opcode, rs, rd = instruction.split(' ')

    if opcode in Rtriadic_funcode:
      output = assemble_Rtriadic(instruction, count)

    elif opcode in RItriadic_opcode:
      output = assemble_RItriadic(instruction, count)

    elif opcode in RItriadic_LS:
      output = assemble_RItriadic_LR(instruction, count)
    elif opcode in Rdiadic_opcode:
      output = assemble_Rdiadic(instruction, count)

    elif opcode in Jtype_opcode:
      output = assemble_J(instruction)
    return output
    

n = int(input())
inst = []

for i in range(n):
  x = str(input()) 
  inst.append(x)

for i in range(n):
  print(assembler_line(inst[i], i))






## RISC V CPU
Link to the medium article - https://medium.com/programmatic/how-to-design-a-risc-v-processor-12388e1163c

RISC-V is an open source Instruction Set Architecture(ISA). Instruction Set Architecture in RISC-V defines the set of 
instructions the CPU can execute.The CPU will perform 12 basic operations defined in RISC-V instruction set and can be 
easily extended to include more advanced as well as custom instruction sets. RISC stands for Reduced Instruction Set
Computers. The CPU is single cycled and not pipelined, that means we will fully execute one instruction before executing
the next instruction. 

### Steps involved in executing single instruction
1. Instruction fetch: read instruction from memory
2. Instruction decode: understand what instruction means
3. Execute: perform the operation defined in instruction
4. Memory access: read required memory locations if needed
5. Write back: write the data to memory if modified


Let's learn how to write a singled cycle (not pipelined) CPU :)
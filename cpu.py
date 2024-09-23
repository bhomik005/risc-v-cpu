from myhdl import block, always, delay, always_comb
from defs import *
'''
clk signal is changing after every 10 nanoseconds
The clock block will run util the CPU is running
'''
@block
def clock(clk):
    @always(delay(10))
    def clck():
        clk.next = not clk
    return clck


"""
program counter adder - increments the program counter by 1 (points to next instruction in the memory)
pc = pc + 1
"""
@block
def pc_adder(reset, step, pc, pc_addr):

    @always(step.posedge)
    def padder():
        if reset.next == INACTIVE_HIGH:
            pc_addr.next = (pc.next + 1)
    return padder


'''
jmp_adder is kind of an ALU used for branching
it calculated the jump address based on the current location in memory and shift value
how much to shift the read address to compute the new address
'''
@block
def jmp_adder(reset, jmp_addr, shl, read_addr):

    @always_comb
    def jadder():
        if reset.next == INACTIVE_HIGH:
            jmp_adder.next = read_addr + shl

    return jadder

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

'''
program counter sel mux - if pc_sel is high, then the next program instruction execution moved to the jump address
else it is incremented to the next PC
'''
@block
def pc_mux(pc_addr, jmp_addr, pc_sel, reset, pc):

    @always_comb
    def pmux():
        if reset.next == INACTIVE_HIGH:
            if pc_sel:
                pc.next = jmp_addr
            else:
                pc.next = pc_addr
    return pmux

@block
def taken(result, brnch, pc_sel):

    @always_comb
    def take():
        if (not result) and (brnch):
            pc_sel.next = True  # branch is taken
        else:
            pc_sel.next = False # branch is not taken

    return take

'''
this module assigns next PC to the instruction data memory, triggering the start of the next instruction execution
'''
@block
def pc_assign(reset, read_addr, pc):

    @always_comb
    def assign():
        if reset.next == INACTIVE_HIGH:
            read_addr.next = pc
    return assign
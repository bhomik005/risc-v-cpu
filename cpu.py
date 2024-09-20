from myhdl import block, always, delay

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



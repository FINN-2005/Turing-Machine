from classes import Turing_Machine
from funcs import *

''' ### TODO: Add more funcs '''


tm = Turing_Machine()

*vals, tape = get_unary_addition()

tm.set_values(*vals, step_limit=50)
tm.set_tape(tape)

tm.compute()
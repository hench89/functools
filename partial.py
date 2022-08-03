from functools import partial, partialmethod
import sys

## example 1: using partail to turn multi argument functions into single arguments.

def pow(number, exp):
    return number**exp

pow_2 = partial(pow, exp=2)
result = pow_2(5)
print('power of 2 for 5 ==', result)

## example 2: single argument functions are can be used by map function
## can also be done with lambda, but reads better this way

pow_3 = partial(pow, exp=3)
result = list(map(pow_3, range(0, 10)))
print('list of pow_3 results', result)

## example 3: another example
print_stderr = partial(print, file=sys.stderr)
print_stderr('stderr: found something unexpected!')


## example 4: partialmethod for classes

class Cell:
    def __init__(self):
        self.alive = True
    def set_state(self, state):
        self._alive = bool(state)
    set_alive = partialmethod(set_state, True)
    set_dead = partialmethod(set_state, False)

c = Cell()
print('cell state ==', c.alive)
c.set_dead()
print('cell state ==', c.alive)
c.set_alive()
print('cell state ==', c.alive)

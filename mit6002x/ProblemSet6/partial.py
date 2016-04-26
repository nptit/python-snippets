from functools import partial

class Cell(object):
    def set_state(self, state):
        self._state = state
    set_alive = partial(set_state, state=True)
    set_dead = partial(set_state, state=False)



c = Cell()
c.set_state(True)
c.set_alive()

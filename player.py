from props import PROPS, Prop

class Player:

    def __init__(self, color):
        self.color = color
        self.first_move = True

        # GENERATE INVENTORY AND SPAWN POSITIONS OF PROPS
        self.inventory = [Prop((50+150*(i%(len(PROPS)/4)), 830-100*int(4*i/len(PROPS))), PROPS[i], self.color) for i in range(len(PROPS))]

from props import PROPS, Prop

class Player:

    def __init__(self, color):
        self.color = color
        self.first_move = True
        self.inventory = [Prop((10+120*(i%(len(PROPS)/4)), 450+90*int(4*i/len(PROPS))), PROPS[i], self.color) for i in range(len(PROPS))]

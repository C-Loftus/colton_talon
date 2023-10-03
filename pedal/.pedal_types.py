class PedalStateMap():
    left: bool
    right: bool
    center: bool

    wasHeld: bool

    def __init__(self) -> None:
        self.left = False
        self.right = False
        self.center = False
        self.wasHeld = False
    
    def __iter__(self):
        return iter([self.left, self.right, self.center])

    # @property
    # def left(self):
    #     return self.left
    
    # @left.setter
    # def left(self, value):
    #     self.left = value

    # @property
    # def right(self):
    #     return self.right
    
    # @right.setter
    # def right(self, value):
    #     self.right = value

    # @property
    # def center(self):
    #     return self.center
    
    # @center.setter
    # def center(self, value):
    #     self.center = value

    def reset(self):
        self.left = False
        self.right = False
        self.center = False

    def multiple_held(self):
        return sum([self.left, self.right, self.center]) >= 2
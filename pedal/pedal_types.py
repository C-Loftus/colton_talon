from typing import TypeVar, Generic


class PedalStateMap(Generic[T := TypeVar("T", bool, float)] ):

    pedals = ["left", "right", "center"]

    wasHeld: bool


    def __init__(self, type: T) -> None:


        if type not in T.__constraints__:
            raise ValueError(f"State Map type must be in {T.__constraints__}")
        
        init_default = type()

        for key in self.pedals:
            setattr(self, key, init_default)

        
        self.wasHeld = False
    
    def __iter__(self):

        return iter(self.pedals)
    
    # allow this item to be set like a dictionary
    def __setitem__(self, key: str, value: T):

        if key not in self.pedals:
            raise KeyError(f'Pedal must be in {self.pedals }')

        setattr(self, key, value)
            
    # allow this item to be accessed like a dictionary
    def __getitem__(self, key):
        
        if key not in self.pedals:
            raise KeyError(f'Pedal must be in {self.pedals }')

        return getattr(self, key)

    def __repr__(self) -> str:
        return [f"{key} : {getattr(self, key)}" for key in self.pedals]


    def reset(self):
        default_value = type(getattr(self, self.pedals[0]))() 
        for key in self.pedals:
            setattr(self, key, default_value)

    def multiple_held(self):
        return sum([getattr(self, key) for key in self.pedals]) >= 2
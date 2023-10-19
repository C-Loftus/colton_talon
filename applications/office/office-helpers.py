from talon import clip
from talon import Module, actions, app

mod = Module()

@mod.action_class
class Entrance:
    def email_entrance() -> str:
        """script the intro of an email"""
        res: str = clip.text()
        first= res.split(",")[1].strip()
        return first 
    
     
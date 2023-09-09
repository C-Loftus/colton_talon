from talon import Module, actions

mod = Module()



@mod.action_class
class Actions:
    def paste_delimited(text: str, delimiter: str="_", orientation: str = "column"):
        '''paste a column by default'''

        assert type(text) == str

        orientation=orientation.strip().lower()
        if orientation != "row" and orientation != "column":
            raise ValueError(f'Invalid orientation {orientation} specified')
        for word in text.split(delimiter): 
            actions.user.paste(word)
            if orientation == "row" :
               actions.key('tab')
            else:
               actions.key('down')

    
    
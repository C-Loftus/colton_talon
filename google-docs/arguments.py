from talon import Context, Module, actions, app

mod =   Module()

@mod.capture(rule="<number> | <user.letter>")
def alnum(m) -> str:
    try: return str(m.number)
    except AttributeError:
        return m.letter
from talon import Context, Module, actions, settings
import time, random, math, os

ctx = Context()
ctx.matches = """title: /Depop/
"""

ctx.settings['user.pedal_scroll_amount'] = 0.04
        

import math
import os
import random
import time

from talon import Context, Module, actions, settings

ctx = Context()
ctx.matches = """title: /Ebay/
"""

ctx.settings["user.pedal_scroll_amount"] = 0.04

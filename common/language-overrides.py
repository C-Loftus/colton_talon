from talon import Context, actions, Module

ctx = Context()
ctx.matches = r"""
app: vscode
title: /Untitled/
"""

@ctx.action_class("code")
class CodeActions:
    def language():
        return "markdown"
    

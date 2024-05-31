from talon import Context, Module, actions

ctx = Context()
ctx.matches = r"""
app: vscode
title: /Untitled/
"""


@ctx.action_class("code")
class CodeActions:
    def language():
        return "markdown"

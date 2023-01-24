title: /Google Docs/
# mode: command
# and mode: user.markdown
# mode: command
# and mode: user.auto_lang
# and code.language: markdown
-
# settings():
#     key_wait = 10.0
    
caps:
    mouse_click()
	mouse_click()
    text = edit.selected_text()
    result = user.formatted_text(text, "title")
    user.paste(result)

mini:
    mouse_click()
	mouse_click()
    text = edit.selected_text()
    result = user.formatted_text(text, "alldown")
    user.paste(result)
#  precision mouse, a warp function to move the mouse coarsely with my eyes, and the dense Mouse grid (alphabet soup)
style:
    mouse_click()
    mouse_click()
    text = edit.selected_text()
    key(alt-shift-i)
    key(e)
    insert(text)
    key(right)

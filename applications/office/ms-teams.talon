title: /Microsoft Teams/
mode: command
tag: browser

-

entrance <user.rango_target>:
    user.rango_command_with_target("copyElementTextContent", rango_target)
    name = user.email_entrance()
    "Hi {name}, "

# like <user.rango_target>:
#     user.rango_command_with_target("hoverElement", rango_target)
#     key(tab)
#     sleep(0.5)
#     key(enter)
#     user.rango_command_without_target("unhoverAll")
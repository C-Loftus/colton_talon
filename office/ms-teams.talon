title: /Microsoft Teams/
mode: command
tag: browser

-

entrance <user.rango_target>:
    user.rango_command_with_target("copyElementTextContent", rango_target)
    name = user.email_entrance()
    "Hi{name}, "
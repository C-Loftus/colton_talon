mode: command

-

departure:
    "\n\nThank you very much \nRegards,\nColton"

entrance <user.rango_target>:
    user.rango_command_with_target("copyElementTextContent", rango_target)
    name = user.email_entrance()
    "Dear{name},\nThank you very much for your email.\n"
    user.draft_hide()
    user.draft_show()

entrance:
    user.rango_command_with_target("copyElementTextContent", rango_target)
    name = user.email_entrance()
    "Hello,\nThank you very much for your email.\n"
    user.draft_hide()
    user.draft_show()
    

mode: command
title: /outlook.office.com/
tag: browser
-

departure:
    "\n\nThank you very much \nRegards,\nColton"

entrance <user.rango_target>:
    _ = user.rango_command_with_target("copyElementTextContent", rango_target)
    name = user.email_entrance()
    "Dear{name},\nThank you very much for your email.\n"

entrance:
    "Hello,\nThank you very much for your email.\n"

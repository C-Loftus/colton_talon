tag: browser
title: /.pdf/i
title: /PowerPoint/i
-

copy image <number>:
    user.notify("Coping image")
    key(ctrl-l)
    key(ctrl-c)
    url = clip.text()
    user.extract_PDF_page(url, number, "tmp")

save <number> as <user.text>:
    key(ctrl-l)
    key(ctrl-c)
    url = clip.text()
    user.extract_PDF_page(url, number, text)

tag: browser
title: /.pdf/i

-

copy image <number>:
    key(ctrl-l)
    key(ctrl-c)
    url = clip.text()
    user.extract_PDF_page(url, number, "tmp")

save <number> as <user.text>:
    key(ctrl-l)
    key(ctrl-c)
    url = clip.text()
    user.extract_PDF_page(url, number, text)


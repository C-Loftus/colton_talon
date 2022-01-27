title: /\.tex/

-
equation:
    user.paste("$$ $$")
    key(left:2)

section:
    user.paste("\n\n \\section{}\n")

text:
    insert("\\text{}")
    key(left)

divide:
    user.paste("\\frac{}")
    user.paste("{}")
    key(left:3)

make document:
    key(ctrl-alt-b)




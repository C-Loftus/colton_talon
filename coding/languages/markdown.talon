code.language: markdown

-

bullet: "- "
level two bullet: "   - "
level three bullet: "      - "

{user.markdown_code_block_language} block:
    user.insert_snippet("```{markdown_code_block_language}\n$0\n```")

code block:
    user.paste("```\n\n```")
    key(up)

# new footnote: 
#     user.paste("\\footnote{}")
#     key(left)

new citation: 
    user.paste("[@]")
    key(left)

new link: 
    user.paste("\\url{}")
    key(left)

new slide: 
    key(down)
    sleep(0.5)
    user.paste("\n---\n")

new footnote <number_small>: 
    user.paste("[^{number_small}]: ")

link footnote <number_small>: 
    user.paste(" [^{number_small}] ")
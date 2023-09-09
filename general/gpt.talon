mode: command

-

model fix grammar:
    res = user.gpt_fix_grammar()
    user.paste(res)

model summarize:
    res = user.gpt_summarize_this()
    user.paste(res)

# add context: 

#     res = user.add_context()
#     user.paste(res)

model query <user.text>:
    res = user.gpt_arbitrary_prompt(text)
    user.paste(res)


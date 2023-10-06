mode: command

-

model fix grammar:
    res = user.gpt_fix_grammar()
    user.paste(res)

model summarize:
    res = user.gpt_summarize_this()
    user.paste(res)

model add context: 
    res = user.gpt_add_context()
    key(right)
    key(enter)
    user.paste(res)

model ask <user.text>:
    res = user.gpt_answer_question(text)
    user.paste(res)

model arbitrary:
    text = user.draft_get_text()
    user.draft_hide()
    res = user.gpt_arbitrary_prompt(text)
    user.paste(res)


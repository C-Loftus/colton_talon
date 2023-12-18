mode: command

-


model ask <user.text>:
    res = user.gpt_answer_question(text)
    user.paste(res)

model arbitrary:
    text = user.draft_get_text()
    user.draft_hide()
    res = user.gpt_arbitrary_prompt(text)
    user.paste(res)

^model {user.promptNoArgument}$:
    result = user.gpt_prompt_no_argument(user.promptNoArgument)
    user.paste(result)


^model help$:
    user.help_list("user.promptNoArgument")
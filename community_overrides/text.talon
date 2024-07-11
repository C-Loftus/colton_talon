(word | were) <user.word>:
    user.add_phrase_to_history(word)
    insert(word)


body <user.prose>$: user.insert_formatted(prose, "ALL_LOWERCASE")
cap <user.prose>$: user.insert_formatted(prose, "CAPITALIZE_FIRST_WORD")



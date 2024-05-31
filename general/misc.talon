mode: command
-

# The visit command within rango is better than this
# target {user.website}:
#     user.launch_new_tab_if_not_opened("{website}")

# used for cursorless chaining
ergo:
    skip()

(fly | why):
    key(end)

voyage:
    key(volup:3)

vacate:
    key(voldown:3)

smile:
    key(volup)

frown:
    key(voldown)

^thumbs up$:
    user.paste("👍")

scope:
    user.paste("{\n\n}")
    key(up)

colgap:
    ": "
spam:
    ", "

bring screenshot:
    user.grab_browser_window_slow()
    sleep(0.5)
    user.focus_vscode()
    sleep(0.5)
    key(end)
    key(end)
    key(enter)
    key(ctrl-v)
    key(end)
    sleep(0.5)
    key(enter)
    key(end)
    user.focus_chrome()

cycle results:
    #we don't have loops so we just have to repeat. easier than using pythonfor this small example
    key(enter)
    sleep(2)
    key(enter)
    sleep(2)
    key(enter)
    sleep(2)
    key(enter)
    sleep(2)
    key(enter)
    sleep(2)
    key(enter)
    sleep(2)
    key(enter)
    sleep(2)
    key(enter)
    sleep(2)

# copy path:
# shift right click
# mimic()

alpha:
    user.paste("α")

beta:
    user.paste("β")

extract info:
    "for the information on this page, extract the company or sponrsor of the drug, the indication, the mechanism of action, route of administration, whether it requires a specific ER/HR/HER status, the line of therapy, the phase if it is a clinical trial, the mutation or gene target if applicable, any other important info and output it all in a bullet point format."

fat <user.word>:
    insert("{word}")
    sleep(.2)
    key(enter)

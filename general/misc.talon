mode: command
-

# pull all talon scripts:
#     user.system_command_nb("find ~/.talon/user -name .git -print -execdir git pull \;")

target {user.website}:
    user.launch_new_tab_if_not_opened("{website}")

queer line: edit.delete_line()

inter:
    key(enter)

(fly | why):
    key(end)

bullet:
    "* "

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

(scrape | scrip):
    edit.extend_word_left()
    edit.delete()


^and$:
    key(end)

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

    
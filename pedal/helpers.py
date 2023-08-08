from talon import Module, Context,cron, actions

def pedal_held_down(key, map, seconds):

    held_down=True

    def check_down():
        if not map[key]:
            held_down=False

    cron.interval(fd, on_interval)


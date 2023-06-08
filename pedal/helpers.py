from talon import Module, Context,cron
# Check if a pedal has been held down4444
def pedal_held_down(key, map, seconds):

    held_down=True

    def check_down():
        if not map[key]:
            held_down=False

    cron.interval(fd, on_interval)
 # echo Hello | osd_cat -p bottom -A center -o -80

# osd_cat -A center --pos bottom --color white -u transparent -f "-*-*-medium-*-*-*-*-*-*-*-*-120-*-*" token

# font is in the X font format
from multiprocessing import Process
import os
from tracemalloc import start
from talon import Module, actions, cron
import talon.linux
from threading import Thread

mod = Module()

@mod.action_class
class TimerActions:
    timer = None


        # os.system("echo {} | osd_cat --delay={} -A center --pos bottom --color white -u blue -O 2 -f {}".format(message, 0, font))


    # detect how long user has been working on the keyboard
    def start_timer(work_time_before_break: int, break_time: int):
        """
        Detect how long user has been working on the keyboard
        """
        from datetime import time, datetime
        import time as t
        import xcffib
        from xcffib import screensaver

        TimerActions.break_time = break_time

        # convert minutes to milliseconds
        wtms = work_time_before_break * 60 * 1000
        wtms_string_fmt = str(wtms) + "ms"

        btms = break_time * 60 * 1000

        def screen_print(message: str, font: str ="-*-*-medium-*-*-*-*-*-*-*-*-120-*-*"):
            """
            Prints a message on the screen
            """
            p = Thread(target=os.system, \
                args=("echo {} | osd_cat --delay={} \
                    -A center --pos bottom --color white -u blue -O 2 -f {}"
                    .format(message, 15, font),)
                )
            p.start()


        def idle():
            conn = xcffib.Connection()
            try:
                print("test")
                root = conn.get_setup().roots[0].root
                screen = conn(screensaver.key)
                reply = screen.QueryInfo(root).reply()
                time = reply.ms_since_user_input
                # idle time less than break time after work time means you need a break
                if time < btms:
                    screen_print("Take a Break, Idle time for {} seconds".format(time))
            finally:
                conn.disconnect()

        TimerActions.timer = cron.interval(wtms_string_fmt, idle)
        print(TimerActions.timer)

    def stop_timer():
        """
        Kill the timer
        """
        cron.cancel(TimerActions.timer)
        print("Timer killed")
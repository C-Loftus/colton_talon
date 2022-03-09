 # echo Hello | osd_cat -p bottom -A center -o -80

# osd_cat -A center --pos bottom --color white -u transparent -f "-*-*-medium-*-*-*-*-*-*-*-*-120-*-*" token

# font is in the X font format
from asyncio import subprocess
from email.mime import image
import os, sys
from re import sub
from time import sleep
from threading import Thread
from multiprocessing import Process
import subprocess

BLUE = "'#0373fc'"

def image_print():
    DIR = os.path.realpath(os.path.dirname(__file__)) + "/Assets" + "/thea.png"
    # pqiv -ciz 3 -P 2800,1080 Assets/thea.png
    img = subprocess.Popen(["pqiv", "-ciz", "2", "-P", "2800,1080", DIR])
    def wait_then_kill(time):
        sleep(time)
        img.terminate()
        return
    t = Thread(target=wait_then_kill, args=(5,))
    t.start()

def screen_print(message,  delay=2, font="-*-*-medium-*-*-*-*-*-*-*-*-120-*-*", position="bottom", color=BLUE):

    thread = Thread(target=os.system, \
        args=("echo {} | osd_cat --delay={} \
             -A center --pos {} --color white -u {} -O 2 -f {}"
             .format(message, delay, position, color, font),)
        )
    thread.start()

# detect how long user has been working on the keyboard
def timer_create(min_until_break, delay):
    import time as t
    seconds_until_break = min_until_break * 60

    screen_print("Timer starting with {} min intervals".format(min_until_break), delay)

    def idle_time():
        #xprintidle
        p = subprocess.Popen(["xprintidle"], stdout=subprocess.PIPE)
        out = p.stdout.read()
        p.terminate()
        return float(out) / 1000 / 60

    def work_time():
        time = 0
        breaksNotTaken = 0

        while True:
            # We can use slow polling since only long breaks matter
            t.sleep(30)
            time += 30
            # 5 min in milliseconds
            # If this is true then that means the user took a break 
            # and thus don't need to take another one

            # round to 4 decimal places
            print(f'Idle time = {round(idle_time(), 4)} minutes')

            if idle_time() > 5.0:
                time, breaksNotTaken = 0, 0
                print("break detected")
            elif (time) > (seconds_until_break):
                if breaksNotTaken > 50:
                    color = "red" 
                    # pqiv -cti
                    ROOT_DIR = os.path.realpath(os.path.dirname(__file__))
                    subprocess.Popen(["pqiv", "-ciz", "3", "-p", ROOT_DIR])
                else:
                    color = "blue"
                print('Displaying message to screen')
                screen_print('Time to take a break!', delay=delay, color=color)
                breaksNotTaken += 1

    p = Process(target=work_time)
    p.start()

    return p


if __name__ == '__main__':
    image_print()
    p = timer_create(20, delay=5)
    try:
        print('Timer started')
        while 1:
            sleep(60)
            pass
    except KeyboardInterrupt:
        print('Terminating')
        p.kill()
        sys.exit()
    # pqiv -cti thea.png
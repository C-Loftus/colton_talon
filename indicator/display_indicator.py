from talon import canvas, ui
from talon.skia import image
from talon.types import rect
from talon import Module
import os

# 100x100 image for thea

default_ubuntu = (1979, 33)
top_bar = (1928, 45)
left_dash_to_panel = (1975, 8)

config = default_ubuntu


if ui.screens()[0].y == 77:
    y = config[1] + 77
else:
    y = config[1]

x = config[0]



can = canvas.Canvas(x=x, y=y, width=30, height=30)

PATH = os.path.realpath(os.path.dirname(__file__)) + "/"
img=image.Image.from_file(PATH+"command.jpg")


mod = Module()
@mod.action_class
class Draw:

    def draw_mode(mode:str):
        """
        mixed
        """
        global img
        img = image.Image.from_file(PATH+mode+".jpg")
        # global can
        # FULLPATH = PATH+mode+".jpg"
        # can.draw_image(image.Image.from_file(FULLPATH), 0, 0)

   

def draw(skcanvas):
    skcanvas.draw_image(img, skcanvas.x, skcanvas.y)


drag_offset = None
def drag(ev):
    global drag_offset
    if ev.down and ev.button == 0:
        drag_offset = (ev.gpos.x - can.rect.x, ev.gpos.y - can.rect.y)
    elif ev.up:
        drag_offset = None
    elif ev.move and drag_offset is not None:
        can.rect = rect.Rect(
            ev.gpos.x - drag_offset[0],
            ev.gpos.y - drag_offset[1],
            can.rect.width,
            can.rect.height
        )


can.register("draw", draw)
can.register("mouse", drag)
can.blocks_mouse = True
# freeze means that draw only gets called ~once, saving a lot of CPU. If you want
# to redraw then just call freeze again.
# can.freeze()
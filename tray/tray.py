from operator import mod
from talon import canvas
from talon.skia import image
from talon.types import rect
from talon import Module


can = canvas.Canvas(x=1970, y=100, width=100, height=100)

PATH="/home/colton/.talon/user/myScripts/tray/"

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
from enum import Enum
from types import NoneType
from talon import Module, Context, app, registry, scope, skia, ui, actions, settings
from talon.canvas import Canvas
from talon.screen import Screen
from talon.skia.canvas import Canvas as SkiaCanvas
from talon.skia.imagefilter import ImageFilter
from talon.types import Rect
import json

mod = Module()
ctx = Context()

hotspot1 = mod.setting(
    "hotspot1",
    str,
    desc="Hotspot 1 settings",
    default='"x": 1, "y": 0, "radius": 20, "color": "099990", "alpha": 0.9,"gradient": 0.9'
)


hotspot_show = mod.setting(
    "hotspot_show",
    bool,
    desc="If true the hotspots are shown",
    default=True,
)


class Hotspot:
    x: float
    y: float
    radius: float
    color: str
    alpha: float
    gradient: float

    def __init__(self, rawConfigStr: str):


        assert rawConfigStr is not None

        d = {}
        split = rawConfigStr.split(" ")
        # convert groups of 2 to key value pairs
        for i in range(0, len(split), 2):
            d[split[i]] = split[i + 1]
        
        conf = d

        self.x = int(conf["x"])
        self.y = int(conf["y"])
        self.radius = int(conf["radius"])
        self.color = conf["color"]
        self.alpha = float(conf["alpha"])
        self.gradient = float(conf["gradient"])

        self.canvas: Canvas = None
        
    def get_alpha_color(self) -> str:
        return f"{int(self.alpha * 255):02x}"
    
    def get_gradient_color(self, color: str) -> str:
        factor = self.gradient
        # hex -> rgb
        (r, g, b) = tuple(int(color[i : i + 2], 16) for i in (0, 2, 4))
        # Darken rgb
        r, g, b = int(r * factor), int(g * factor), int(b * factor)
        # rgb -> hex
        return f"{r:02x}{g:02x}{b:02x}"
    
    def get_colors(self):
        color_mode = self.color
        color_gradient = self.get_gradient_color(color_mode)
        color_alpha = self.get_alpha_color()
        return f"{color_mode}{color_alpha}", f"{color_gradient}"
    
        
    def show_indicator(self):
        self.canvas = Canvas.from_rect(Rect(0, 0, 0, 0))
        self.canvas.register("draw", on_draw)


    def hide_indicator(self):
        self.canvas.unregister("draw", on_draw)
        self.canvas.close()
        self.canvas = None

    def move_indicator(self):
        screen: Screen = ui.main_screen()
        rect = screen.rect
        radius = self.radius * screen.scale / 2

        x = rect.left + min(
            max(self.x * rect.width - radius, 0),
            rect.width - 2 * radius,
        )

        y = rect.top + min(
            max(self.y * rect.height - radius, 0),
            rect.height - 2 * radius,
        )

        side = 2 * radius
        self.canvas.move(x, y)
        self.canvas.resize(side, side)


def getHotSpots() -> list[Hotspot]:
    return hotspot_list

def makeHotspotList() -> list[Hotspot]:
    return [Hotspot("x 1 y 0 radius 20 color 808080 alpha 0.9 gradient 0.9")]

hotspot_list = makeHotspotList()
print(hotspot_list)

setting_paths = {
    s.path
    for s in [
        hotspot_show,
        hotspot1
    ]
}



def on_draw(canvas: Canvas):

    c: SkiaCanvas = canvas

    # TODO fix
    global hotspot_list
    hotspot = hotspot_list[0]

    color_mode, color_gradient = hotspot.get_colors()
    x, y = c.rect.center.x, c.rect.center.y
    radius = c.rect.height / 2 - 2

    c.paint.shader = skia.Shader.radial_gradient(
        (x, y), radius, [color_mode, color_gradient]
    )

    c.paint.imagefilter = ImageFilter.drop_shadow(1, 1, 1, 1, color_gradient)

    c.paint.style = c.paint.Style.FILL
    c.paint.color = color_mode
    c.draw_circle(x, y, radius)



def update_hotspots():
    global hotspot_list

    for hotspot in hotspot_list:
        canvas = hotspot.canvas

        print(type(canvas))
        if hotspot_show.get():
            if not canvas or canvas is None:
                print("running with", type(canvas))
                hotspot.show_indicator()
            move_indicator(hotspot)
            
            canvas.freeze()
        elif canvas:
            hide_indicator(hotspot)



def on_update_settings(updated_settings: set[str]):
    if setting_paths & updated_settings:
        global hotspot_list
        update_hotspots(hotspot_list)

def on_ready():
    update_hotspots()   
    registry.register("update_settings", on_update_settings)
    ui.register("screen_change", lambda _: update_hotspots)


app.register("ready", on_ready)

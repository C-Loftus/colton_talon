import json
from types import NoneType
from typing import assert_never

from talon import Context, Module, actions, app, registry, settings, skia, ui
from talon.canvas import Canvas
from talon.screen import Screen
from talon.skia.canvas import Canvas as SkiaCanvas
from talon.skia.imagefilter import ImageFilter
from talon.types import Rect

mod = Module()
ctx = Context()

hotspot_enabled = mod.setting(
    "hotspot_enabled",
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
    _uniqueID: int = 1

    def __init__(self, rawConfigStr: str):
        self._uniqueID = Hotspot._uniqueID
        Hotspot._uniqueID += 1

        assert rawConfigStr is not None

        conf = {}
        split = rawConfigStr.split(" ")
        # convert groups of 2 to key value pairs
        for i in range(0, len(split), 2):
            conf[split[i]] = split[i + 1]

        self.x = float(conf["x"])
        self.y = float(conf["y"])
        self.diameter = float(conf["diameter"])
        self.color = str(conf["color"])
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
        self.canvas.register("draw", on_draw_wrapper(self.canvas, self))

    def hide_indicator(self):
        self.canvas.unregister("draw", on_draw_wrapper(self.canvas, self))
        self.canvas.close()
        self.canvas = None

    # by default the coordinates are a percentage of the screen.
    # this function converts them to pixel coordinates
    def _getPlottingCoords(self):
        screen: Screen = ui.main_screen()
        rect = screen.rect
        radius = self.diameter * screen.scale / 2

        x = rect.left + min(
            max(self.x * rect.width - radius, 0),
            rect.width - 2 * radius,
        )

        y = rect.top + min(
            max(self.y * rect.height - radius, 0),
            rect.height - 2 * radius,
        )
        return (x, y, radius)

    def move_indicator(self):
        x, y, radius = self._getPlottingCoords()

        side = 2 * radius
        self.canvas.move(x, y)
        self.canvas.resize(side, side)

    def cursorInside(self) -> bool:
        cursor_y = actions.mouse_y()
        cursor_x = actions.mouse_x()

        x_coord_from_percentage, y_coord_from_percentage, radius = (
            self._getPlottingCoords()
        )

        # check if the cursor is in any of the hotspots. each hotspot has a x and y coordinate as well as a radius. they are all circles
        INSIDE_X = (
            x_coord_from_percentage - radius
            <= cursor_x
            <= x_coord_from_percentage + radius
        )
        INSIDE_Y = (
            y_coord_from_percentage - radius
            <= cursor_y
            <= y_coord_from_percentage + radius
        )

        if INSIDE_X and INSIDE_Y:
            print("cursor is inside")
            return True
        return False

    def get_unique_id(self) -> int:
        return self._uniqueID

    def run_associated_action(self):
        functionName = f"actions.user.hotspot_{self.get_unique_id()}_focus"
        # run a python function from a string. eval is ok here because the string is not user input
        eval(functionName)()


def getHotSpots() -> list[Hotspot]:
    return hotspot_list


def makeHotspotList() -> list[Hotspot]:
    return [
        Hotspot("x 1 y 0 diameter 20 color 808280 alpha 0.9 gradient 0.9"),
        Hotspot("x 0 y 01 diameter 50 color 899841 alpha 0.9 gradient 0.9"),
        Hotspot("x 0.5 y 0.5 diameter 50 color 893880 alpha 0.4 gradient 0.9"),
    ]


hotspot_list = makeHotspotList()


def on_draw_wrapper(c: SkiaCanvas, current_hotspot: Hotspot):

    def on_draw(c: SkiaCanvas):

        color_mode, color_gradient = current_hotspot.get_colors()
        x, y = c.rect.center.x, c.rect.center.y
        radius = c.rect.height / 2 - 2
        c.paint.shader = skia.Shader.radial_gradient(
            (x, y), radius, [color_mode, color_gradient]
        )
        c.paint.imagefilter = ImageFilter.drop_shadow(1, 1, 1, 1, color_gradient)
        c.paint.style = c.paint.Style.FILL
        c.paint.color = color_mode
        c.draw_circle(x, y, radius)

    return on_draw


def getHotspotIfFocused():
    hotSpots = getHotSpots()

    for hotSpot in hotSpots:
        if hotSpot.cursorInside():
            return hotSpot
    return None


def update_hotspots():
    global hotspot_list

    for hotspot in hotspot_list:
        canvas = hotspot.canvas

        if hotspot_enabled.get():
            if not canvas or canvas is None:
                hotspot.show_indicator()
                assert (
                    hotspot.canvas is not None and type(hotspot.canvas) is not NoneType
                )

            hotspot.move_indicator()
            hotspot.canvas.freeze()
        elif canvas:
            hotspot.hide_indicator()


def on_update_settings(updated_settings: set[str]):
    if {hotspot_enabled.path} & updated_settings:
        update_hotspots()


def on_ready():
    update_hotspots()
    registry.register("update_settings", on_update_settings)
    ui.register("screen_change", lambda _: update_hotspots)


app.register("ready", on_ready)

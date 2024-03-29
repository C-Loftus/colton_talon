The code in this folder relates to eyetrackers. `stare_main.py` can be used to automatically call an action depending on the placement of the cursor. This is particularly useful in older 2d video games with movement on a grid. For instance, if the cursor is in the left half of the screen, the left arrow key can be pressed.

`hotspots.py` is a script that allows you to define a set of hotspots on the screen. When the cursor is in a hotspot and held there for a specific amount of time, an action can be called. This is useful not just for games, but also for any other application where you don't want to use either your voice or your hands to call an action. For instance, you can define a hotspot on the screen that, when you look at it for 2 seconds, will open a new tab in your browser.

```
The quadrants are defined on a monitor as follows:
            +------------+
            |\          /|
            | \        / |
            |  \  up  /  |
            |   \    /   |
            |left+--right|
            |   /   \    |
            |  /     \   |
            | / down  \  |
            |/         \ |
            +------------+
```

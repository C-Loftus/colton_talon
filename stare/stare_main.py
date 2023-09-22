from .stare_by_quadrant import ScreenQuadrant, getQuadrant, runQuadrantAction
from .hotspot import getHotSpots, getHotspotIfFocused
from .stare_actions import APP_NAMES
from talon import ui, actions, cron, settings
import time


tracker_job = None
CRON_INTERVAL = "500ms"


def on_app_switch(application):
    global tracker_job
    if application.name == "Visual Studio Code":
        cron.cancel(tracker_job)
        return

    if application.name in APP_NAMES or settings.get("user.stare_debug"):
        print(f'Starting cron interval at {CRON_INTERVAL}')
        tracker_job = cron.interval(CRON_INTERVAL, handleCursorLocation)
    else:
        cron.cancel(tracker_job)
    
# when there is a change in the active app, check if it is one of the apps we want 
ui.register("app_activate", on_app_switch)



def handleCursorLocation():

    hotspot = getHotspotIfFocused()
    if hotspot is not None:
        if sufficient_threshold(hotspot.get_unique_id()):
            hotspot.run_associated_action()
    
    global focusedQuadrant
    focusedQuadrant = getQuadrant()


    if settings.get("user.stare_debug") and int(time.time()) % 5 == 0:
        print(f'{actions.mouse_y()=},{actions.mouse_x()=}')
        print(f'{focusedQuadrant=}')


    #  don't call an action unless it has been hovered for a  signif andicant threshold
    if sufficient_threshold(focusedQuadrant) and settings.get("user.stare_by_quadrant_enabled"): 
        runQuadrantAction(focusedQuadrant)


ids = [hotspot.get_unique_id() for hotspot in getHotSpots()]
stare_map = {}
stare_map.update({id:0 for id in ids})
stare_map.update({quadrant:0 for quadrant in ScreenQuadrant})


def sufficient_threshold(focusedLocation) -> bool:
    
    # remove the "ms" unit from the cron interval
    to_int = lambda cron_fmt: int(cron_fmt[:-2])
  
    stare_map[focusedLocation]+= to_int(CRON_INTERVAL)

    for location in stare_map:
        if location != focusedLocation:
            stare_map[location]=0

    if stare_map[focusedLocation] >= to_int(settings.get("user.thresholdToTriggerStare")):
        return True
    else:
        return False




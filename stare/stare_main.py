from .stare_by_quadrant import ScreenQuadrant, getQuadrant, runQuadrantAction
from .hotspot import getHotSpots, getHotspotIfFocused
from .stare_actions import APP_NAMES
from talon import ui, actions, cron, settings
import time


tracker_job = None
CRON_INTERVAL = "500ms"
stare_map = {}


def on_app_switch(application):
    global tracker_job

    something_enabled = settings.get("user.stare_debug") \
        or settings.get("user.stare_by_quadrant_enabled") \
        or settings.get("user.hotspot_enabled")
    

    if  (not tracker_job and something_enabled):

        print(f'Starting cron interval at {CRON_INTERVAL}')
        tracker_job = cron.interval(CRON_INTERVAL, handleCursorLocation)

        global stare_map
        ids = [hotspot.get_unique_id() for hotspot in getHotSpots()]
        stare_map.update({id:0 for id in ids})
        stare_map.update({quadrant:0 for quadrant in ScreenQuadrant})
        print(ids)

    elif (not something_enabled and tracker_job):
        try:
            print(f'Canceling cron interval for staring/hotspots')
            cron.cancel(tracker_job)
        except:
            print('cron job not found for staring/hotspots')
    
# when there is a change in the active app, check if it is one of the apps we want 
ui.register("app_activate", on_app_switch)



def handleCursorLocation():

    hotspot = getHotspotIfFocused()
    if hotspot is not None and settings.get("user.hotspot_enabled"):
        if sufficient_threshold(hotspot.get_unique_id()):
            hotspot.run_associated_action()
        else: 
            if settings.get("user.stare_debug"):
                print('not long enough')
            
    else:
        if settings.get("user.stare_debug"):
            print(f'{hotspot=}, {settings.get("user.hotspot_enabled")=}')
            print('not valid setting' )

    
    global focusedQuadrant
    focusedQuadrant = getQuadrant()


    if settings.get("user.stare_debug") and int(time.time()) % 5 == 0:
        print(f'{actions.mouse_y()=},{actions.mouse_x()=}')
        print(f'{focusedQuadrant=}')


    #  don't call an action unless it has been hovered for a  signif andicant threshold
    if settings.get("user.stare_by_quadrant_enabled"):
        # this needs to be nested given the fact that the threshold updates the map 
        # and resets it to zero if it isn't focused
        if sufficient_threshold(focusedQuadrant):
            runQuadrantAction(focusedQuadrant)




def sufficient_threshold(focusedLocation) -> bool:
    global stare_map
    
    # remove the "ms" unit from the cron interval
    to_int = lambda cron_fmt: int(cron_fmt[:-2])
  
    stare_map[focusedLocation]+= to_int(CRON_INTERVAL)

    for location in stare_map:
        if location != focusedLocation:
            stare_map[location]=0

    if stare_map[focusedLocation] >= to_int(settings.get("user.thresholdToTriggerStare")):
        return True
    else:
        print(stare_map)
        return False




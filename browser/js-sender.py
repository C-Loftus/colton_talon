from talon import Module, Context, actions, app, clip
import os, time, subprocess
from typing import NewType

ctx = Context()
mod = Module()

# Get the current working directory
script_directory = os.path.dirname(os.path.abspath(__file__))

NaturalLanguageName = NewType('NaturalLanguageName', str)
RawJSFileName = NewType('RawJSFileName', str)
javascript_file_names: dict[NaturalLanguageName, RawJSFileName] = {}

def build_capture_list():
    '''
    Builds a mapping between spoken text and js file names.
    Files should be named with snakecase and be easy to dictate
    i.e. `console_log_test.js` would be dictated as "console log test" 
    '''
    global javascript_file_names
    # Specify the path to the 'build/' directory
    build_directory = os.path.join(script_directory, 'build')
    
    # Check if the 'build/' directory exists
    if os.path.exists(build_directory) and os.path.isdir(build_directory):
        file_names = os.listdir(build_directory)
        
        for file_name in file_names:
            try:
                if not file_name.endswith(".js"):
                    continue
                else:
                    pretty_name = file_name.replace(".js", "")
                pretty_name = pretty_name.replace("_", " ") if "_" in pretty_name else pretty_name
                javascript_file_names[pretty_name] = file_name
            except :
                #  should never trigger given the fact that the file name is auto generated from webpack
                print(f'{file_name} triggered an exception when parsing')
    else:
        print("The 'build/' directory does not exist.")

build_capture_list()


mod.list("talon_JS_Functions", desc="All the local javascript functions that can be sent to the browser")
ctx.lists["user.talon_JS_Functions"] = javascript_file_names

@mod.capture(rule="{user.talon_JS_Functions}")
def talon_JS_Functions(functionName: str) -> str:
    "Convert spoken text to the proper filename"
    return functionName.talon_JS_Functions


#  reads in the raw text from a javascript source file
def fn_contents(js_build_file: str) -> str:
    relative_path = os.path.join(script_directory, 'build',js_build_file)
    with open(relative_path, 'r') as file:
        data = file.read()
        return data

@mod.action_class
class Actions:
    def send_js(funct: str):
        '''copy JS to clipboard and send to browser'''
        with clip.revert():
            raw_text=fn_contents(funct) 
            clip.set_text(raw_text)
            actions.key("ctrl-shift-i")
            time.sleep(0.5)
            actions.user.paste(clip.text())
            actions.key("enter")
            time.sleep(1)
            actions.key("ctrl-shift-i")

    def build_js():
        """build typescript to raw js for browser execution"""
        # path of this file
        print("Compiling JS...")
        this_file_path = os.path.dirname(os.path.abspath(__file__))
        subprocess.run(f'npm run build --prefix {this_file_path}', shell=True)
from talon import Module, Context, actions, app, clip,fs
import os, time, subprocess, shutil
from typing import NewType

ctx = Context()
mod = Module()

# Get the current working directory
script_directory = os.path.dirname(os.path.abspath(__file__))

NaturalLanguageName = NewType('NaturalLanguageName', str)
RawJSFileName = NewType('RawJSFileName', str)
javascript_file_names: dict[NaturalLanguageName, RawJSFileName] = {}
build_directory = os.path.join(script_directory, 'build')
src_directory = os.path.join(script_directory, 'src')


def copyJSToBuild():
    # copy all raw js files to the build directory
    print("Copying JS files to build directory")
    for file in os.listdir(src_directory):
        if file.endswith(".js"):
            shutil.copy(os.path.join(src_directory, file), build_directory)

def build_capture_list(path: str= None, flags: int= None ):
    '''
    Builds a mapping between spoken text and js file names.
    Files should be named with snakecase and be easy to dictate
    i.e. `console_log_test.js` would be dictated as "console log test" 
    '''
    print("Building JS file name list")
    copyJSToBuild()
    global javascript_file_names
    
    if os.path.exists(build_directory) and os.path.isdir(build_directory):
        file_names = os.listdir(build_directory)
        
        for file_name in file_names:
            try:
                if not file_name.endswith(".js"):
                    continue
                
                naturalLangName = file_name.replace(".js", "")
                naturalLangName = naturalLangName.replace("_", " ") if "_" in naturalLangName else naturalLangName
                javascript_file_names[naturalLangName] = file_name
            except :
                #  should never trigger given the fact that the file name is auto generated from webpack
                print(f'{file_name} triggered an exception when parsing')
    else:
        print("The 'build/' directory does not exist.")

build_capture_list()
fs.watch(str(src_directory), build_capture_list)


mod.list("talon_JS_Functions", desc="All the local javascript functions that can be sent to the browser")
ctx.lists["user.talon_JS_Functions"] = javascript_file_names


@mod.capture(rule="{user.talon_JS_Functions}")
def talon_JS_Functions(functionName: str) -> str:
    "Convert spoken text to the proper filename"
    return functionName.talon_JS_Functions


#  reads in the raw text from a javascript source file
def fn_contents(js_build_file: str) -> str:
    relative_path = os.path.join(build_directory, js_build_file)
    with open(relative_path, 'r') as file:
        return file.read()

@mod.action_class
class Actions:
    def copy_js(funct: str):
        '''copy JS to clipboard and send to browser'''
        raw_text=fn_contents(funct) 
        clip.set_text(raw_text)


    def build_js():
        """build typescript to raw js for browser execution"""
        print("Compiling TS...")

        # remove all js files from the build directory
        build_directory = os.path.join(script_directory, 'build')
        if os.path.exists(build_directory) and os.path.isdir(build_directory):
            file_names = os.listdir(build_directory)
            for file_name in file_names:
                if file_name.endswith(".js"):
                    os.remove(os.path.join(build_directory, file_name))

        npm_path = os.path.dirname(os.path.abspath(__file__))
        subprocess.run(f'npm run build --prefix {npm_path}', shell=True)
        # block until the build folder contains the js files

        total_time = 0
        while len(os.listdir(build_directory)) < len(javascript_file_names):
            time.sleep(0.5)
            total_time += 0.5
            if total_time > 30:
                actions.user.notify("Build timed out")
                return
        
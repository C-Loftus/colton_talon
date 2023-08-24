
from typing import Union
import json
import re
from os.path import expanduser
from pathlib import Path

from talon import Context, Module, actions, app, clip
from typing import Any

mod = Module()

@mod.action_class
class Actions:

    def remove_spaces(string: str): 
        """"Removes Spaces from String"""
        if string.endswith("\n"):
            print("YES")

        return string.replace(" ", "")
    


    def change_setting(setting_name: str, setting_value: Union[str, int, bool]):
        """
        Changes a VSCode setting by name
        Args:
            setting_name (str): The name of the setting
            setting_value (any): The new value.  Will be JSON encoded
        """

        if type(setting_value) == str and (setting_value == 'true' or setting_value == 'false'):
            setting_value=bool(setting_value)


        original_settings_path = Path(
            expanduser("~/.config/Code/User/settings.json")
        )
        original_settings = original_settings_path.read_text()
        regex = re.compile(rf'^(\s*)"{setting_name}": .*[^,](,?)$', re.MULTILINE)
        new_settings = regex.sub(
            rf'\1"{setting_name}": {json.dumps(setting_value)}\2', original_settings
        )
        original_settings_path.write_text(new_settings)

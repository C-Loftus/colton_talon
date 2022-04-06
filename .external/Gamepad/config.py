import yaml
import os
from talon import app

APP_PATH = "config.yaml"
HARDWARE_PATH = "hardware_mappings.yaml"

class application_config:
    
    def __init__(self):
        ROOT_DIR = os.path.realpath(os.path.dirname(__file__))
        self.app_path = os.path.join(ROOT_DIR, APP_PATH)
        self.hardware_path = os.path.join(ROOT_DIR, HARDWARE_PATH)
        
        self._load_config()
        
        try:
            self.modifier = self.config["MODIFIER"]
            # print("Modifier: {}".format(self.modifier))
        except KeyError:
            # pymsgbox.alert(text="Config loaded but no Modifier Found. Using one tap mode", 
            #      title="Step-Hotkey", timeout=2000)
            pass


    def _load_config(self):
        with open(self.app_path) as file:
            try:
                self.config = yaml.safe_load(file)
            except yaml.YAMLError as exc:
                raise Exception("Error loading config file at {}".format(self.app_path))
        with open(self.hardware_path) as file:
            try:
                self.hardware = yaml.safe_load(file)
            except yaml.YAMLError as exc:
                raise Exception("Error loading hardware config file at {}".format(self.hardware_path))

    def get_config(self):
        return self.config
    def get_hardware_config(self):
        return self.hardware

    def get_hardware_list(self, gamepad):
        return {k:v for x in self.hardware[gamepad] for k,v in x.items()}

    def print_config(self):
        for os_key in self.config:
            print(os_key, self.config[os_key])
    def print_hardware(self):
        for device in self.hardware:
            print(device)

    def pad_listed(self, pad_name) -> bool:
        if pad_name in self.hardware:
            return True
        raise Exception("Pad \"{}\" not found in hardware config file".format(pad_name))

    def os_key_listed(self, os_key, gamepad) -> bool:
        key_list = self.get_hardware_list(gamepad)

        if os_key in key_list:
            return True
        raise Exception("os key {} not found in hardware config file".format(os_key))

    def dancepad_button_mapped(self, button) -> bool:
        for b in self.config:
            if button == str(b):
                return True
        app.notify(body=f'Button {button} not mapped in config file')

        return False

    def os_key_to_action(self, os_key):
        try:
            return self.config[os_key]
        except KeyError:
            raise Exception("os_key {} not found in config file".format(os_key))

    def decode_step(self, gamepad, os_key, modifierActivated=False):
        if self.pad_listed(gamepad) and self.os_key_listed(os_key, gamepad):
            dancepad_button = self.get_hardware_list(gamepad)[os_key]

            if self.dancepad_button_mapped(dancepad_button):
                return self.os_key_to_action(dancepad_button)
    
if __name__ == "__main__":
    conf = application_config()
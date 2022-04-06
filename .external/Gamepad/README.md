# step-hotkey
### About
 The purpose of this repository is to provide a solution for controlling one's computer while working at a standing desk or a desk with enough leg room. This program can be used to program  key presses of dance pads to hot keys, talon voice commands, or shell commands. If you have a disability affecting the use of your hands or a repetitive strain injury, this program can allow you to bind otherwise long commands or key presses to  a press of a button.

This program can be ran on Linux Mac OS or Windows.

 ### Usage
 Clone the repository. Make sure that your dancepad is plugged in.  make sure that  your dance pad is listed within the [hardware mappings](./hardware_mappings.yaml) file

 Pads that are supported:
(others should work, you will just need to check the mappings and put them in the [hardware mappings](./hardware_mappings.yaml) file):
* https://www.amazon.com/dp/B00FJ2KTXC/ref=cm_sw_r_cp_apa_fabc_QCHMCW0ADDK3W96GBF7X
 
To install
```bash
pip install -r requirements.txt
```

 To run
 ```bash
python3 main.py
 ```

  ### Assist Me
   Different dance pads will have different output from different keys. If  you don't have one of the supported dance pads you want to help, run the script to find  the names of the key outputs on your device.

```bash
python3 map_my_dancepad.py
```
 while the script is running, press each key on the pad and the script will print out its name.
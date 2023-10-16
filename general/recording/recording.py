from talon import Module, actions
import subprocess
import datetime
import os
import pathlib

# Global variable to store the FFmpeg subprocess
ffmpeg_process = None
output_file = None  # Store the output file name

mod = Module()


import subprocess
import shlex
import time

# class FFmpegWrapper:
#     def __init__(self, output_file):
#         self.output_file = output_file
#         self.process = None

#     def start_recording(self):
#         if self.process:
#             print("Recording is already in progress.")
#             return

#         # command = f"ffmpeg -f x11grab -s 1920x1080 -i :0.0 -f alsa -i default {self.output_file}"
#         # command = f'ffmpeg -f gdigrab -framerate 30 -i desktop -f dshow -i audio="Integrated Camera" {self.output_file}'
#         command = 'ffmpeg -f gdigrab -framerate 0 -i -ac 2 desktop test.mp4'

#         args = shlex.split(command)
        
#         try:
#             self.process = subprocess.Popen(args)
#             print("Recording started...")
#         except Exception as e:
#             print(f"Error starting recording: {e}")
#             self.process.kill()

#     def stop_recording(self):
#         if self.process:
#             self.process.terminate()
#             self.process.wait()
#             self.process = None
#             print("Recording stopped.")
#             # print save location
#             print(f"Saved to: {self.output_file}")
#         else:
#             print("No active recording to stop.")

# recorder = FFmpegWrapper(output_file)
    

@mod.action_class
class Actions:

    # def start_ffmpeg():
    #     """start"""
    #     recorder.start_recording()
        

    # def stop_ffmpeg():
    #     """stop"""
    #     recorder.stop_recording()


    def start_recording():
        """Start recording"""
        actions.key("alt-f9:down")
        actions.sleep("100ms")
        actions.key("alt-f9:up")

    def stop_recording():
        """Stop recording"""
        actions.key("alt-f10:down")
        actions.sleep("100ms")
        actions.key("alt-f10:up")
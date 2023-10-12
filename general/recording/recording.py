from talon import Module, actions
import subprocess
import datetime
import os
import pathlib

# Global variable to store the FFmpeg subprocess
ffmpeg_process = None
output_file = None  # Store the output file name

mod = Module()

@mod.action_class
class Actions:

    def start_ffmpeg():
        """start"""
        global ffmpeg_process
        global output_file

        if ffmpeg_process is not None and ffmpeg_process.poll() is None:
            print("FFmpeg is already running.")
            return

        # Get the current time to use as the output file name
        current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        output_file = f"ffmpeg_record_{current_time}.mp4"

        # Construct the FFmpeg command with default microphone
        command = [
            'ffmpeg',
            '-f', 'gdigrab',
            '-framerate', '30',
            '-offset_x', '0',
            '-offset_y', '0',
            '-video_size', '1920x1080',  # Adjust the screen size as needed
            '-i', 'desktop',
            '-f', 'dshow',
            '-i', 'audio="Microphone (Your Default Audio Device)"',  # Use the default microphone
            output_file
        ]

        # Start FFmpeg as a subprocess and capture stdout and stderr
        ffmpeg_process = subprocess.Popen(command, stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)

        print("FFmpeg started.")
        # get the full path of the output file
        path = pathlib.Path(output_file)
        full_path = os.path.abspath(path)
        print(f"Output file: {full_path}")

    def stop_ffmpeg():
        """stop"""
        global ffmpeg_process
        global output_file

        if ffmpeg_process is not None:
            try:
                # Terminate the FFmpeg process
                ffmpeg_process.terminate()
                ffmpeg_process.wait()
                print("FFmpeg stopped.")

                # Clear the process and reset the output file
                ffmpeg_process = None
                output_file = None

            except subprocess.TimeoutExpired:
                print("FFmpeg process did not stop gracefully.")
        else:
            print("FFmpeg is not running.")

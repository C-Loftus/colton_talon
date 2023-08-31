from talon import Module, clip, actions, ui, skia
import subprocess, os
import urllib.request
from typing import Optional
from pathlib import Path
from pathlib import Path
import time, io

mod = Module()
@mod.action_class
class Actions:

    def test_clip():
        """test clipboard"""
        path = 'C:\\Users\\cloftus\\tmp\\trimmed.png'
        with open(path, "rb") as image:
            f = image.read()
            b = bytearray(f)
            clip.set_image(b)

    # Must have ghost script and image magick installed
    def extract_PDF_page(url: str, page_number: int, file_description: str):
        # https://jdhao.github.io/2019/11/20/convert_pdf_to_image_imagemagick/
        """converts pdf page to an iamge"""
        file_description="_".join(file_description.split())

        filename= os.path.join(Path.home(), 
                               "tmp",
                               "download.pdf")
        
        if not os.path.exists(filename):
            urllib.request.urlretrieve(url, filename)

        output_filename =  os.path.join(Path.home(), "tmp", f'page-{page_number}_{file_description}.png')

        command = [
            'C:\\Users\\cloftus\\scoop\\apps\\imagemagick\\7.1.1-15\\magick.exe', 
                "convert",
                "-density",
                "300",
                f'{str(filename)}[{page_number - 1}]',
                "-quality",
                "100", 
                "-background",
                "white",
                "-alpha", "remove",
                "-alpha", 
                "off",
                output_filename
            ]

        # assert command == ['magick.exe', 'convert', '-density', '300', 'C:\\Users\\cloftus\\tmp\\download2.pdf[1]', '-quality', '100', 'C:\\Users\\cloftus\\tmp\\trimmed.png']

        p = subprocess.run(command)
        # time.sleep(2)

        # # Convert image to bytes
        # image_bytes = io.BytesIO()
        clip.set_image(skia.Image.from_file(output_filename))



def on_app_switch(application):
    if "XamlAction" in application.name:
        actions.insert("This is a bug in Delinea caused by a misrecognition of Talon. This is auto dismissed")
        time.sleep(.5)
        actions.key("tab")
        actions.key("enter")
        actions.key("enter")

ui.register("app_activate", on_app_switch)
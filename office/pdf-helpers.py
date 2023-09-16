from talon import clip, actions, ui, skia
import subprocess, os
import urllib.request
from pathlib import Path
import time
from talon import Module, actions

# not in PATH var so we need the absolute path
IMAGE_MAGICK_PATH = 'C:\\Users\\cloftus\\scoop\\apps\\imagemagick\\7.1.1-15\\magick.exe'

mod = Module()
@mod.action_class
class Actions:

    # Must have ghost script and image magick installed
    def extract_PDF_page(url: str, page_number: int, file_description: str):
        """converts pdf page to an iamge"""
        # https://jdhao.github.io/2019/11/20/convert_pdf_to_image_imagemagick/
        file_description="_".join(file_description.split())

        filename= os.path.join(Path.home(), 
                               "tmp",
                               "download.pdf")
        
        if not os.path.exists(filename):
            urllib.request.urlretrieve(url, filename)

        output_filename =  os.path.join(Path.home(), "tmp", f'page-{page_number}_{file_description}.png')

        # Convert PDF to image and remove any sort of transparency
        command = [IMAGE_MAGICK_PATH, 
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

        subprocess.run(command)

        clip.set_image(skia.Image.from_file(output_filename))


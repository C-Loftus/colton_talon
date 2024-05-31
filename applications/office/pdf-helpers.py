import os
import subprocess
import time
import urllib.request
from pathlib import Path

from talon import Module, actions, clip, skia, ui

# not in PATH var so we need the absolute path
IMAGE_MAGICK_PATH = "C:\\Users\\cloftus\\scoop\\apps\\imagemagick\\7.1.1-15\\magick.exe"

mod = Module()


@mod.action_class
class Actions:

    # Must have ghost script and image magick installed
    def extract_PDF_page(url: str, page_number: int, file_description: str):
        """converts pdf page to an iamge"""
        # https://jdhao.github.io/2019/11/20/convert_pdf_to_image_imagemagick/
        file_description = "_".join(file_description.split())

        # todays date
        today = time.strftime("%Y-%m-%d", time.gmtime())

        filename = os.path.join(Path.home(), "tmp", f"{today}-download.pdf")

        try:
            if not os.path.exists(filename):
                urllib.request.urlretrieve(url, filename)
        except Exception as e:
            actions.user.notify(e)
            return

        output_filename = os.path.join(
            Path.home(), "tmp", f"page-{page_number}_{file_description}.png"
        )

        # Convert PDF to image and remove any sort of transparency
        command = [
            IMAGE_MAGICK_PATH,
            "convert",
            "-density",
            "300",
            f"{str(filename)}[{page_number - 1}]",
            "-quality",
            "100",
            "-background",
            "white",
            "-alpha",
            "remove",
            "-alpha",
            "off",
            output_filename,
        ]

        subprocess.run(command)

        clip.set_image(skia.Image.from_file(output_filename))

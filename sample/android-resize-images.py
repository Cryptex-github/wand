#!/usr/bin/env python

# Python MagickWand bindings can be obtained
# from https://github.com/emcconville/wand
from wand.image import Image

import os
import re

# Android - Supporting multiple screens
# http://developer.android.com/guide/practices/screens_support.html

MANIFEST = (
    # dpi, ratio
    ('h', .75),  # high-dpi
    ('m', .5),  # medium-dpi
    ('l', .375)  # low-dpi
)

if __name__ == "__main__":
    # We start from here (2.0x size images)
    files = os.listdir("res/drawable-xhdpi/")

    # Filter out non-desired files
    files = filter(lambda x: re.match(r"^\w+(.jpg|.png)$", x) is not None,
                   files)

    for filename in files:
        with Image(filename=f"res/drawable-xhdpi/{filename}") as img:

            print(f"Resizing {filename}...")

            width, height = img.size

            for dpi, ratio in MANIFEST:
                cimg = img.clone()
                cimg.resize(int(width * ratio), int(height * ratio))
                cimg.save(filename=f"res/drawable-{dpi}dpi/{filename}")

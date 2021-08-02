import io
import os
from google.cloud import vision


def load(path):
    file_name = os.path.abspath(path)

    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    return vision.Image(content=content)


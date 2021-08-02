import io
import os
from lib import image_loader
from google.cloud import vision

FEATURES = [
    vision.Feature(type_=vision.Feature.Type.LABEL_DETECTION),
    vision.Feature(type_=vision.Feature.Type.TEXT_DETECTION),
    vision.Feature(type_=vision.Feature.Type.IMAGE_PROPERTIES),
]

client = vision.ImageAnnotatorClient()


def label_image(path):
    image = image_loader.load(path)

    response = client.label_detection(image=image)

    return response.label_annotations


def annotate_image(path):
    image = image_loader.load(path)
    return client.annotate_image(vision.AnnotateImageRequest(image=image, features=FEATURES))


def annotate_images(paths):
    requests = list(map(__to_request, paths))
    response = client.batch_annotate_images(requests=requests)

    return list(zip(paths, response.responses))


def __to_request(path):
    image = image_loader.load(path)
    return vision.AnnotateImageRequest(image=image, features=FEATURES)
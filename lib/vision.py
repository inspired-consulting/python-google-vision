import io
import os
from lib import image_loader
from google.cloud import vision

FEATURES = [
    vision.Feature(type_=vision.Feature.Type.LABEL_DETECTION),
    vision.Feature(type_=vision.Feature.Type.TEXT_DETECTION),
    vision.Feature(type_=vision.Feature.Type.IMAGE_PROPERTIES),
]

CHUNK_SIZE = 10

client = vision.ImageAnnotatorClient()


def label_image(path):
    image = image_loader.load(path)

    response = client.label_detection(image=image)

    return response.label_annotations


def annotate_image(path):
    image = image_loader.load(path)
    return client.annotate_image(vision.AnnotateImageRequest(image=image, features=FEATURES))


def annotate_images(paths):

    chunks = chunk(paths, CHUNK_SIZE)

    annotations = []

    for c in chunks:
        requests = list(map(__to_request, c))
        response = client.batch_annotate_images(requests=requests)
        annotations.extend(response.responses)

    return list(zip(paths, annotations))


def chunk(full_list, chunk_size):
    return [full_list[i:i + chunk_size] for i in range(0, len(full_list), chunk_size)]


def __to_request(path):
    image = image_loader.load(path)
    return vision.AnnotateImageRequest(image=image, features=FEATURES)
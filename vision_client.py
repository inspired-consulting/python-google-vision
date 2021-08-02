from lib import vision
from pathlib import Path


def process(files):
    annotations = vision.annotate_images(files)

    for ia in annotations:
        path, annotation = ia
        labels = [anno.description for anno in annotation.label_annotations]
        print(f"{path.name} : {labels}")


def image_files_in_dir(dir, max=100):
    all_images = [f for f in Path(dir).iterdir() if f.is_file()]
    return all_images[:max]


if __name__ == '__main__':
    images_files = image_files_in_dir('./images/indoor/clear/', 10)
    process(images_files)





from lib import vision
from pathlib import Path
import argparse


def process(files):
    annotations = vision.annotate_images(files)

    for ia in annotations:
        path, annotation = ia
        labels = [anno.description for anno in annotation.label_annotations]
        print(f"{path.name},", ", ".join(labels))


def image_files_in_dir(dir, max=100):
    all_images = [f for f in Path(dir).iterdir() if f.is_file()]
    return all_images[:max]


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--folder', dest='folder', type=str, required=True, help='The folder containing the images', )
    parser.add_argument('-m', '--max-files', dest='max_files', type=int, required=False, default=100, help='Max number of images')
    args = parser.parse_args()

    images_files = image_files_in_dir(args.folder, args.max_files)
    process(images_files)





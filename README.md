# Python - Google Vision Demo

Demo Google Vision API usage from Python

## Prerequisites

You need:

* Python3
* Google Cloud account
* Virtual env (optional)

## Setup 

Before starting with the Vision API, you have to set up a project 
and authentication: https://cloud.google.com/vision/docs/setup

You need to export the path to your key file as env variable:

    export GOOGLE_APPLICATION_CREDENTIALS="your path"

Afterwards you need to install the required libraries from `requirements.txt`:

    pip install -r requirements.txt

You can download sample image sets from Kaggle, e.g. https://www.kaggle.com/balraj98/synthetic-objective-testing-set-sots-reside

## Execute image annotation

To annotate images in some directory you can execute the `visual_client.py` file:

     python vision_client.py -f images 

You can obtain help about the options using:

     python vision_client.py -h







import requests
import time
import os
import sys
%matplotlib inline
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from PIL import Image
from io import BytesIO

# Add your Computer Vision subscription key and endpoint to your environment variables.
if 'COMPUTER_VISION_SUBSCRIPTION_KEY' in os.environ:
    subscription_key = os.environ['COMPUTER_VISION_SUBSCRIPTION_KEY']
else:
    print("\nSet the COMPUTER_VISION_SUBSCRIPTION_KEY environment variable.\n**Restart your shell or IDE for changes to take effect.**")
    sys.exit()

if 'COMPUTER_VISION_ENDPOINT' in os.environ:
    endpoint = os.environ['COMPUTER_VISION_ENDPOINT']

text_recognition_url = endpoint + "/v2.1/read/core/asyncBatchAnalyze"

image_path = input();
# Read the image into a byte array
image_data = open(image_path, "rb").read()
data=image_data
# Set Content-Type to octet-stream
headers = {'Ocp-Apim-Subscription-Key': subscription_key, 'Content-Type': 'application/octet-stream'}
params = {'language': 'unk', 'detectOrientation': 'true'}
# put the byte array into your post request
response = requests.post(text_recognition_url, headers=headers, params=params, data = image_data)
response.raise_for_status()

# Extracting text requires two API calls: One call to submit the
# image for processing, the other to retrieve the text found in the image.

# Holds the URI used to retrieve the recognized text.
operation_url = response.headers["Operation-Location"]

# The recognized text isn't immediately available, so poll to wait for completion.
analysis = {}
poll = True
while (poll):
    response_final = requests.get(
        response.headers["Operation-Location"], headers=headers)
    analysis = response_final.json()
#     print(analysis)
    time.sleep(1)
    if ("recognitionResults" in analysis):
        poll = False
    if ("status" in analysis and analysis['status'] == 'Failed'):
        poll = False

analysed_text = []
if ("recognitionResults" in analysis):
    # Extract the recognized text, with bounding boxes.
    analysed_text = [(line["boundingBox"], line["text"])
                for line in analysis["recognitionResults"][0]["lines"]]
c=image_path.rfind("\\")
file_name=image_path[:c]
file_name=file_name+"\\"+analysed_text[0][1]+"_"+analysed_text[1][1]+'.txt'
with open(file_name,"a+") as f:
    for i in range(2,len(analysed_text)):
        f.write(analysed_text[i][1]+' ')

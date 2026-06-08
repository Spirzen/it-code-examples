# pip install azure-ai-vision-imageanalysis
import os
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential

endpoint = os.environ["VISION_ENDPOINT"]
key = os.environ["VISION_KEY"]

client = ImageAnalysisClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(key),
)

with open("photo.jpg", "rb") as f:
    result = client.analyze(
        image_data=f.read(),
        visual_features=[
            VisualFeatures.CAPTION,
            VisualFeatures.TAGS,
            VisualFeatures.OBJECTS,
        ],
        language="en",
    )

if result.caption:
    print(result.caption.text)
for tag in (result.tags.list if result.tags else []):
    print(tag.name, tag.confidence)

from importlib.resources import contents
from google.cloud import vision
import os, io

client = vision.ImageAnnotatorClient()
class OCR:
    @staticmethod
    def read_image(path):
        file_name = os.path.abspath(path)

        # Loads the image into memory
        with io.open(file_name, 'rb') as image_file:
            content = image_file.read()
            image = vision.Image(content=content)
            return image

    @staticmethod
    def image_to_string(path):
        image = OCR.read_image(path)

        filtered = []
        try:
            response = client.document_text_detection(image=image)
            full_text = response.full_text_annotation
            clear_data = full_text.text.split('\n')
            for item in clear_data:
                if item.isspace() or len(item) <= 2:
                    continue
                else:
                    filtered.append(item)
        except:
            return None

        return filtered 
        
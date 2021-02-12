from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials
from PIL import ImageGrab
import io
import pyperclip


def recognize_printed_text_in_mac_clipboard_image():
    """RecognizedPrintedTextUsingOCR_API.
    This will do an OCR analysis of the given image.
    """

    endpoint="xxx"
    credentials="xxx"

    client = ComputerVisionClient(endpoint=endpoint, credentials = CognitiveServicesCredentials(credentials))

    img = ImageGrab.grabclipboard()

    # Store the bytes in a byte stream
    with io.BytesIO() as img_bytes:
        img.save(img_bytes, format='PNG')
        img_bytes.seek(0)

        image_analysis = client.recognize_printed_text_in_stream(
            image=img_bytes
        )
        lines = image_analysis.regions[0].lines
        pyperclip.copy("\n".join([(" ".join([word.text for word in line.words])) for line in lines]))

recognize_printed_text_in_mac_clipboard_image()

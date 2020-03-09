try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import pyglet

from selenium import webdriver
browser=webdriver.Firefox()
DB = browser.get('https://tableauserver.suny.edu/t/IRPublic/views/PublicDashboard-ADAChanges/Dashboard?%3Aembed=y&%3AshowVizHome=no&%3Ahost_url=https%3A%2F%2Ftableauserver.suny.edu%2F&%3Aembed_code_version=3&%3Atabs=yes&%3Atoolbar=yes&%3AshowAppBanner=false&%3Adisplay_spinner=no&%3AloadOrderID=0')

DB.image.get


def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    text = pytesseract.image_to_string(Image.open(filename))  # We'll use Pillow's Image class to open the image and
    # Tesseract to detect the string in the image
    return text

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

print(ocr_core('C:\\Users\\Leonardo\\Documents\\tmp\\suny_webscrape\\ocr_sample.png'))

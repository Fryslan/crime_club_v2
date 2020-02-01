
import io
import requests
import pytesseract
from PIL import Image
from skimage import io

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
response = requests.get("https://www.crime-club.nl/images/captcha/captcha.php")
# print( type(response) ) # <class 'requests.models.Response'>
img = Image.open(io.BytesIO(response.content))
basewidth = 500
wpercent = (basewidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((basewidth,hsize), Image.ANTIALIAS)
img.show()
# print( type(img) ) # <class 'PIL.JpegImagePlugin.JpegImageFile'>
print(pytesseract.image_to_data(img))
text = pytesseract.image_to_string(img)
print( text )
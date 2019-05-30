# __author:  Administrator
# __date:  2019/5/29/029

import pytesseract
from PIL import Image

filepath = "C:/Users/Administrator/Desktop/tess.png"
img = Image.open(filepath)
print(pytesseract.image_to_string(img))

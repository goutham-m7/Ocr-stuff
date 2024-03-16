from pdf2image import convert_from_path
import pytesseract as tess
import os
from PIL import Image
file_name="test.pdf"
images = convert_from_path(file_name)
#print(images)
a=0
pages=[]
'''text=tess.image_to_string(Image.open("image1.jpeg"))
pages.append(text)
with open("out2.txt","w") as f:
    f.write("\n".join(pages))'''

for i,image in enumerate(images):
    a=a+1
    filename="image"+str(a)+".jpeg"
    image.save(filename,"JPEG")
    text = tess.image_to_string(Image.open(filename))  
    pages.append(text)  
with open("new.txt","w") as f:
    f.write("\n".join(pages))

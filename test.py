import psutil
from PIL import Image

# open and show image
im = Image.open('myImageFile.jpg')
im.show()



# hide image
for proc in psutil.process_iter():
    if proc.name() == "display":
        proc.kill()
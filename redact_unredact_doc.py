# Part 2 of the unredaction project - revealing the text beneath redacted text

#!/usr/bin/python

from PIL import Image, ImageShow, ImageFilter
import os
import time
import sys


# go to directory where images live
os.chdir('/home/pi/Desktop/images/')

# try to open image and show error if cannot
try:
    image1 = Image.open("a_CIA_IG_Report_REDACT_p15_400x600.jpg")
except IOError:
    print("cannot load image")
    sys.exit(1)

# display image1 - the heavily redacted document    
image1.show()
# code below can be used during testing to check size/mode
#print(image1.format, image1.size, image1.mode)
time.sleep(1)


# try to open 2nd image in backgroundand show error if cannot
try:
    image2 = Image.open("b_CIA_IG_Report_p15_400x600.jpg")
except IOError:
    print("cannot load image")
    sys.exit(1)

# the 2 code lines below can be used during testing to check size/mode
#image2.show()
#print(image2.format, image2.size, image2.mode)

# now use PIL Image.blend to slowly blend the 2 images together
# fade out the redaction to reveal the less-redacted version over 3 steps

newimg1= Image.blend(image1, image2, 0.3)

newimg1.show()
time.sleep(1)

newimg2= Image.blend(image1, image2, 0.7)

newimg2.show()
time.sleep(1)

newimg3= Image.blend(image1, image2, 0.9)

newimg3.show()
time.sleep(1)

# finally show image2, the less-redacted document, fully
# sleep some extra seconds here to allow the user to read what had been hidden

image2.show()
time.sleep(7)

image2.close() #unfortunately this does not close the image window, but it is here in case it helps release memory from this process

# bring the user back to viewing the heavily redacted document
# wait 2 seconds before being available to motion sensor triggers again to start over

image1.show()
time.sleep(2)

image1.close() #unfortunately this does not close the image window, but it is here in case it helps release memory from this process

# sys.exit(1)  # when activated/uncommented attempts to exit active processes

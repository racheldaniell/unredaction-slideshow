# unredaction-slideshow
# UNREDACTION: Behind the Black Box

The basic function of this project is to facilitate the creation of a slideshow of images that will transition when a motion sensor is triggered. 

In the original project, the slideshow is taken from a U.S. government document related to the use of torture by the CIA that has been released in differently redacted versions, so that the slideshow appears to make the redaction disappear through user action, highlighting what we have learned about the CIA's use of abusive techniques over time through pushing for access to government information.
The same code could be used to transition between two images on other themes based on user motion interaction as well.

A Fritzing diagram is included to show the materials and setup required, which includes a Raspberry Pi 3 B+, MicroBit, and two PIR motion sensors.

Code is in Python 3, primarily run on the Raspberry Pi, with a small code piece run on the MicroBit to have it display a scrolled text credit about the redacted document. 

You will also need two image files to transition. The examples used in the original project are included in this repository -- two JPEGs, one is a heavily redacted document page and the other a less-redacted document page. The code is designed to take 2 images and make 3 transitions between them using alpha channel blending, but it can be adjusted for any number of images and any number of blend transitions (just set the alpha value to a different number between 0 and 1 for each transition).

Recommended naming conventions: It is handy to give your image files a prefix such as "a_", "b_" or "1_", "2_" so that you can control their order. It is also useful to number your transitions (in this example, a numeric suffix on the temporary blended image name has been used).

To set up the project, first get your physical supplies, go through the steps of basic setup of your Raspberry Pi (instructions for this can be found in the Raspberry Pi forums) and set up your equipment according to the fritzing diagram provided. Then upload your image set to the Pi in the designated folder as indicated in the code (or change the code to the directory you would like to use for images). Then adjust any settings in the Python code files relevant to your project and run them through.

Note that the PIL/pillow library also has other options for image manipulation that could be experimented with if you are looking for other types of transition effects.

# Installation
In addition to the files in the current repository, you will utilize the following Python libraries, modules and tools; many of these are built in to the Python3 releases:
  * Pillow:  https://pillow.readthedocs.io/en/stable/installation.html
  * os:  https://docs.python.org/3/library/os.html
  * sys: https://docs.python.org/3/library/sys.html
  * time: https://docs.python.org/3/library/time.html#module-time
  * GPIO: https://sourceforge.net/p/raspberry-gpio-python/wiki/BasicUsage/
  * ImageMagick: https://imagemagick.org/script/download.php
       (or any other image viewer capable of being triggered to open images by Python code)
  

# Credits and acknowledgements:
This project was created for the <b>INFO 697 Physical Computing and Prototyping course at Pratt Institute</b> in Spring 2019 taught by Monica Maceli and Basem Ali. Grateful acknowledgement goes out to the professors and my fellow students who were an enormous help with their feedback on this project.

Code snippet inspiration came from all over forums describing projects with PIL/Pillow and digital photo frame projects, particularly the Raspberry Pi forums and StackExchange. Many thanks go out into the universe of developers posting code and answering each other's questions for engaging in the dialog that produces resources for so many of us working on new coding projects.

# About the Redacted Document:
The document images were taken from different releases of the <b> May 07, 2004 CIA Inspector General's Report on Counterrorism, Detention and Interrogation Activities</b>. Inspriation for the entire project comes from the <b>UNREDACTED blog post of the National Security Archive (https://unredacted.com/2012/04/06/document-friday-the-torture-memos-we-now-know)</b>. The heavily redacted version of the document was accessed from the National Security Archive's online files related to this issue and the less-redacted version in its latest release version (2016 release) was downloaded from the CIA's FOIA Electronic Reading Room. <b>My enormous thanks go to the National Security Archive for everything that they do and all of the increased government transparency that they make possible.</b>

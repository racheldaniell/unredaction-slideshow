# unredaction-slideshow

# This project facilitates the creation of a slideshow of images that will transition when a motion sensor is triggered. 

# In the original project, the slideshow is taken from a U.S. government document related to the use of torture by the CIA that has been released in differently redacted versions, so that the slideshow appears to make the redaction disappear.

# A Fritzing diagram is included to show the materials and setup required, which inncludes a Raspberry Pi 3 B+, MicroBit, and two PIR motion sensors.

# Code is in Python 3. 

# You will also need a series of images to transition. The examples used in the original project are included in this repository. The code is designed to take 2 images and make 3 transitions between them using alpha channel blending, but it can be adjusted for any number of images and any number of blend transitions (just set the alpha value to a different number between 0 and 1 for each transition).

# Recommended naming conventions: It is handy to give your image files a prefix such as "a_", "b_" or "1_", "2_" so that you can control their order. It is also useful to number your transitions (in this example, a numeric suffix on the temporary blended image name has been used).

# To set up the project, first get your physical supplies, go through the steps of basic setup of your Raspberry Pi (instructions for this can be found in the Raspberry Pi forums) and set up your equipment according to the fritzing diagram provided. Then upload your image set to the Pi in the designated folder.

# Note that the PIL/pillow library has other options for image manipulation that could also be experimented with.

# Credits and acknowledgements:
# This project was created for the <b>INFO 697 Physical Computing and Prototyping course at Pratt Institute</b> in Spring 2019. Grateful acknowledgement goes out to the professors, Monica Maceli and Basem Ali were an enormous help in their feedback on and support for this project.
# Code snippet inspiration came from all over forums describing projects with PIL/Pillow and digital photo frame projects, Many thanks go out into the universe of developers posting code and answering each other's questions.
# The document images were taken from different releases of the <b> May 07, 2004 CIA Inspector General's Report on Counterrorism, Detention and Interrogation Activities</b>. Inspriation for the project comes from the UNREDACTED blog post of the National Security Archive (https://unredacted.com/2012/04/06/document-friday-the-torture-memos-we-now-know ). The heavily redacted version of the document was accessed from the National Security Archive's online files related to this issue and the less-redacted version in its latest release version (2016 release) was downloaded from the CIA's FOIA Electronic Reading Room. My enormous thanks go to the National Security Archive for everything that they do and all of the increased government transparency that they make possible.

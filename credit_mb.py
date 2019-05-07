# This code displays the credit line for the redacted document on the attached microbit
# Ideally, microbit is taped to bottom or side of screen where scroll can be easily seen
# in a future version of this project this could be set to scroll on a wider horizontal LCD instead

# flash this code to the microbit as part of setting up display environment

# first import microbit code library

from microbit import *


# display credit line for redacted/unredacted doc

credit_redactdoc = "07 May 2004 - CIA Inspector General Report - BUSH RELEASE VS OBAMA RELEASE"


while True:
    display.scroll(credit_redactdoc)
    sleep(100)

# Ideally this basic info is accompanied with longer doc explanation/credit on paper handout or walltag for users who are interested
# or else with verbal explanations by project author
import sys
from time import sleep
from random import uniform

words = "Extraction: Two very large bears from the wilderness [Completed]"
for char in words:
    sleep(uniform(0, 0.03))
    sys.stdout.write(char)
    sys.stdout.flush()
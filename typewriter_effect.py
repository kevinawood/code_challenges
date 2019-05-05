import sys
from time import sleep
from random import uniform

words = "Extraction: Two very large bears from the wilderness [Completed]"

print('\033[1;30mGreen like Ghost\033[1;m')

for char in words:
    sleep(uniform(0, 0.1))
    sys.stdout.write(char)
    sys.stdout.flush()
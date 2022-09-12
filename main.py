import random
import sys
from time import sleep

for x in range(15): 
    sleep(1)
    print("Hello World!")
code = random.choice([0,1])
sys.exit(code)
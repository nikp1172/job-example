import random
import sys
from time import sleep

for x in range(30): 
    sleep(2)
    print("hello world")
code = random.choice([0,1])
sys.exit(code)
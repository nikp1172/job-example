import random
import sys
from time import sleep

for i in range(10):
    for x in range(15): 
        sleep(1)
        print("hello world")
    sleep(20)
code = random.choice([0,1])
sys.exit(code)

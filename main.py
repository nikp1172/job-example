import random
import sys
from time import sleep

for x in range(40000): 
    print(f"hello world {x}")
code = random.choice([0,1])
sys.exit(code)

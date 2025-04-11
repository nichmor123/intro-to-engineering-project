import os

pins = [2, 5, 7, 8, 25, 23, 3, 4]

for x in pins:
    os.system(f"gpio write {x} 0")
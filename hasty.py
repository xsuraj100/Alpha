import os
import time

filename = "data.txt"

print("Created:", time.ctime(os.path.getctime(filename)))
print("Modified:", time.ctime(os.path.getmtime(filename)))
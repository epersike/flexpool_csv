import os
import sys
from reader import read_file
from writer import write_workook

REWARDS_FILENAME = 'rewards-api.csv'
OUTPUT_FILENAME = os.sep.join(['output','rewards-out.xlsx'])

from_api = input("Get from api? [Y/n] ")
if from_api != 'y':
    REWARDS_FILENAME = 'rewards.csv'
else:
    from api import get_file_from_api
    get_file_from_api(REWARDS_FILENAME)

if not os.path.exists(REWARDS_FILENAME):
    print("File {} not found... bye".format(REWARDS_FILENAME))
    sys.exit()

print("Reading file {}...".format(REWARDS_FILENAME))
lines = read_file(REWARDS_FILENAME)
if not lines:
    print("Unable to read file lines!!")
    sys.exit(0)

print("File opened successfully, {} lines found...".format(len(lines)))
print("Writing file: {}".format(OUTPUT_FILENAME))
write_workook(lines,OUTPUT_FILENAME)
print("File wrote successfully.")
os.system("open {}".format(OUTPUT_FILENAME))
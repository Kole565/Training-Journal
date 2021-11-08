"""Add Training.

Part of training journal.
Get train info, push to db.

Usage:
Follow printed instructions.

"""

from time import sleep

import os, sys
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from lib.helpers.add_training_helper import check_inp, add_next_dict

print("In every question remember: 'quit' for quit and 'none' for nothing")

data = {}
add_next = True # Question after "train added"; "Want to add another train?"
while add_next:
	print("Name (train title): (any text)")
	data["name"] = check_inp(input())
	
	print("Time (train duration): (1:20:30)")
	data["time"] = check_inp(input())

	print("Distance (for run; optional): (in meters)")
	data["distance"] = check_inp(input())

	print("\nYour train:")
	for f, v in data.items():
		print("\t{0}: {1}".format(f.capitalize(), v))
	# Save train there
	print("\nTrain not saved")

	print("Want to add another train?(y, n)")
	add_next = bool(add_next_dict.get(input()))

print("Bye!")
sleep(2)

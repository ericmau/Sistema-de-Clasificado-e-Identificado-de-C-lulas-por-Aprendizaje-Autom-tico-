# USAGE
# python detect_color.py --image pokemon_games.png

# import the necessary packages
import numpy as np
import argparse
import cv2
from PIL import Image

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image")
args = vars(ap.parse_args())

# load the image
image = cv2.imread(args["image"])

# define the list of boundaries
boundaries = [
    ([0,0,0],[219,112,147]),
	([0,0,0],[238,104,123]),
    ([0,0,0],[205,90,106])
    #([0,0,0],[139,26,85])
    #([139,0,139], [255,62,191])
]

output = Image.new("L", (1200, 1200))

# loop over the boundaries
for (lower, upper) in boundaries:
	# create NumPy arrays from the boundaries
	lower = np.array(lower, dtype = "uint8")
	upper = np.array(upper, dtype = "uint8")

	# find the colors within the specified boundaries and apply
	# the mask
	mask = cv2.inRange(image, lower, upper)

	output = cv2.bitwise_and(image, image, mask = mask)




	# show the images
	#cv2.imshow("images", np.hstack([image, output]))
	cv2.imwrite("/Users/eric/Desktop/salida2.jpg", output)
	break

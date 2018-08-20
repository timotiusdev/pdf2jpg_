# convert jpg image to tif file format
# using existing convert.py we can convert
# pdfs, jpg, or png image into tif file format

import argparse # for input argument in the terminal
from PIL import Image
import os
import glob
import convert as c # reuse our convert.py function

def jpg2tif(dir, dir_, i):
    # folder of images
    dir = str(dir)
    # make sure all input is jpg
    cek = c.inputCheck(dir_)
    # Input is jpg
    input_ = str(cek)
    #check input_ directory
    # print("this is input_ {}".format(input_))

    # tif output directory
    out_ = dir + str(i) + ".tif"
    # check out_ directory
    # print("this is out_ {}".format(out_))
    
    # image processing using PIL
    im = Image.open(input_)
    im = im.convert('L')  # convert image to black and white
    im.save(out_)
    print('done')
    # returning *.tif directory
    return out_

# argument input : file directory
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True, help="File Directory Path")
args = vars(ap.parse_args())

# sequential start from
i = 0

#run in one directory
dir = str(args["input"])
# print all files on directory
files = os.listdir(dir)
print(files)
for file in files:
    # print file to convert
    print(file)
    dir_ = os.path.join(dir, file)
    jpg2tif(dir, dir_, i)
    i += 1
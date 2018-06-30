from wand.image import Image as imgs
import os
from PIL import Image as I

# PDF2IMAGE
def pdf2jpg(filename):
    with imgs(filename=filename, resolution=300) as img:
        img.compression_quality = 99
        img.save(filename= str(filename[:-4]) + ".jpg")
        print("converting {} done!".format(filename))

#CHECK INPUT
def inputCheck(filename):
    if (str(filename[-3:])) == "pdf":
        print("input file pdf, converting to jpg . . . ")
        pdf2jpg(filename)
    elif ((str(filename[-3:])) == "png" or (str(filename[-3:])) == "bmp"):
        print("input file png or bmp, converting to jpg . . . ")
        img = I.open(filename)
        convert = img.convert('RGB')
        convert.save(filename[:-4] + '.jpg')
    elif ((str(filename[-3:])) == "jpg" or (str(filename[-3:])) == "peg" or (str(filename[-3:])) == "JPG" or (str(filename[-3:])) == "PEG"):
        print("input file {}! Convert to RGB".format(filename))
        img = I.open(filename)
        convert = img.convert('RGB')
        convert.save(str(filename))
    else:
        print("input file (*{}) is not supported".format((str(filename[-4:]))))

#CHECK IN DIRECTORY
def dirCheck(DIR):
    print("dirCheck start . . . ")
    files = os.listdir(DIR)
    for file in files:
        dir_ = os.path.join(DIR, file)
        print(dir_)
        inputCheck(dir_)
    print("dirCheck done!")
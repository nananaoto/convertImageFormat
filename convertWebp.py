# Convert all Webp files in selected directories

import sys
import os
import glob
from PIL import Image

# original image format
#origFormat = 'webp'
origFormat = ''
# converted image format
convFormat = 'jpg'
# compress quality
compressQuality = 100

def convertWebp(dirPath):
    print("start converting {0} files to {1} in {2}".format(origFormat, convFormat, dirPath))
    # change current directory
    os.chdir(dirPath)
 
    # list of Webp files
    fileList = glob.glob('*' + origFormat)

   # make a directory to save converted files
    #convDir = os.path.basename(dirPath) + '_' + convFormat
    convDir = os.path.basename(os.getcwd()) + '_' + convFormat
    os.makedirs(convDir, exist_ok=True)

    # convert files
    for origFile in fileList:
        # open file
        print("\r" + "converting {}".format(origFile), end="")
        filenameNoExt = os.path.splitext(origFile)[0]
        image = Image.open(origFile).convert('RGB')
        # save a file
        image.save(convDir + '/' + filenameNoExt + '.' + convFormat, quality=compressQuality)
    print()
    print("finished converting")

if __name__ == '__main__':
    numDirs = len(sys.argv) - 1
    for i in range(1, len(sys.argv)):
        if not os.path.exists(sys.argv[i]):
            print("Wrong path")
            print("Input a path of target directory as argument")
        else:
            convertWebp(sys.argv[i])


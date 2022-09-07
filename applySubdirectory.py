# apply convertWebp.py to all directories in specified directory

import sys
import os
import glob
import subprocess

if __name__ == '__main__':
    if len(sys.argv) > 2:
        print("Too many arguments")
    elif not os.path.exists(sys.argv[1]):
        print("Wrong path")
        print("Input a path of target directory as argument")
    else:
        #os.chdir(sys.argv[1])
        dires = glob.glob(sys.argv[1] + '*')
        for i in dires:
            #dirPath = sys.argv[1] + i
            subprocess.run("python convertWebp.py {}".format(i), shell=True)

# -*- coding: utf-8 -*-
'''
Created on 2016-03-22

@author: HuangZili
'''

import sys
import time
import os

def main():
    '''
    This will be called if the script is directly envoked.
    '''
    workdir = sys.argv[1]
    workdir = workdir.rstrip('/') + '/'
    try:
        xdays = int(sys.argv[2])
    except IndexError:
        xdays = 30

    # Get the current time
    now = time.time()
    # Loop through all the files in the working directory
    for f in os.listdir(workdir):
        fpath = os.path.join(workdir, f)
        if os.stat(fpath).st_mtime < now - xdays * 86400:
            # Check it's a file
                if os.path.isfile(fpath):
                    os.remove(fpath)

if __name__ == '__main__':
    main()

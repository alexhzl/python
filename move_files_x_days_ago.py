# -*- coding: utf-8 -*-
'''
Created on 2016-03-22

@author: HuangZili
'''

import sys
import time
import os
import shutil

def main():
    '''
    This will be called if the script is directly envoked.
    '''
    srcdir = sys.argv[1]
    srcdir = srcdir.rstrip('/') + '/'
    dstdir = sys.argv[2]
    dstdir = dstdir.rstrip('/') + '/'
    if not os.path.exists(dstdir):
        print 'Error: folder ' + dstdir + ' not exists.'
        sys.exit(1)
    
    try:
        xdays = int(sys.argv[3])
    except IndexError:
        xdays = 30

    # Get the current time
    now = time.time()
    # Loop through all the files in the working directory
    for f in os.listdir(srcdir):
        fpath = os.path.join(srcdir, f)
        if os.stat(fpath).st_mtime < now - xdays * 86400:
            # Check it's a file
                if os.path.isfile(fpath):
                    shutil.move(fpath, dstdir) 

if __name__ == '__main__':
    main()

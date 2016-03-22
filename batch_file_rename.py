# -*- coding: utf-8 -*-
'''
Created on 2016-03-22

@author: HuangZili
'''

import os
import sys
import getopt

def usage():
    print 'batch_file_rename.py usage:'
    print '-h, --help: print help message.'
    print '-v, --version: print script version'
    print '-w, --workdir: The dir of files that you want to rename.'
    print '-o, --oldext: The extension of files that you want to rename.'
    print '-n, --newext: The extension of files that you want to rename to.'
    
def version():
    print 'batch_file_rename.py 0.0.1'
    
def main(argv):
    try:
        opts, args = getopt.getopt(argv[1:], 'hvwon:')
    except getopt.GetoptError, err:
        print str(err)
        usage()
        sys.exit(1)
    for o, a in opts:
        if o in ('-h', '--help'):
            usage()
            sys.exit(0)
        elif o in ('-v', '--version'):
            version()
            sys.exit(0)
        elif o in ('-w',):
            workdir = a
        elif o in ('-o',):
            oldext = a
        elif o in ('-n',):
            newext = a
        else:
            print 'unhandled option'
            sys.exit(1)
    batch_rename(workdir, oldext, newext)
     
def batch_rename(workdir, oldext, newext):
    '''
    This will batch rename a group of files in a given directory,
    once you pass the current and new extensions
    '''
    for filename in os.listdir(workdir):
        file_ext = os.path.splitext(filename)[1]
        if oldext == file_ext:
            newfile = filename.replace(oldext, newext)
            os.rename(
              os.path.join(workdir, filename),
              os.path.join(workdir, newfile)
            )

if __name__ == '__main__':
    main(sys.argv)

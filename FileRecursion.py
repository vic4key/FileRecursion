# -*- coding: ascii -*-

'''''''''''''''''''''''''''''''''
@Author	: Vic P.
@Email  : vic4key@gmail.com
@Name   : File Recursion
'''''''''''''''''''''''''''''''''

import os, sys, glob, shutil
import vp as rg

''' INPUT '''
INPUT_DIRECTORY = r"C:\Intel"
INPUT_EXTENSION = ["*"]

''' GLOBAL VARIABLES '''
LINE_FIXED = 80
NUMBER_OF_FILE = 0
LIST_EXTENSION = []
PARENT_DIRECTORY = ""

def rgFixDirectory(Directory):
    if Directory[-1] != '\\': Directory += "\\"
    return Directory

def rgCopyFile(FilePath, DestinationDirectory):
    if not os.path.isdir(DestinationDirectory): return
    DestinationDirectory = rgFixDirectory(DestinationDirectory)
    DstFilePath = DestinationDirectory + rg.ExtractFileName(FilePath)
    shutil.copy(FilePath, DstFilePath)
    return

def rgMoveFile(FilePath, DestinationDirectory):
    if not os.path.isdir(DestinationDirectory): return
    DestinationDirectory = rgFixDirectory(DestinationDirectory)
    DstFilePath = DestinationDirectory + rg.ExtractFileName(FilePath)
    shutil.move(FilePath, DstFilePath)
    return

def rgDeleteFile(FilePath): os.remove(FilePath)

def rgCallback(Index, SubDirectory, FilePath, FileExtension):
    print "%d. `%s` - `%s` - `%s`" % (Index, SubDirectory, FilePath, FileExtension)
    return

def rgRecusive(Directory, FileExtensions, ParentDirectory=True):
    Directory = rgFixDirectory(Directory)

    if not os.path.isdir(Directory):
        print "ERROR: Directory is not existing `%s`" % Directory
        return
    
    global LEVEL
    global NUMBER_OF_FILE
    global LIST_EXTENSION
    global PARENT_DIRECTORY
    
    if ParentDirectory == True:
        PARENT_DIRECTORY = Directory
        LIST_EXTENSION =  map(lambda extension: extension.upper(), FileExtensions)
        print "[.]".center(LINE_FIXED, "-")
    
    SubDirectory = ""
    LengthParentDirectory = len(PARENT_DIRECTORY)
    if LengthParentDirectory != 0: SubDirectory = Directory[LengthParentDirectory:]
    
    if len(SubDirectory) == 0: SubDirectory = "."

    l = glob.glob(Directory + "*")
    l.reverse();
    for e in l:
        if os.path.isfile(e):
            ext = rg.ExtractFileExtension(e, False).upper()
            if "*" in LIST_EXTENSION or ext in LIST_EXTENSION:
                NUMBER_OF_FILE += 1
                rgCallback(NUMBER_OF_FILE, SubDirectory, e, ext)
        elif os.path.isdir(e):
            print ("[%s]" % e[len(PARENT_DIRECTORY):]).center(LINE_FIXED, "-") 
            rgRecusive(e, ["*"], False)
    
    return

def main():
    try:
        print "[START]".center(LINE_FIXED, "*")
        rgRecusive(INPUT_DIRECTORY, INPUT_EXTENSION)
        print "[DONE]".center(LINE_FIXED, "*")
    except (Exception, KeyboardInterrupt): rg.LogException(sys.exc_info())
    return 0

if __name__ == "__main__":
    main()
    sys.exit()
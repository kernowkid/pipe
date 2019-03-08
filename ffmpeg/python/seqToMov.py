import subprocess as sp
import sys
import os
import re

##sys.argv[1] is the file to upload -- need to replace frame number with %04d
file = sys.argv[1]
file = file.replace('\\','/')

##file name
origFileName = os.path.basename( file )

##extract path to file
path = os.path.dirname( file )

##create dir for mp4
movPath = path+'/'+'mp4/' 
if not os.path.exists( movPath ):
        os.mkdir( movPath )

##rebuild path and file name, replacing frame number with %04d
fname, fileExt = os.path.splitext(origFileName)

if '.' not in fname.split('_')[-1]:
    fileName = '_'.join(fname.split('_')[:-1])
    startNumber = fname.split('_')[-1]
    movFileName = '_'.join(origFileName.split('_')[:-1]) + '.mp4'
else:
    fileName = fname.split('.')[-2]
    startNumber = fname.split('.')[-1]
    movFileName = fileName + '.mp4'


paddingAmount = len(startNumber)
filePadding = '.%0'+ str(paddingAmount)+'d'
newFileName = path + '/' + fileName + filePadding + fileExt
newFileName = newFileName.replace('/','\\')


##build ffmpeg cmd 
cmd="ffmpeg -framerate 25 -start_number %s -i %s -s 1920x1080 -c:v libx264 -crf 18 -b:v 4M -pix_fmt yuv420p -movflags +faststart %s" %(startNumber,newFileName,movFile)
sp.call(cmd,shell=True)
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
drive = path.split('/')[0]

##rebuild path and file name, replacing frame number with %04d
fname, fileExt = os.path.splitext(origFileName)
fileName = '_'.join(fname.split('_')[:-1])
filePadding = '_%4d'
newFileName = fileName + filePadding + fileExt

##create dir for mp4
movPath = path+'/'+'mp4/' 
if not os.path.exists( movPath ):
        os.mkdir( movPath )

## create mp4 name and path
movFileName = '_'.join(origFileName.split('_')[:-1]) + '.mp4'
movFile = 'mp4/' + movFileName

##build ffmpeg cmd 
cmd="%s&& cd %s&& ffmpeg -i %s -s 1920x1080 -vcodec libx264 -crf 25 -b:v 4M -pix_fmt yuv420p %s" %(drive,path,newFileName,movFile)
sp.call(cmd,shell=True)

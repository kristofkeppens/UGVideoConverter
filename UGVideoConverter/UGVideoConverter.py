#! /usr/bin/env python

'''
Created on Jun 15, 2009

@author: kristof
'''
'''
Python script that transcodes a directory of video files
to pre-specified video profiles and places them in a flv 
dir for streaming.
'''
import os
import sys

def main():
  
  #path variables
  inpath = "/home/kristof/UG_ST/incoming"
  outpath = "/home/kristof/UG_ST/flv"
  
  #get filenames from an input path
  filelist = os.listdir(inpath)
  filecount = 0
  for file in filelist:
    if os.path.isfile(inpath + '/' + file):
      filecount = filecount + 1
  
  totalcount = 0
  
  #Loop through files and convert
  for inname in filelist:
    if os.path.isfile(inpath + '/' + inname):
      outfile = inname.split(".")
      outfile.pop()
      outname = outfile.pop()
      
      #define profiles
      
      #high definition
      highdef = 'ffmpeg -i "' + inpath + '/' + inname + '" -f flv -vcodec libx264 -b 2500k -s hd720 -qscale .2 -ar 22050 -ac 2 -ab 96k -threads 2 ' + outpath + '/' + outname + '_hd.flv' + '| flvtool2 -UP ' + outpath + '/' + outname + '_hd.flv'
      #high quality
      highquality = 'ffmpeg -i "' + inpath + '/' + inname + '" -f flv -vcodec libx264 -b 1000k -s 720x540 -qscale 1 -ar 22050 -ac 2 -ab 96k -threads 2 ' + outpath + '/' + outname + '_high.flv' + '|flvtool2 -UP' + outpath + '/' + outname + '_high.flv'
      #medium quality
      mediumquality = 'ffmpeg -i "' + inpath + '/' + inname + '" -f flv -vcodec libx264 -b 700k -s 480x360 -qscale 2 -ar 22050 -ac 2 -ab 96k -threads 2 ' + outpath + '/' + outname + '_medium.flv' + '| flvtool2 -UP' + outpath + '/' + outname + '_medium.flv'
      #low quality
      lowquality = 'ffmpeg -i "' + inpath + '/' + inname + '" -f flv -vcodec libx264 -b 400k -s 320x240 -qscale 4 -ar 22050 -ac 2 -ab 96k -threads 2 ' + outpath + '/' + outname + '_low.flv"' + '| flvtool2 -UP ' + outpath + '/' + outname + '_low.flv'
      
      #convert video
        
      if(not os.path.isfile(outpath + "/" + outname + "_hd.flv")):
        print "converting" + str(totalcount) + " of " + str(filecount) + "in high definition"
        os.system(highdef)
      else:
        print "file allready converted"
        
      if(not os.path.isfile(outpath + "/" + outname + "_high.flv")):
        print "converting" + str(totalcount) + " of " + str(filecount) + "in high quality"
        os.system(highquality)
      else:
        print "file allready converted"
        
      if(not os.path.isfile(outpath + "/" + outname + "_medium.flv")):
        print "converting" + str(totalcount) + " of " + str(filecount) + "in medium quality" 
        os.system(mediumquality)
      else:
        print "file allready converted"
        
      if(not os.path.isfile(outpath + "/" + outname + "_low.flv")):
        print "converting" + str(totalcount) + " of " + str(filecount) + "in low quality" 
        os.system(lowquality)
        totalcount = totalcount + 1
      else:
        print "file allready converted"
    
    print str(totalcount) + " of " + str(filecount) + " file(s) converted."
    sys.exit()
  
def getVideoResolution(param):
  '''
  TODO get video resolution
  video trancoding can than be done depending on the original size
  '''
  video = param
  #ffmpeg command to get video resolution
  command = 'tcprobe -i ' + video + ' > ' + video + '.txt'
  temp = os.system(command)
  
  infile = open(outpath + '/' + video + '.txt', 'r')
  indata = infile.readlines()
  infile.close()
  for inline in indata:
    if inline.find("width="):
      pass



if __name__ == '__main__':
    main()
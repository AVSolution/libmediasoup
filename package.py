#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import sys
import time
import platform
import shutil
import glob
import requests
import json
import zipfile
  
def system(command):
    retcode = os.system(command)
    if retcode != 0:
        raise Exception("Error while executing:\n\t %s" % command)
def main():
    version = "0.0.0"
    isOnline = "0"
    channel = "stable"
    paramlen = len(sys.argv)
    print("paramlen:" + str(paramlen))
    if paramlen == 3:
       version = sys.argv[1]
       isOnline = sys.argv[2]
       print("version:"+str(version)+" isOnline:"+str(isOnline))
    elif paramlen == 2:
       version = sys.argv[1]
       print("version:"+str(version))
    elif paramlen == 1:
       print("version:"+str(version)+" isOnline:"+str(isOnline))
    else:
       print("params error.");
       return;
    if isOnline == "0":
        channel = "test"  
    system('conan create . LibMediaSoup/%s@bixin/%s -s compiler.version=16 -s arch=x86 -s build_type=Debug' % (version,channel))
    system('conan create . LibMediaSoup/%s@bixin/%s -s compiler.version=16 -s arch=x86 -s build_type=Release' % (version,channel))
    if isOnline == "1":
       system('conan upload LibMediaSoup/%s@bixin/%s --all -r=pc' % (version,channel))
       system('git tag %s' % version)
       system('git push --tags')
if __name__ == "__main__":
    main()

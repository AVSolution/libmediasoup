#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import sys
import glob
import subprocess
excludeSet = {}

def sign(file):
    for i in range(0,3):
        sign_proc = subprocess.Popen("signtool sign /v /ac MSCV-GSClass3.cer /fd sha1 /f pcyuer.pfx /p Xxqpc111! /tr http://rfc3161timestamp.globalsign.com/advanced /td sha256 %s" %(file))
        ret = sign_proc.wait()
        if ret ==0:
            return

for file in glob.glob(os.path.join('../bin/Release', '*.exe')):
    filepath,filename = os.path.split(file)
    if filename not in excludeSet:
        print("signed: "+file)
        sign(file)
for file in glob.glob(os.path.join('../bin/Release', '*.dll')):
    filepath,filename = os.path.split(file)
    if filename not in excludeSet:
        print("signed: "+file)
        sign(file) 
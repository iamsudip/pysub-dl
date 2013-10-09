#!/usr/bin/env python

import os
import sys
import requests
import zipfile
from prompt_user import prompt

def download_file(url):
    ''' Downloads and extracts the url content.

       :kwarg url: Contains the download link to raw data.

    '''
    response = requests.get(url, stream = True)
    with open('subtitle.zip', 'wb') as out_file:
        fsrc = response.raw
        size = response.headers.get("content-length")
        length = 16*1024
        while True:
            buf = fsrc.read(length)
            if not buf:
                break
            out_file.write(buf)
            sys.stdout.write("Downloaded " + str(os.path.getsize('subtitle.zip')/1024) + "kb of " + str(int(size)/1024) + " kb\r")
            sys.stdout.flush()
        print "\nDownload complete\nExtracting"
    del response
    try:
        zipfile.ZipFile.extractall(zipfile.ZipFile('subtitle.zip'))
        os.remove('subtitle.zip')
    except:
        print "* The subtitle file is not good to extract."
        return 'no'
    return prompt()

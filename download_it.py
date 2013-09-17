#!/usr/bin/env python

import os
import requests
import shutil
import zipfile
from prompt_user import prompt

def download_file(url):
    ''' Downloads and extracts the url content.

       :kwarg url: Contains the download link to raw data.

    '''
    response = requests.get(url, stream = True)
    with open('subtitle.zip', 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response
    try:
        zipfile.ZipFile.extractall(zipfile.ZipFile('subtitle.zip'))
        os.remove('subtitle.zip')
    except:
        print "* The subtitle file is not good to extract."
        return 'no'
    return prompt()

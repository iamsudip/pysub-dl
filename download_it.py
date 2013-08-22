#!/usr/bin/env python

import requests
import shutil
import zipfile
import os
from prompt_user import prompt

def download_file(url):
    ''' Downloads the File provided by subscene.
    '''
    response = requests.get(url, stream = True)
    with open('%s.zip' % ('outfile'), 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response
    zipfile.ZipFile.extractall(zipfile.ZipFile('outfile.zip'))
    os.remove('outfile.zip')
    return prompt()

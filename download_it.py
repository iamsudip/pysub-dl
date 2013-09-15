#!/usr/bin/env python

import requests
import shutil
from prompt_user import prompt

def download_file(url):
    ''' Downloads the File.

       :kwarg url: Contains the download link to raw data.

    '''
    response = requests.get(url, stream = True)
    with open('subtitle.zip', 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response
    return prompt()

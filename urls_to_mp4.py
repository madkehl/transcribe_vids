import urllib.request
import urllib.error
import os
from datetime import datetime
import time
import requests


def urls_to_mp4():
    """
    takes urls txt file and then writes the videos to new data folder
    :return:
    """
    url_file = open('urls.txt', 'r')
    lines = url_file.readlines()
    name = './data'
    if os.path.isdir(name):
        today = datetime.now()
        name = './' + today.strftime("%d_%m_%Y_%H_%M_%S") + '_data'
        os.mkdir(name)
    else:
        os.mkdir('./data')

    for i, line in enumerate(lines):
        file_name = str(i) + '.mp4'
        try:
            urllib.request.urlretrieve(line, name + '/' + file_name)
        except urllib.error.HTTPError:
            r = requests.get(line, stream=True)
            if str(r) == '<Response [403]>':
                print('You do not have permissions to access this URL (403)')
            else:
                with open(name + '/' + file_name, 'wb') as outfile:
                    for chunk in r.iter_content(chunk_size=1024):
                        # writing one chunk at a time to mp4 file
                        if chunk:
                            outfile.write(chunk)

        time.sleep(2)

    return name

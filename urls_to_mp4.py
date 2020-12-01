import urllib.request
import os
from datetime import datetime


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
        urllib.request.urlretrieve(line, name + '/' + file_name)

    return name

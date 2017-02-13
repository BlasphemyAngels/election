# !/usr/bin/python3
# _*_coding: utf-8_*_
"""read data from source"""
import utils
import os
import pandas as pd
def read_data():
    """
        read data from source
    return the data read from source
    """
    vpath = __file__
    relpath = os.path.abspath(__file__)
    dirpath = relpath[0:relpath.rfind(vpath)]
    dirpath = "{}data/".format(dirpath)
    filename = os.listdir(dirpath)[0]
    zfile = utils.unzipfile(dirpath + filename, dirpath)
    data_df = pd.read_csv(dirpath + zfile.namelist()[0],\
            usecols=['enddate', 'rawpoll_clinton', 'rawpoll_trump',\
            'rawpoll_johnson', 'rawpoll_mcmullin', 'adjpoll_clinton', \
            'adjpoll_trump', 'adjpoll_johnson', 'adjpoll_mcmullin'],
            dtype='str')
    return data_df
if __name__ == '__main__':
    data_df = read_data()
    print('data size: %d' % data_df.shape[0])


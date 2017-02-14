# !/usr/bin/python3
# _*_coding: utf-8_*_
"""read data from source"""
from utils import utils
import os
import pandas as pd
import numpy as np
def read_data():
    """
        read data from source
    @return: the data read from source
    """
    vpath = __file__
    relpath = os.path.abspath(__file__)
    dirpath = relpath[0:relpath.rfind(vpath)]
    dirpath = "{}data/".format(dirpath)
    filename = os.listdir(dirpath)[0]
    zfile = utils.unzipfile(dirpath + filename, dirpath)
    data_df = pd.read_csv(dirpath + zfile.namelist()[0],\
            usecols=['enddate', 'rawpoll_clinton', 'rawpoll_trump',\
            'adjpoll_clinton', 'adjpoll_trump'])
    return data_df
def clean_data(data_df):
    """
        clean the data : filtering the broken data and format the data
    @parm data_df: the source data needed to clean
    @return: the cleaned data
    """
    #filter the nan data
    data_df = data_df.dropna()
    print('clean data size: %d' % data_df.shape[0])
    #get the date data
    date_s = pd.to_datetime(data_df.pop('enddate')).dropna() 
    #get the clinton origin data
    rawpoll_clinton = data_df.pop('rawpoll_clinton').dropna()
    #get the trump origin data
    rawpoll_trump = data_df.pop('rawpoll_trump').dropna()
    #get the clinton adjust data
    adjpoll_clinton = data_df.pop('adjpoll_clinton').dropna()
    #get the trump adjust data
    adjpoll_trump = data_df.pop('adjpoll_trump').dropna()

if __name__ == '__main__':
    data_df = read_data()
    print('data size: %d' % data_df.shape[0])
    clean_data(data_df)

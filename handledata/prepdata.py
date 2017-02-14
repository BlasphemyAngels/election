# !/usr/bin/python3
# _*_coding: utf-8_*_
"""read data from source"""
import os
from election.utils import utils
import pandas as pd


def read_data():
    """
        read data from source
    @return: the data read from source
    """
    print('start read data')
    print('...')
    vpath = __file__
    relpath = os.path.abspath(__file__)
    dirpath = relpath[0:relpath.rfind(vpath)]
    dirpath = "{}data/".format(dirpath)
    filename = os.listdir(dirpath)[0]
    zfile = utils.unzipfile(dirpath + filename, dirpath)
    data_df = pd.read_csv(dirpath + zfile.namelist()[0],\
            usecols=['enddate', 'rawpoll_clinton', 'rawpoll_trump',\
            'adjpoll_clinton', 'adjpoll_trump'])
    print('data size: %d' % data_df.shape[0])
    print('read data finish')
    return data_df
def clean_data(data_df):
    """
        clean the data : filtering the broken data and format the data
    @parm data_df: the source data needed to clean
    @return: the cleaned data
    """
    print('start clean data')
    print('...')
    #filter the nan datka
    data_df = data_df.dropna()
    #transform the datetime to %Y-%m-%d
    data_df['enddate'] = pd.to_datetime(data_df['enddate'])
    #transform the datetime to %Y-%m
    data_df['enddate'] = data_df['enddate'].map(lambda t: t.strftime('%Y-%m'))
    print('clean data size: %d' % data_df.shape[0])
    print('clean data finish')

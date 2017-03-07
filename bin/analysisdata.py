#!/usr/bin/env python
# _*_coding: utf-8_*_

"""Analysis the data and show it in a image"""

import matplotlib.pyplot as plt
import prepdata
import numpy as np

if __name__ == '__main__':
    data_df = prepdata.read_data()
    data_df = prepdata.clean_data(data_df)
    # print(data_df['rawpoll_trump'][0])
    # print(type(data_df['rawpoll_trump'][0]))
    data_group = data_df.groupby(['enddate'])
    data_group_sum_df = data_group.sum()
    # print(type(data_group_sum_df))
    fig, subplot_arr = plt.subplots(2, 2, figsize=(15, 10))
    # print(data_group_sum_df['rawpoll_trump'].tolist())
    subplot_arr[0, 0].plot(data_group_sum_df['rawpoll_trump'].tolist(), color='r')
    subplot_arr[0, 0].plot(data_group_sum_df['rawpoll_clinton'].tolist(), color='g')
    subplot_arr[1, 0].plot(data_group_sum_df['adjpoll_trump'].tolist(), color='r')
    subplot_arr[1, 0].plot(data_group_sum_df['adjpoll_clinton'].tolist(), color='g')
    #draw bar
    width = 0.25
    x = np.arange(data_group_sum_df.shape[0])
    subplot_arr[0, 1].bar(x, data_group_sum_df['rawpoll_trump'].tolist(), width, color='r')
    subplot_arr[0, 1].bar(x + width, data_group_sum_df['rawpoll_clinton'].tolist(), width, color='g')
    subplot_arr[1, 1].bar(x, data_group_sum_df['adjpoll_trump'].tolist(), width, color='r')
    subplot_arr[1, 1].bar(x + width, data_group_sum_df['adjpoll_trump'].tolist(), width, color='g')
    subplot_arr[0, 1].set_xticks(x + width)
    subplot_arr[0, 1].set_xticklabels(data_group_sum_df.index.tolist(), rotation='vertical')
    subplot_arr[1, 1].set_xticks(x + width)
    subplot_arr[1, 1].set_xticklabels(data_group_sum_df.index.tolist(), rotation='vertical')
    plt.subplots_adjust(wspace=0.2)
    plt.show()

#!/usr/bin/env python 
# coding:utf-8
# @Time :8/17/18 15:39


def execute(raw_params, filter_empty=True):
    convert_params = {i.split('=')[0]: i.split('=')[1] for i in raw_params.split('&')}
    if filter_empty:
        convert_params = {j: k for j, k in convert_params.items() if k}
    return convert_params


if __name__ == '__main__':
    raw_params = "f_noticeid=402848d365409df20165469f6783101b&xqType=cggg&type=1"
    print execute(raw_params)

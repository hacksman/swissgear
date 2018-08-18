#!/usr/bin/env python 
# coding:utf-8
# @Time :8/17/18 15:39


def execute(raw_params, filter_empty=True):
    convert_params = {i.split('=')[0]: i.split('=')[1] for i in raw_params.split('&')}
    if filter_empty:
        convert_params = {j: k for j, k in convert_params.items() if k}
    return convert_params


if __name__ == '__main__':
    raw_params = "1=1&currentPage=1&query.title=&query.cglb=&query.gglx=3&query.cgfs=&query.time_s=&query.time_e=&query.areacode=&query.endtime_s=&query.endtime_e="
    print execute(raw_params)

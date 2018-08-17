#!/usr/bin/env python 
# coding:utf-8
# @Time :8/17/18 15:39


def execute(raw_params):
    return {i.split('=')[0]: i.split('=')[1] for i in raw_params.split('&')}

if __name__ == '__main__':
    raw_params = "nType=prcmNotices&pType=&prcmPrjName=&prcmItemCode=&prcmOrgName=&startDate=2018-01-01&endDate=2019-01-01&prcmPlanNo=&page=3&pageSize=18"
    print execute(raw_params)

# !/Library/Frameworks/Python.framework/Versions/2.7/bin/Python
# -*- coding: utf-8 -*-

__author__ = "Cloga Chen(Cloga0216@gmail.com)"
__copyright__ = "Copyright (c) 2014 Cloga Chen"
__createtime__ = "2014-11-14 14:17:58"
__modifytime__ = "2014-11-14 14:17:59"

import pandas as pd
traffic = pd.read_excel('Paid Search Traffic.xlsx', sheetname='Dataset1')
kws_list = pd.read_excel('E-UP_kws_list_tracking_2014_10_14.xlsx', 0)
df = pd.merge(traffic, kws_list, how='left', left_on='Source / Medium', right_on ='&utm_medium=')
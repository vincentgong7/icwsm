'''
Created on 14 Feb 2017

@author: vgong
'''

from datetime import datetime as dt1
import time
# import datetime as dt2

# parse date from text based on standard format
def my_date_parse_withtimezone(str="2015-08-23 08:40:19+02"):
#     str = "2015-08-23 08:40:19+02"
    the_format = "%Y-%m-%d %H:%M:%S+02"
    t = dt1.strptime(str, the_format)
    return t

def my_date_parse(str="2015-08-23 08:40:19"):
#     str = "2015-08-23 08:40:19"
#     format = "%Y-%m-%d %H:%M:%S"
#     t = dt1.strptime(str."+02", format)
    t = my_date_parse_withtimezone(str+"+02")
    return t

# parse a python date fram a timestamp text
def ts2date(ts):
    t = dt1.fromtimestamp(ts)
#   if the ts requires adjustment
#     adjust_timezone = dt2.timedelta(hours = 2)
#     t = t + adjust_timezone
    return t
# print(ts2date(1.4399e+09))

def textdate2ts(strdate):
    date = my_date_parse(strdate)
    return round(time.mktime(date.timetuple()))


def date2ts(strdate):
    return textdate2ts(strdate)
'''
Created on 19 Sep 2017

@author: vgong
'''
import numpy as np
from scipy.stats.stats import pearsonr   
from scipy.stats import spearmanr
import pandas as pd
import math

class Metric(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
    @classmethod    
    def dis_metric(cls, list1, list2):
    
        result = []
        for i in range(0, min(len(list1), len(list2))):
            if list1[i]==None or list2[i]==None:
                continue
            dis = float(abs(float(list1[i]) - float(list2[i])))
            result.append(dis)
    
        return result
    
    
    @classmethod 
    def error_metric(cls, list1, list2):
        dis_list = cls.dis_metric(list1, list2)
        dis_array = np.asarray(dis_list, dtype=np.float64)
        
        d_min = np.nanmin(dis_array)
        d_max = np.nanmax(dis_array)
        d_mean = np.nanmean(dis_array, dtype=np.float64)
        d_median = np.nanmedian(dis_array)
        d_std = np.nanstd(dis_array)
    
        result = [d_min,d_max,d_mean,d_median,d_std]
        return result

    @classmethod 
    def error_percentage(cls, sensor_list, est_list):
        
        unit_list = []
        dis_metric = cls.dis_metric(sensor_list, est_list)
        for i in range(0, min(len(sensor_list), len(est_list), len(dis_metric))):
            if sensor_list[i]==None or sensor_list[i]==0 or est_list[i]==None or dis_metric[i]==None :
                continue
            unit = float(abs(dis_metric[i]/sensor_list[i]))
            unit_list.append(unit)
         
        unit_arr = np.asarray(unit_list)   
        mape_mean = np.nanmean(unit_arr)
        
        return mape_mean
    
    # correlation: pearsonr
    @classmethod 
    def pearsonr_metric(cls, list1, list2):
        l1, l2 = [],[]
        for i in range(0, min(len(list1), len(list2))):
            if list1[i]==None or list2[i]==None or math.isnan(list1[i]) or math.isnan(list2[i]):
                continue
            l1.append(list1[i])
            l2.append(list2[i])
        print(l1)
        print(l2)
        result = pearsonr(l1,l2)
    #     print(result) # (Pearson’s correlation coefficient, 2-tailed p-value)
        return result

    @classmethod 
    def spearmanr_metric(cls, list1, list2):
        l1, l2 = [],[]
        for i in range(0, len(list1)):
            if list1[i]==None or list2[i]==None:
                continue
        result = spearmanr(l1,l2)
    #     print(result) # (Spearman’s correlation coefficient, 2-tailed p-value)
        return result


def main():
    
    arr1 = np.arange(0,10)
    print(arr1)
    arr2 = np.arange(100,130,3)
    print(arr2)
    print("----------------------------")
    print("Metric.dis_metric")
    print(Metric.dis_metric(arr1, arr2))
    
    
    print("----------------------------")
    print("Metric.error_metric")
    print(Metric.error_metric(arr1, arr2))
    
    print("----------------------------")
    print("Metric.error_percentage")
    print(Metric.error_percentage([8,8.5,9,9.4,10,10.5], [7,7.8,9.4,8.2,6.5]))
    
    print("----------------------------")
    print("Metric.pearsonr_metric")
    print(Metric.pearsonr_metric(arr1, arr2))
    

    print("----------------------------")
    print("Metric.spearmanr_metric")
    spearman_result = Metric.spearmanr_metric(arr1, arr2)
    print(spearman_result)
    print(spearman_result[0])
    print(spearman_result[1])
    
    
        
    return 0






if __name__ == '__main__': main()





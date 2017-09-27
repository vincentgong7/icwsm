'''
Created on 22 Sep 2017

@author: vgong
'''
import icwsm17.mfs.MF_flow_before_after as MF_flow_before_after
import icwsm17.entity.DBSource as DBS
import icwsm17.entity.ExperimentProfile as EP
import icwsm17.callers.case1.case1_ep as case1_ep
import icwsm17.mfs.toolbox as tb
import pandas as pd

class case2_before_after(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    
    
    def process(self, dic):    
        
#         strategy_suffix = 'probability'
        
        mfba = MF_flow_before_after.MF_flow_before_after.from_dbs_ep(dic)
        cell_id = dic["cell_id"]
        
        delta_ts = 30*60  # in seconds
        bin_ts = 30*60  # the bin timestamp size, here per hour, in seconds
        pedestrian_speed = 1.4  # the pedestrian speed is normally below 7.
        max_length = pedestrian_speed * delta_ts  # e.g. 7 * (30*60), delta_t_ts is in seconds
        
        '''for "before"'''
#         extra_out_put_flag = '_before' 

        record_start_ts = dic["ep"].start_ts
        record_end_ts = dic["ep"].end_ts
        before_prob_array = mfba.call_membership_fun_probability(cell_id, record_start_ts, record_end_ts, bin_ts, delta_ts, max_length)
        
        before_df = pd.DataFrame(before_prob_array[:,0],columns=['before'])
#         output_file = '{}/mf_{}_cell_{}{}.txt'.format(dic["outputfolder"], strategy_suffix, cell_id, extra_out_put_flag)
#         before_df.to_csv(output_file)
        
        
        '''for "after"'''
#         extra_out_put_flag = '_after' 
        record_start_ts = tb.date2ts('2016-04-25 23:30:00') 
        record_end_ts = tb.date2ts('2016-04-28 23:30:00')
        after_prob_array = mfba.call_membership_fun_probability(cell_id, record_start_ts, record_end_ts, bin_ts, delta_ts, max_length)
        after_df = pd.DataFrame(after_prob_array[:,1],columns=['after'])
#         output_file = '{}/mf_{}_cell_{}{}.txt'.format(dic["outputfolder"], strategy_suffix, cell_id, extra_out_put_flag)
#         after_df.to_csv(output_file)
        
        
        
        result_df = pd.concat([before_df, after_df], axis=1)
        
        
        print('\n\n\n !DONE! \n\n\n')
#         
        return result_df


def main():
    print ("This only executes when %s is executed rather than imported" % __file__)

    c2ba = case2_before_after()
    
    dic = {}
    dic["outputfolder"] = "/Users/vgong/Desktop/icwsm/kings2016/case2/data/sm_data/processed/0922-v1/rate"
    dbs = DBS.DBSource()
    dic["dbs"] = dbs
    ep = case1_ep.case1_ep.get_case1_ep()
    dic["ep"] = ep
    dic["mf.rate.twitter_table"] = 'case1smd.v_twitter_geo_is'
    dic["mf.rate.inst_table"] = 'case1smd.v_inst_geo_is'
    
    for cell_id in range(0,4):
        
        dic["cell_id"] = cell_id
        result_df = c2ba.process(dic)
        output_file = '{}/case_1_mf_flow_before_after_cell_{}.txt'.format(dic["outputfolder"], cell_id)
        result_df.to_csv(output_file)


if __name__ == '__main__': main()
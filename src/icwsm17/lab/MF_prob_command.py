'''
Created on 17 Sep 2017

@author: vgong
'''
import numpy as np
import icwsm17.mfs.MF_flow_rate_calculator as MFFRC


class MF_prob_command(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
    
    def calculate_flow_rate(self, folder):   
        
        output_file = "{}/flow_rate_per30min.txt".format(folder)
        
        a_up_in = np.load("{}/cam_count_A_up_in.txt.npy".format(folder))
        a_down_out = np.load("{}/cam_count_A_down_out.txt.npy".format(folder))
        f_up_out = np.load("{}/cam_count_F_up_out.txt.npy".format(folder))
        f_down_in = np.load("{}/cam_count_F_down_in.txt.npy".format(folder))
        smd_in = np.load("{}/mf_probability_cell_0_before.txt.npy".format(folder))
        smd_out = np.load("{}/mf_probability_cell_0_after.txt.npy".format(folder))
        
        mfrc = MFFRC.MF_flow_rate_calculator()
        cam_flow = mfrc.generate_flow_in_out_from_cam(a_up_in, a_down_out, f_up_out, f_down_in)
        smd_flow = mfrc.generate_smd_in_out(smd_in, smd_out)
        flow_rate = mfrc.generate_flow_rate(cam_flow, smd_flow)
        
        return flow_rate

def main():
    print ("This only executes when %s is executed rather than imported" % __file__)
    
    folder = '/Users/vgong/Desktop/icwsm/kings2016/case2/data/sm_data/processed/0916-v1'
    
    mfpc = MF_prob_command()
    #flow_rate: cam_flow_in_out, smd_in_out
    flow_rate = mfpc.calculate_flow_rate(folder)

    #basis
    
    
    #mf_flow = #basis+smd_in*flow_rate+smd_out*flow_rate
    
    
    return 0




if __name__ == '__main__': main()
'''
Created on 14 Feb 2017

@author: vgong
'''

# common function: write line to a file from a list
def write_to_file(data_list, file):
    with open(file, 'w') as f_w:
        for line in data_list:
            f_w.write("{0}".format(line))
    print("done.")

def mywritelines2file(data_list, file):
    with open(file, 'w') as f_w:
        for line in data_list:
            f_w.write("{0}\n".format(line))
    print("done.")

    
def printlist(a_list):
    for item in a_list:
        print('{}\n'.format(item))


def test_fun(a, b):
    c = a+b
    print(c)
    return c


test_fun(1)

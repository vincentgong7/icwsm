'''
Created on 30 May 2017

@author: vgong
'''

cell_points_list = []
# cell_points_list.append([[y1,x1],[y2,x2],[y3,x3],[y4,x4]]), the left-top is point1, clockwise

# this is the terrain of Zuidplein Amsterdam
cell_points_list.append([[52.340821, 4.872787], [52.340840, 4.873365], [52.339472, 4.873540], [52.33945, 4.87278]])

# this is the terrains of Sail event
# cell_points_list.append([[52.380853, 4.898841], [52.378196, 4.907432], [52.377343, 4.906678], [52.380259, 4.898109]])
# cell_points_list.append([[52.379857, 4.925105], [52.379209, 4.928704], [52.378781, 4.928566], [52.379371, 4.924914]])
# cell_points_list.append([[52.379352, 4.924892], [52.377850, 4.933742], [52.377177, 4.933332], [52.378710, 4.924574]])
# cell_points_list.append([[52.375891, 4.929162], [52.374704, 4.936065], [52.374124, 4.935806], [52.375251, 4.928784]])

# cell area, 1 ha = 10000 m2
cell_area = [0.640*10000]

# the half length of each cells
cell_half_length = [72]
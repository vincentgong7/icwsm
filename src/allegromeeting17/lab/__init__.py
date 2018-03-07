


import numpy as np
import pandas as pd
from pandas.core.frame import DataFrame
from scipy.spatial import ConvexHull


import pandas as pd, numpy as np
import matplotlib.pyplot as plt
# from sklearn.cluster import DBSCAN
# from geopy.distance import great_circle

# import matplotlib.pyplot as plt
from scipy.cluster.vq import kmeans2, whiten

folder = "/Users/vgong/Downloads/Kingsday_2016_social_media_data/"
inst_df = pd.read_csv(folder+"inst_post.csv.txt")
twitter_df = pd.read_csv(folder+"twitter_post.csv.txt")    


inst_lat = inst_df["latitude"].values
inst_lon = inst_df["longitude"].values

inst_coords = []
for i in range(len(inst_lat)):
    inst_coords.append([inst_lat[i],inst_lon[i]])

inst_coords = np.array(inst_coords)
# print(inst_coords)


# coordinates= np.array([
#            [lat, long],
#            [lat, long],
#             ...
#            [lat, long]
#            ])

# coordinates

x, group_id_list = kmeans2(whiten(inst_coords), 10, iter = 20)

# print(x)
# print(y[0:1000])


groups = [0,0,0,0,0,0,0,0,0,0]

print(groups)


gc0,gc1,gc2,gc3,gc4,gc5,gc6,gc7,gc8,gc9 = [],[],[],[],[],[],[],[],[],[]
gc = [gc0,gc1,gc2,gc3,gc4,gc5,gc6,gc7,gc8,gc9]

for i in range(len(group_id_list)):
    g_id = group_id_list[i]
#     print(t)
    groups[g_id] = groups[g_id] + 1
    
    gc[g_id].append(inst_coords[i])

print(groups)
print("------------")
# groups = # posts in each group
for i in range(len(gc)):
    print(len(gc[i]))
    hull = ConvexHull(gc[i])
    
#     plt.plot(inst_coords[hull.vertices,0], inst_coords[hull.vertices,1], 'r--', lw=2)
#     plt.plot(inst_coords[hull.vertices[0],0], inst_coords[hull.vertices[0],1], 'ro')
#     plt.show()
    
    print("area: {}".format(hull.area))
    print("density: {}".format(len(gc[i])/ hull.area))
    
    
    for h in range(len(hull.vertices)):
        print("{},{};".format(inst_coords[h][0],inst_coords[h][1]))
#     print(hull.vertices)
    print("-----")


    






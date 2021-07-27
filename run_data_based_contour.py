
# %% Header
from matplotlib import pyplot as plt
import networkx as nx
import numpy as np
from numpy.core.defchararray import asarray
from numpy.core.records import record

import networks
#import linkedList
import construct
import importlib
import algos1
import algos
importlib.reload(networks)
import csv 
from os import remove
#import sys
#print(algos.__file__)

#print(sys.path)

#print(dir())

# %% Setting basic variables
# x=y=16
# print (x,y)
processing_counter = 0
algorithms = [algos1.Algo1]
# algos = [contourAlgo.AlgoPixelCenter]

plt.rcParams['xtick.bottom'] = plt.rcParams['xtick.labelbottom'] = False
plt.rcParams['xtick.top'] = plt.rcParams['xtick.labeltop'] = True
#%% Creating Image
image = construct.imageV2()
(x,y,depth) = image.shape
print (x,y)
plt.imshow(image,'gray',vmin=0,vmax=255)
plt.show()
imarray = asarray(image)
#print(imarray)

#%% Creating Graph
shift = 0
G = nx.Graph()
G = networks.graph_twisted_torus(G,x,y,shift)

#print(G.edges)
#print(G.nodes)
#for me in G.nodes():
    #print(G.neighbors(me))
#     sorted_nbrs = algos.sort_neighbors(G,x,y,me)
#     for nbr in sorted_nbrs:
#      for nbr in G.neighbors(me):
#         print(me,nbr)
# %% Assigning image matrix to the graph
nx.set_node_attributes(G,1,"pixel")         
for node in G.nodes : 
    #print(node)
    for row in range(x):
        for col in range(y):
            #print(image[row,col])
            G.nodes[(row,col)]["pixel"] = image[row,col]  # assigning image to the graph
#print(nx.get_node_attributes(G,"pixel"))
# nx.set_node_attributes(G,0,"ROI")       # Region of Interest attribute
# nx.set_node_attributes(G,0,"scanned")       # Scanned or not attribute
# nx.set_edge_attributes(G,0,"hop_count") # attribute to count number of hops of each edge
# nx.set_edge_attributes(G,0,"is_corner") # attribute to count number of hops of each edge
# contourStack =[]
# algos1.AlgoRasterScan(G,x,y,contourStack)
# print(contourStack)



    
#remove("Hops_stacklen.csv")
twist_str = [["Twist"], [shift]]
records = open ('Hops_stacklen.csv', 'a', newline='')
with records:
    record_writer = csv.writer(records)
    record_writer.writerow(twist_str)
# %% Setting Region of Interest variable
for algo in algorithms:
    nx.set_node_attributes(G,0,"ROI")       # Region of Interest attribute
    nx.set_node_attributes(G,0,"scanned")       # Scanned or not attribute
    nx.set_edge_attributes(G,0,"hop_count") # attribute to count number of hops of each edge
    nx.set_edge_attributes(G,0,"is_corner") # attribute to count number of hops of each edge
    records = open ('Hops_stacklen.csv', 'a', newline='')
    contourStack = []
    contourStack,edge_cost, del_edge_cost  = algo(G,x,y,contourStack)

    #%% Assign ROI to image using pop in stack

    img_ROI = np.zeros((x,y,1), np.uint8)
    img_ROI.fill(255)
    for i in range(len(contourStack)):
        img_ROI[contourStack[i]] = 0
    print(algo)
    print ("ROI:")
    plt.imshow(img_ROI,'gray',vmin=0,vmax=255)


    #%% Displaying heat map of the edges
    hop_counter = 0
    for edge in G.edges():
        hop_counter += G.edges[edge]['hop_count']
        
    print("hop_counter = ",hop_counter)
    print("length of stack = ",len(contourStack))
    print("cost of adding new edges = ", edge_cost)
    print("cost of deleting unused edges = ", del_edge_cost)
    rec = [str(algo),str(hop_counter),str(len(contourStack))]    #row to be saved in the csv file for this algo
    with records:
        record_writer = csv.writer(records)
        record_writer.writerow(rec)
    import matplotlib.pyplot as plt
    edges,h_counts = zip(*nx.get_edge_attributes(G,'hop_count').items())
    #print(len(h_counts),len(edges))
    edge_labels = nx.get_edge_attributes(G,'hop_count')
    
    pos = {(x,y):(y,-x) for x,y in G.nodes()}                   # this shifts the origin to top left
    #print(pos)
    #nx.draw(G, pos, node_color='black', node_size=100, edgelist=edges, edge_color=h_counts, width=7.0, edge_cmap=plt.cm.Blues)
    
    plt.show()
    nx.draw(G, pos, node_color='lightgreen', node_size=100)
    nx.draw_networkx_edge_labels(G,pos,edge_labels)
    plt.show()

    ############# More ideas #########
    #-- Recursive searching : If 'me' is in ROI and the neighbor has same value as me then the neighbor might also be in ROI
    #-- Reconfigurable network : Based in the slope of the curve occuring, change the connections of the network predictably
    ##### to get the number of hops less


    # # %%
    # # Order of iteration is starting from right side and clockwise rotation
    # # first finding the non matching pixel in neighbors
    # # then finding the non matching pixel in neighbor of neighbors (discarding the non relevant neighbors of neighbors)
    # # breaking whenever we find the first match

    # #? Problems : Since all the nodes will be searching in parallel, there is no way to know which node is the first one
    # #? Therefore, an algorithm is to be found to make a *sequential* global list of the contour found
    # #? Or we can just make a stack of the points of the contour

    # %%

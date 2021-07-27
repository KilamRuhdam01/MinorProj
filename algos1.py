
from matplotlib.pyplot import flag
from networks import graph_step_twisted_torus
from networks import add_edges_diagonally
from networks import del_edges_diagonally
#%% Function to arrange the neighbors in clockwise direction
# def clockwise(nbrs):
#     print(nbrs)
#     return nbrs


# def sort_neighbors(G,x,y,me,shift):
#     nbr_array = [None]*6
#     (row,col) = me
#     print("###### me ########", me)
#     for nbr in G.neighbors(me):
        
#         (nrow,ncol) = nbr
#         # col checking
#         if (nrow == row) and (ncol == (col+1)%y):   #nbr(0) is always the same for both cases
#             print('element0', nbr)
#             nbr_array[0] = nbr
#         # for a positive shift you have first nbr on the diagonal and then subsequently others
#         if shift == 1: 

#             if (nrow == (row+1)%x) and (ncol == (col+1)%y and nrow == ncol):
#                 print("element1",nbr)
#                 nbr_array[1] = nbr
#             if((nrow == (row +1)%x) and (ncol == col) and nrow != x ):  # second element in the nbr is from the next row but not for the last row
#                 print('element2',nbr)
#                 nbr_array[2] = nbr
#             if ((nrow == row) and (ncol == (col-1)%y)):
#                 print('element3',nbr)
#                 nbr_array[3] = nbr
#             if ((nrow == (row-1)%x) and (ncol == (col-1)%y)):
#                 print('element 4',nbr)
#                 nbr_array[4] = nbr
#             if ((nrow == (row-1)%x) and (ncol == col)):
#                 print('element 5',nbr)
#                 nbr_array[5] = nbr

#         if shift == -1: 

#             if (nrow == (row+1)%x) and (ncol == (col-1)%y ):
#                 nbr_array[2] = nbr
#             if((nrow == (row +1)%x) and (ncol == col) and nrow != x ):  # second element in the nbr is from the next row but not for the last row
#                 print('element 2')
#                 nbr_array[1] = nbr
#             if ((nrow == row) and (ncol == (col-1)%y)):
#                 print('3 element')
#                 nbr_array[3] = nbr
#             if ((nrow == (row-1)%x) and (ncol == col)):
#                 print('element 4')
#                 nbr_array[4] = nbr
#             if ((nrow == (row-1)%x) and (ncol == (col-1)%y)):
#                 print('element 5')
#                 nbr_array[5] = nbr
        
#         #else:                          #case of twist ; whatever is remaining that is assigned the twisted node
#         if (nbr_array[0] == None): nbr_array[0] = nbr
#         elif (nbr_array[1] == None): nbr_array[1] = nbr
#         elif (nbr_array[2] == None): nbr_array[2] = nbr
#         elif (nbr_array[3] == None): nbr_array[3] = nbr
#         elif (nbr_array[4] == None): nbr_array[4] = nbr
#         elif (nbr_array[5] == None): nbr_array[5] = nbr

#     return nbr_array

#%% Image neighbor search with neighbor setting
def Algo1(G,x,y,contourStack):
    n = -1
    initial_shift = 0
    row = 0 
    later_shift = 0
    new_edge_cost =0
    edge_cost = 0 
    del_edge_cost = 0
    while row <x:
        col = 0
        if initial_shift == 1 or later_shift == 1:   
            col = node2[1]%y                            #node2 is the top node of the stack use to set the col rom where to scan next

        elif initial_shift == -1 or later_shift == -1 :
            # nodex = contourStack[n]
            col = (node2[1]-1)%y
            #print("###I am node2 ###",  node2)          # node2 is the top most node of the stack used to set the column from where we scan next
            if later_shift == -15:                      # Case when we have an overflowing V in our image
                print("setting the col to zero")
                col = 0
 
        while col <y:
            me = (row,col)
            print("Scanning ####", me)
            if (G.nodes[me]["ROI"] != 1):       # If not already set as ROI
                sorted_nbrs= sort_neighbors(G,x,y,me,initial_shift)
            
                for nbr in sorted_nbrs:     # check with all my neighbors
                    if (G.nodes[me]["ROI"] != 1 ):       # If not already set as ROI  
                        G.edges[me, nbr]['hop_count'] += 1      # error on hop_count since the new edges dont have a key hop_count
                        if (G.nodes[nbr]["pixel"] > G.nodes[me]["pixel"]):
                            n +=1               # keeps track of the nodes pushed in the contourStack
                            print(" ##### n ####", n)
                            G.nodes[me]["ROI"] = 1
                            print("##### me added to the ROI #####", me)
                            contourStack.append(me)
                            
                        if (G.nodes[nbr]["ROI"] != 1):       # If not already set as ROI
                            if (G.nodes[nbr]["pixel"] < G.nodes[me]["pixel"]):
                                G.nodes[nbr]["ROI"] = 1
                                print("##### nbr added to the ROI #####", nbr)
                                contourStack.append(nbr)
                                if later_shift != initial_shift:
                                    ssorted_nbrs= sort_neighbors(G,x,y,nbr,later_shift)
                                else :
                                    ssorted_nbrs= sort_neighbors(G,x,y,nbr,initial_shift)
                                nbr1 = ssorted_nbrs[0]                                      # we are always bringing up the first diagonal nbr in sort
                                if G.nodes[nbr1]["ROI"] !=1:
                                    G.edges[nbr, nbr1]['hop_count'] += 1
                                    if (G.nodes[nbr1]["pixel"] == G.nodes[nbr]["pixel"]) and G.nodes[nbr1]["ROI"]!=1:
                                        G.nodes[nbr1]["ROI"] = 1
                                        print("##### nbr of nbr added to the ROI #####", nbr1)
                                        contourStack.append(nbr1)
                                        n+=1
                                n+=1
                                print("### n ###",n)
                                
                                                
            col = col+1

        if(n==1 and initial_shift == 0):               # initial check if there are exactly two nodes in the stack 
            node1 = contourStack[n-1]
            node2 = contourStack[n]
            print(node1)
            print(node2)
            print("\nThese are the first two nodes popped off the stack",node1,node2)
            #print("\n Difference between row",node1[0]-node2[0])
            print("\nDifference between col",node2[1]-node1[1])
            initial_shift  = node2[1]-node1[1]

            if (initial_shift == -1):       # add edges on the diagonal from NE to SW
                         
                print("Changing graph negative shift")
                edge_cost = add_edges_diagonally(G,x,y,initial_shift,node2[0],node2[1])     # pass the start points of the digonal shifted connection
           
                
            elif (initial_shift == 1):      # add edges on the diagonal from NW to SE

                print("Changing graph positive shift")
                edge_cost = add_edges_diagonally(G,x,y,initial_shift,node2[0],node2[1])

            else: 
                print("Not changing the graph")
                #continue                    # if neither positive or negative shift required continue do nothing

        elif n >=2 :                        # subsequent shifts to figure out the starting column
            node1 = contourStack[n-1]
            node2 = contourStack[n]
            if (node2[0] != node1[0]):
                later_shift = node2[1] - node1[1]
            
            print("later_shift", later_shift)    ####change connections with later shift
            if later_shift != initial_shift : 
                print("later shift is different")
                print("node1", node1)
                new_edge_cost = new_edge_cost+ add_edges_diagonally(G,x,y,later_shift,node2[0],node2[1])
                del_edge_cost = del_edges_diagonally(G,x,y,initial_shift,node1[0],node1[1])
                initial_shift = later_shift       

                # if (row == node2[0]):
                #     row = row+1
                # else : row = node2[0]
                
                
           
        row = row+1    

    edge_cost = new_edge_cost+edge_cost          
    return contourStack, edge_cost,del_edge_cost


#%% Image neighbor search with neighbor setting
def Algo1_Prev(G,x,y,contourStack):
    edge_cost = 0
    del_edge_cost = 0
    for row in range(x):
        for col in range(y):
            me = (row,col)
            if (G.nodes[me]["ROI"] != 1):       # If not already set as ROI
                for nbr in G.neighbors(me):     # check with all my 4 neighbors
                    if (G.nodes[me]["ROI"] != 1):       # If not already set as ROI
                        G.edges[me, nbr]['hop_count'] += 1
                        if (G.nodes[nbr]["pixel"] > G.nodes[me]["pixel"]):
                            G.nodes[me]["ROI"] = 1
                            contourStack.append(me)
                        if (G.nodes[nbr]["ROI"] != 1):       # If not already set as ROI
                            if (G.nodes[nbr]["pixel"] < G.nodes[me]["pixel"]):
                                G.nodes[nbr]["ROI"] = 1
                                contourStack.append(nbr)
    return contourStack, edge_cost,del_edge_cost



def sort_neighbors(G,x,y,me,shift=0):
    nbr_array = [None]*6
    (row,col) = me
    for nbr in G.neighbors(me):
        (nrow,ncol) = nbr
        # col checking
        if (nrow == row):
            if (ncol == (col+1)%y):
                nbr_array[0] = nbr
            elif (ncol == (col-1)%y):
                nbr_array[2] = nbr
        elif (ncol == col):
            if (nrow == (row+1)%x):
                nbr_array[1] = nbr
            elif (nrow == (row-1)%x):
                nbr_array[3] = nbr
        ######## shift 1 #######
        if shift == 1: 
            if (nrow == (row+1)%x and ncol == (col+1)%y):
                nbr_array[5] = nbr
            elif (nrow == (row-1)%x and ncol == (col-1)%y):
                nbr_array[4] = nbr
        ###### shift -1 ######
        if shift == -1:
            # if (nrow+ncol == row+ col):          # this implies that the shift is -1
            if(nrow == (row +1)%x and ncol == (col-1)%y):
                nbr_array[5] = nbr                  # nbr to the south in last
            elif (nrow == (row-1)%x and ncol == (col+1)%y): 
                nbr_array[4] = nbr                  # nbr to north second last
    if shift == 1 or shift == -1:   # in both cases since we are moving from top to bottom we have to move the south nbr to first position
        temp = nbr_array[0]
        if nbr_array[5]  != None:
            nbr_array[0] = nbr_array[5]
            nbr_array[5] = temp
        
        # else:                          #case of twist ; whatever is remaining that is assigned the twisted node
        #     if (nbr_array[0] == None): nbr_array[0] = nbr
        #     elif (nbr_array[1] == None): nbr_array[1] = nbr
        #     elif (nbr_array[2] == None): nbr_array[2] = nbr
        #     elif (nbr_array[3] == None): nbr_array[3] = nbr
    nbr_array = list(filter(None, nbr_array))
       

    return nbr_array




#%% Pixel-center tracing method
# Raster Scan (left to right) used to detect the first point in the contour. And then pixel neighbors
# are followed in clockwise fashion to continue the tracing
def AlgoPixelCenter(G,x,y,contourStack):
# Pseudocode :
#
# me is the first contour point
# Iterate over my 4 nbr
#   Is this nbr in ROI?
#       yes :   Push in ROI; Iterate over my 4 neighbors
#       no  :   Go to the next neighbor
#   all neighbors done -> return

    def searchNeighbor(me):
        # Iterate over my 4 nbr
        # cw_nbr = clockwise(G.neighbors(me))
        sorted_nbrs1 = sort_neighbors(G,x,y,me)
#        for nbr in sorted_nbrs1:     # check with all my 4 neighbors
        for i in range(2):              # check with 2 neighbors only
            nbr = sorted_nbrs1[i]
            if (G.nodes[me]["scanned"] == 0):
                # print("scanning: ",me,nbr)
                G.edges[me, nbr]['hop_count'] += 1
                if (G.nodes[nbr]["ROI"] != 1):
                    #   Is this nbr in ROI?
                    sorted_nbrs2 = sort_neighbors(G,x,y,nbr)
                    
                    for nbr2 in sorted_nbrs2:     # check with all my  neighbors
                        if nbr2 != None : 
                           
                            if (G.nodes[nbr]["scanned"] == 0):
                                # print("scanning: ",nbr,nbr2)
                                G.edges[nbr, nbr2]['hop_count'] += 1
                                if ((G.nodes[nbr2]["pixel"] > G.nodes[nbr]["pixel"]) and G.nodes[nbr]["ROI"] != 1):
                                    G.nodes[nbr]["ROI"] = 1
                                   
                                #       yes :   Push in ROI; Iterate over my 4 neighbors
                                    contourStack.append(nbr)
                                    # print("pushed: ",nbr)
                                    # print(nbr,G.nodes[nbr]["ROI"])
                                    searchNeighbor(nbr)
                            #       no  :   Go to the next neighbor
                                if ((G.nodes[nbr2]["pixel"] < G.nodes[nbr]["pixel"]) and G.nodes[nbr2]["ROI"] != 1):
                                    G.nodes[nbr2]["ROI"] = 1
                                #       yes :   Push in ROI; Iterate over my 4 neighbors
                                    contourStack.append(nbr2)
                                    # print("pushed: ",nbr2)
                                    # print(nbr,G.nodes[nbr]["ROI"])
                                    searchNeighbor(nbr2)
                        #       no  :   Go to the next neighbor
                G.nodes[nbr]["scanned"] = 1
        #   all neighbors done -> return
        G.nodes[me]["scanned"] = 1
        return

    # foundFirst = 0
    # Finding first contour point
    for row in range(x):
        # if (foundFirst == 1): break
        for col in range(y):
            # if (foundFirst == 1): break
            me = (row,col)
            sorted_nbrs = sort_neighbors(G,x,y,me)
            print("###### me #####", me)
            print(sorted_nbrs)
            nbr_count = -1
            for nbr in sorted_nbrs:     # check with all my  neighbors
                nbr_count +=1
                if nbr != None:         # only check if the neighbour exists 
                    if (G.nodes[me]["scanned"] == 0):
                        # print("scanning: ",me,nbr)
                        # if (foundFirst == 1): break
                        G.edges[me, nbr]['hop_count'] += 1
                        if ((G.nodes[nbr]["pixel"] > G.nodes[me]["pixel"]) and G.nodes[me]["ROI"] != 1):
                            G.nodes[me]["ROI"] = 1
                            contourStack.append(me)
                            
                            # print("pushed: ",me)
                            searchNeighbor(me)
                            # print(me,G.nodes[me]["ROI"])
                            # firstNode = me
                            # foundFirst = 1
                        if ((G.nodes[nbr]["pixel"] < G.nodes[me]["pixel"]) and G.nodes[nbr]["ROI"] != 1):
                            G.nodes[nbr]["ROI"] = 1
                            contourStack.append(nbr)
                            # if nbr_count == 5 : 
                            #     print("Next neigbour will be found likely on south diagonal ")
                            # print("pushed: ",nbr)
                            searchNeighbor(nbr)
                            # print(nbr,G.nodes[nbr]["ROI"])
                            # foundFirst = 1
                            # firstNode = nbr
            G.nodes[me]["scanned"] = 1
    # print(firstNode,G.nodes[firstNode]["ROI"])
    # searchNeighbor(firstNode)
    return contourStack
#%% Plain image neighbor search
def Algo0(G,x,y,contourStack):
    #n = -1
    for row in range(x):
        for col in range(y):
            me = (row,col)
            # if (row == 1 and col ==14):
            #     print("Last col")
            #     print(G.nodes[me]["ROI"])
            #     for nbr in G.neighbors(me):     # check with all my 4 neighbors
            #         print(nbr)
            if (G.nodes[me]["ROI"] != 1):       # If not already set as ROI
                #print("#######",me,"#######")
                for nbr in G.neighbors(me):     # check with all my 4 neighbors
                    # if (row == 1 and col ==14):
                    #     print(nbr)
                    if (G.nodes[me]["ROI"] != 1):       # If not already set as ROI
                        G.edges[me, nbr]['hop_count'] += 1
                        if (G.nodes[nbr]["pixel"] > G.nodes[me]["pixel"]):
                            G.nodes[me]["ROI"] = 1
                            contourStack.append(me)
                            # n = n+1                         # counter to keep track of the last element in the list
            
                            # if (len(contourStack) !=0):         # writing the code to the appended pixel with the previous pixel in contour
                            #     previous = contourStack[n]      # this is the last pixel appended'
                            #     if (row == previous[0]) and (col == previous[1]):   # means the direction of shift has to be NE-SW
                            #         G = graph_step_twisted_torus(G,x,y,1)
                            #     print("#######",previous)
    return contourStack

#%% Pixel-Corner Tracing Algo
def AlgoPixelCorner(G,x,y,contourStack):
    cornerStack = []
    for row in range(x):
        for col in range(y):
            me = (row,col)
            sorted_nbrs = sort_neighbors(G,x,y,me)
            # for nbr in sorted_nbrs:
            for i in range(2):
                nbr = sorted_nbrs[i]
                if ((G.nodes[me]["scanned"] == 0) and 
                    (G.edges[me, nbr]['is_corner'] == 0)):
                    # print("scanning: ",me,nbr)
                    G.edges[me, nbr]['hop_count'] += 1
                    if (G.nodes[nbr]["pixel"] != G.nodes[me]["pixel"]):
                        G.edges[me, nbr]['is_corner'] = 1
                        cornerStack.append((me,nbr))
                        G.nodes[me]["ROI"] = 1
                        G.nodes[nbr]["ROI"] = 1
    for row in range(x):
        for col in range(y):
            me = (row,col)
            if (G.nodes[me]["ROI"] == 1):
                contourStack.append(me)
    return contourStack

#%% Raster Scan Algorithm
def AlgoRasterScan(G,x,y,contourStack):
    edge_cost = 0
    del_edge_cost = 0
    i = [0]         # only right neighbor
    cornerStack = []
    for row in range(x):
        for col in range(y):
            me = (row,col)
            
            sorted_nbrs = sort_neighbors(G,x,y,me)
            
            for index in i:     
                nbr = sorted_nbrs[index]
                G.edges[me, nbr]['hop_count'] += 1
                if (G.nodes[nbr]["pixel"] != G.nodes[me]["pixel"]):
                    if (G.nodes[me]["pixel"] == 0):
                        cornerStack.append(me)
                    else:
                        cornerStack.append(nbr)
    # finding the contour
    # while len(cornerStack) != 0:    #iterate till list is empty
    #     (row2,col2) = cornerStack.pop()
    #     (row1,col1) = cornerStack.pop()
    #     if (row1==row2):
    #         for i in range(col1,col2+1):
    #             contourStack.append((row1,i))
    return(cornerStack), edge_cost, del_edge_cost
    # return(contourStack)
# %%

# #%% Single Processor Pixel Following Algorithm
# def AlgoSinPixelCenter(image,contourStack):

#     def nbrloc(locme):
#         (row,col) = locme
#         loc[0] = (row,(col+1)%y)       #east neighbour
#         loc[1] = ((row+1)%x,col)       #south neighbour
#         loc[2] = (row,(col-1)%y)        #west neighbour
#         loc[3] = ((row-1)%x,col)        #north neighbour
#         return loc

#     def searchNeighbor(locme):
#         loc1 = nbrloc(locme)
#         for k in range(4):
#             if (scanned[locme] == 0):
#                 process_count += 1
#                 if (ROI[loc1[k]] != 1):
#                     loc2 = nbrloc(loc1[k])
#                     for j in range(4):
#                         if (scanned[loc1[j]] == 0):
#                             process_count += 1
#                             if (image[loc2[j]] > image[loc1[k]]):
#                                 ROI[loc1[k]] = 1
#                                 contourStack.append(loc1[k])
#                                 searchNeighbor(loc1[k])
#                 scanned[loc1[k]] = 1
#         scanned[locme] = 1
#         return   

#     (x,y,depth) = image.shape
#     rows, cols = (x, y)
#     scanned = [[0]*cols]*rows
#     ROI = [[0]*cols]*rows
#     process_count = 0
#     # Finding first contour point
#     for row in range(rows):
#         for col in range(cols):
#             locme = (row,col)
#             loc = nbrloc(locme)
#             for i in range(2):
#                 if (scanned[locme] == 0):        # not scanned yet
#                     process_count += 1
#                     if (image[loc[i]] > image[locme]):
#                         ROI[locme] = 1
#                         contourStack.append(locme)
#                         searchNeighbor(locme)
#                     if (image[loc[i]] < image[locme]):
#                         ROI[loc[i]] = 1
#                         contourStack.append(loc[i])
#                         searchNeighbor(loc[i])
#             scanned[locme] = 1
#     return contourStack



# %%

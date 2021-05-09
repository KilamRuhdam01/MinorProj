#%% Function to arrange the neighbors in clockwise direction
# def clockwise(nbrs):
#     print(nbrs)
#     return nbrs
def sort_neighbors(G,x,y,me):
    nbr_array = [None]*4 
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
    for i in range(len(nbr_array)-1):
        if nbr_array[i] == None:
            del nbr_array[i]
    return nbr_array

#%% Plain image neighbor search
def Algo0(G,x,y,contourStack):
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
    return contourStack

#%% Image neighbor search with neighbor setting
def Algo1(G,x,y,contourStack):
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
    return contourStack

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
        for nbr in sorted_nbrs1:     # check with all my 4 neighbors
            if (G.nodes[me]["scanned"] == 0):
                # print("scanning: ",me,nbr)
                G.edges[me, nbr]['hop_count'] += 1
                if (G.nodes[nbr]["ROI"] != 1):
                    #   Is this nbr in ROI?
                    sorted_nbrs2 = sort_neighbors(G,x,y,nbr)
                    for nbr2 in sorted_nbrs2:     # check with all my 4 neighbors
                        if (G.nodes[nbr]["scanned"] == 0):
                            # print("scanning: ",nbr,nbr2)
                            G.edges[nbr, nbr2]['hop_count'] += 1
                            if (G.nodes[nbr2]["pixel"] > G.nodes[nbr]["pixel"]):
                                G.nodes[nbr]["ROI"] = 1
                            #       yes :   Push in ROI; Iterate over my 4 neighbors
                                contourStack.append(nbr)
                                # print(nbr,G.nodes[nbr]["ROI"])
                                searchNeighbor(nbr)
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
            print(me)
            sorted_nbrs = sort_neighbors(G,x,y,me)
            print(sorted_nbrs)
            # for nbr in sorted_nbrs:     # check with all my 4 neighbors
            for i in range(2):
                nbr = sorted_nbrs[i]
                
                if (G.nodes[me]["scanned"] == 0):
                    # print("scanning: ",me,nbr)
                    # if (foundFirst == 1): break
                    print(G.edges[me,nbr])
                    G.edges[me, nbr]['hop_count'] += 1
                    if (G.nodes[nbr]["pixel"] > G.nodes[me]["pixel"]):
                        G.nodes[me]["ROI"] = 1
                        contourStack.append(me)
                        searchNeighbor(me)
                        # print(me,G.nodes[me]["ROI"])
                        # firstNode = me
                        # foundFirst = 1
                    if (G.nodes[nbr]["pixel"] < G.nodes[me]["pixel"]):
                        G.nodes[nbr]["ROI"] = 1
                        contourStack.append(nbr)
                        searchNeighbor(nbr)
                        # print(nbr,G.nodes[nbr]["ROI"])
                        # foundFirst = 1
                        # firstNode = nbr
            G.nodes[me]["scanned"] = 1
    # print(firstNode,G.nodes[firstNode]["ROI"])
    # searchNeighbor(firstNode)
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
    while len(cornerStack) != 0:    #iterate till list is empty
        (row2,col2) = cornerStack.pop()
        (row1,col1) = cornerStack.pop()
        if (row1==row2):
            for i in range(col1,col2+1):
                contourStack.append((row1,i))
    return(contourStack)
# %%

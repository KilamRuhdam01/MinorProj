
from matplotlib.pyplot import flag
#from networks import graph_step_twisted_torus
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
    # scan all rows 
    while row <x:
          # initialise col value to 0, the check for contour slope to figure out where to start the scan from
        col = 0                                        
        if initial_shift == 1 or later_shift == 1:   
            col = node2[1]%y                            #node2 is the top node of the stack used to set the col from where to scan next

        elif initial_shift == -1 or later_shift == -1 :
            col = (node2[1]-1)%y                        # node2 is the top most node of the stack used to set the column from where we scan next
            if later_shift == -15:                      # Case when we have an overflowing V in our image
                print("setting the col to zero")
                col = 0

        # scan all col wise for each row
        while col <y:
            me = (row,col)
            print("Scanning ####", me)
            if (G.nodes[me]["ROI"] != 1):                # If not already set as ROI
                # use sorted neighbors, neighbors are sorted as per the slope of the contour
                sorted_nbrs= sort_neighbors(G,x,y,me,initial_shift)
                for nbr in sorted_nbrs:                 # check with all my neighbors
                    if (G.nodes[me]["ROI"] != 1 ):      # If not already set as ROI  
                        # earlier : error on hop_count since the new edges dont have a key hop_count, since then corrected 
                        G.edges[me, nbr]['hop_count'] += 1      
                        if (G.nodes[nbr]["pixel"] > G.nodes[me]["pixel"]):
                            n +=1                       # keeps track of the  number of nodes pushed in the contourStack
                            print(" ##### n ####", n)
                            G.nodes[me]["ROI"] = 1
                            print("##### me added to the ROI #####", me)
                            contourStack.append(me)
                            
                        if (G.nodes[nbr]["ROI"] != 1):       # If not already set as ROI
                            if (G.nodes[nbr]["pixel"] < G.nodes[me]["pixel"]):
                                n+=1
                                G.nodes[nbr]["ROI"] = 1
                                print("##### nbr added to the ROI #####", nbr)
                                contourStack.append(nbr)
                                # check for the next neighbor along the shift
                                if later_shift != initial_shift:
                                    ssorted_nbrs= sort_neighbors(G,x,y,nbr,later_shift)
                                else :
                                    ssorted_nbrs= sort_neighbors(G,x,y,nbr,initial_shift)
                                # we are always bringing up the first diagonal nbr in sort so only need to check the first one
                                nbr1 = ssorted_nbrs[0]                                  
                                if G.nodes[nbr1]["ROI"] !=1:
                                    G.edges[nbr, nbr1]['hop_count'] += 1
                                    if (G.nodes[nbr1]["pixel"] == G.nodes[nbr]["pixel"]) and G.nodes[nbr1]["ROI"]!=1:
                                        G.nodes[nbr1]["ROI"] = 1
                                        print("##### nbr of nbr added to the ROI #####", nbr1)
                                        contourStack.append(nbr1)
                                        n+=1
                                
                                print("### n ###",n)
                                
                                                
            col = col+1
        # initial check if there are exactly two nodes in the stack and then finding the initial slope
        if(n==1 and initial_shift == 0):               
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
                # add new edges, pass the start points of the digonal shifted connection
                edge_cost = add_edges_diagonally(G,x,y,initial_shift,node2[0],node2[1])     
           
                
            elif (initial_shift == 1):      # add edges on the diagonal from NW to SE

                print("Changing graph positive shift")
                edge_cost = add_edges_diagonally(G,x,y,initial_shift,node2[0],node2[1])

            # if neither positive or negative shift required continue do nothing
            else: 
                print("Not changing the graph")

        # if the number of nodes is greater than 2, check for change in slope                           
        elif n >=2 :                        # subsequent shifts to figure out the starting column
            node1 = contourStack[n-1]
            node2 = contourStack[n]
            if (node2[0] != node1[0]):
                later_shift = node2[1] - node1[1]
            
            print("later_shift", later_shift)  
            ####change connections with later shift  
            if later_shift != initial_shift : 
                print("later shift is different")
                print("node1", node1)
                # calculate cost of adding new edges 
                new_edge_cost = new_edge_cost+ add_edges_diagonally(G,x,y,later_shift,node2[0],node2[1])
                # delete redundant edges if the slope has changed now
                del_edge_cost = del_edges_diagonally(G,x,y,initial_shift,node1[0],node1[1])
                initial_shift = later_shift       
        
        row = row+1    

    edge_cost = new_edge_cost+edge_cost          
    return contourStack, edge_cost,del_edge_cost


#%% Image neighbor search with neighbor setting
# this is the previous version of Algo1 for comparison purposes
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


# sort neighbors as per the shift
def sort_neighbors(G,x,y,me,shift=0):
    # nbr array has 6 elements since you can have diagonal edges
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
                nbr_array[5] = nbr                # nbr to the south in the last
            elif (nrow == (row-1)%x and ncol == (col-1)%y):
                nbr_array[4] = nbr                # nbr to the north second last
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
    
    # delete empty entires from the nbr array being returned 
    nbr_array = list(filter(None, nbr_array))
    return nbr_array


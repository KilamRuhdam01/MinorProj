#%% A file to define different networks for experimentation
import networkx as nx

#%% Function to make a twisted torus network
def graph_twisted_torus(G,x,y,shift):
    G.clear()
    G = nx.grid_2d_graph(x, y, periodic=False, create_using=None)       #simple 2D graph without wraparound
    for row in range(x):
        G.add_edge((row,0),(row,y-1))
    for col in range(y):
        G.add_edge((0,col),(x-1,(col+shift)%y))              #connect to next column takes care of connecting last column to first
        
    return G

#%% Function to make a simple 2D graph with no torus like connectivity
def graph_simple(G,x,y,shift):
    G.clear()
    G = nx.grid_2d_graph(x, y, periodic=False, create_using=None) 
    for row in range(x):                                    # this adds the horizontal twist of the torus
        G.add_edge((row,0), (row,y-1), hop_count = 0)
    return G


# %% Function to add edges digonally as per the slope and from the particular starting node
def add_edges_diagonally(G,x,y,shift,start_row,start_col):
    edge_cost = 0
    row = 0 
    if (shift == 1):
        row = start_row
        col = start_col
        while (col<y):
            G.add_edge((row,col),((row+1)%x,(col+shift)%y), hop_count = 0)
            edge_cost +=0.5
            col = col +1
            row = row+1
    elif(shift == -1):
        row = start_row
        col = start_col
        while (col >0):
            G.add_edge((row,col), ((row+1)%x, (col+shift)%y), hop_count = 0)   
            edge_cost +=0.5
            col = col -1
            row = row +1
    return edge_cost

#%% Function to delete edges as per the slope and starting node
def del_edges_diagonally(G,x,y,shift,start_row,start_col):
    edge_cost = 0
    row = 0 
    if (shift == 1):
        row = start_row
        col = start_col
        while (col<y):
            G.remove_edge((row,col),((row+1)%x,(col+shift)%y))
            edge_cost +=0.25
            col = col +1
            row = row+1
    elif(shift == -1):
        row = start_row
        col = start_col
        while (col >0):
            G.remove_edge((row,col), ((row+1)%x, (col+shift)%y))   
            edge_cost +=0.25
            col = col -1
            row = row +1
    return edge_cost






# # %% Func
# def graph_step_twisted_torus(G,x,y,shift):                  #shift can be +1 or -1 depending on what slope is predicted
#     G.clear()
#     G = nx.grid_2d_graph(x,y,periodic = False, create_using = None)
#     for row in range(x):                        # add edges for the horizontal twisted torus
#         G.add_edge((row,0), (row,y-1))
#     row = 0 
#     if (shift == 1):
#         while (row<x):
#             for col in range(y):
#                 G.add_edge((row,col),((row+1)%x,(col+shift)%y))
#                 row = row+1
#     elif(shift == -1):
#         col = y-1
#         row = 0 
#         while (col >0):
#             G.add_edge((row,col), ((row+1)%x, (col+shift)%y))   
#             col = col -1
#             row = row +1
#     return G


# def graph_4_connected(G,x,y):
#     G.clear()
#     G = nx.grid_2d_graph(x,y,periodic = False,create_using = None)
#     for row in range(y):
#         for col in range(x):
#             G.add_edge((col,row),((col+1)%x,row))   #connect to the next column
#             if row !=y-1:
#                 G.add_edge((col,row),(col,(row+1)%y))    #connect to the pixel below except for the last pixel
#             # this completes adding the edges since the edges are bidirectional and we have already added edges
#             # to pixels on the left and on top
#     return G

# def graph_8_connected(G,x,y):
#     G.clear()
#     G = nx.grid_2d_graph(x,y,periodic = False,create_using = None)
#     for row in range(y):
#         for col in range(x):
#             G.add_edge((col,row),((col+1)%x,row))   #coonect to the next column
#             if row !=y-1:
#                 G.add_edge((col,row),(col,(row+1)%y))    #connect to the pixel below except for the last pixel
#             # this completes adding the edges since the edges are bidirectional and we have already added edges
#             # to pixels on the left and on top
#     return G
